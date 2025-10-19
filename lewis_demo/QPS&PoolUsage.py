import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

class ConnectionPoolAnalyzer:
    def __init__(self, safety_margin=0.2, max_usage_threshold=0.8):
        """
        初始化分析器
        
        Parameters:
        safety_margin: 安全边际系数
        max_usage_threshold: 最大使用率阈值
        """
        self.safety_margin = safety_margin
        self.max_usage_threshold = max_usage_threshold
        self.model = None
        self.scaler = StandardScaler()
        
    def analyze_pool_capacity(self, df):
        """
        分析连接池容量
        
        Parameters:
        df: 包含QPS、排队数、使用率的数据框
        
        Returns:
        dict: 分析结果和建议
        """
        results = {}
        
        # 1. 基础统计分析
        results['basic_stats'] = self._get_basic_stats(df)
        
        # 2. 容量瓶颈识别
        results['bottleneck_analysis'] = self._identify_bottlenecks(df)
        
        # 3. QPS与使用率关系建模
        results['relationship_model'] = self._model_qps_usage_relationship(df)
        
        # 4. 容量建议
        results['recommendations'] = self._generate_recommendations(
            results['basic_stats'], 
            results['bottleneck_analysis'],
            results['relationship_model']
        )
        
        return results
    
    def _get_basic_stats(self, df):
        """获取基础统计信息"""
        stats = {
            'qps_stats': {
                'mean': df['应用QPS'].mean(),
                'max': df['应用QPS'].max(),
                'p95': df['应用QPS'].quantile(0.95),
                'p99': df['应用QPS'].quantile(0.99)
            },
            'usage_stats': {
                'mean': df['Usage-polarDB（连接池使用率）'].mean(),
                'max': df['Usage-polarDB（连接池使用率）'].max(),
                'p95': df['Usage-polarDB（连接池使用率）'].quantile(0.95)
            },
            'queue_stats': {
                'max_queue': df['padding-polarDB(连接池排队数)'].max(),
                'queue_occurrence_rate': (df['padding-polarDB(连接池排队数)'] > 0).mean()
            }
        }
        return stats
    
    def _identify_bottlenecks(self, df):
        """识别容量瓶颈"""
        bottlenecks = {
            'high_usage_periods': len(df[df['Usage-polarDB（连接池使用率）'] >= 100]),
            'queue_periods': len(df[df['padding-polarDB(连接池排队数)'] > 0]),
            'critical_periods': len(df[
                (df['Usage-polarDB（连接池使用率）'] >= 100) & 
                (df['padding-polarDB(连接池排队数)'] > 0)
            ])
        }
        
        # 计算瓶颈时间占比
        total_periods = len(df)
        bottlenecks['high_usage_ratio'] = bottlenecks['high_usage_periods'] / total_periods
        bottlenecks['queue_ratio'] = bottlenecks['queue_periods'] / total_periods
        bottlenecks['critical_ratio'] = bottlenecks['critical_periods'] / total_periods
        
        return bottlenecks
    
    def _model_qps_usage_relationship(self, df):
        """建立QPS与使用率的关系模型"""
        # 过滤掉使用率100%的异常点（可能已经达到上限）
        normal_data = df[df['Usage-polarDB（连接池使用率）'] < 100]
        
        if len(normal_data) < 10:
            # 如果正常数据太少，使用所有数据
            normal_data = df
        
        X = normal_data[['应用QPS']].values
        y = normal_data['Usage-polarDB（连接池使用率）'].values
        
        if len(X) > 1:
            # 训练线性回归模型
            self.model = LinearRegression()
            self.model.fit(X, y)
            
            # 预测不同QPS下的使用率
            qps_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
            predicted_usage = self.model.predict(qps_range)
            
            relationship = {
                'coefficient': self.model.coef_[0],
                'intercept': self.model.intercept_,
                'r_squared': self.model.score(X, y),
                'qps_range': qps_range.flatten(),
                'predicted_usage': predicted_usage
            }
        else:
            relationship = {'error': '数据不足建立关系模型'}
        
        return relationship
    
    def _generate_recommendations(self, basic_stats, bottlenecks, relationship_model):
        """生成配置建议"""
        recommendations = {}
        
        # 当前容量评估
        current_assessment = self._assess_current_capacity(bottlenecks)
        recommendations['current_assessment'] = current_assessment
        
        # 基于峰值QPS的容量建议
        peak_qps_recommendation = self._calculate_peak_qps_recommendation(
            basic_stats, relationship_model
        )
        recommendations['peak_qps_recommendation'] = peak_qps_recommendation
        
        # 基于平均负载的容量建议
        avg_load_recommendation = self._calculate_avg_load_recommendation(
            basic_stats, relationship_model
        )
        recommendations['avg_load_recommendation'] = avg_load_recommendation
        
        # 动态调整策略
        recommendations['dynamic_adjustment'] = self._suggest_dynamic_adjustment(basic_stats)
        
        return recommendations
    
    def _assess_current_capacity(self, bottlenecks):
        """评估当前容量是否足够"""
        assessment = {}
        
        if bottlenecks['critical_ratio'] > 0.01:  # 超过1%的时间出现严重瓶颈
            assessment['status'] = '严重不足'
            assessment['reason'] = f"系统在{bottlenecks['critical_ratio']*100:.2f}%的时间达到容量极限并出现排队"
        elif bottlenecks['high_usage_ratio'] > 0.05:  # 超过5%的时间使用率100%
            assessment['status'] = '不足'
            assessment['reason'] = f"系统在{bottlenecks['high_usage_ratio']*100:.2f}%的时间达到最大使用率"
        elif bottlenecks['queue_ratio'] > 0.02:  # 超过2%的时间出现排队
            assessment['status'] = '紧张'
            assessment['reason'] = f"系统在{bottlenecks['queue_ratio']*100:.2f}%的时间出现连接排队"
        else:
            assessment['status'] = '充足'
            assessment['reason'] = '当前连接池容量能够满足业务需求'
        
        return assessment
    
    def _calculate_peak_qps_recommendation(self, basic_stats, relationship_model):
        """基于峰值QPS计算容量建议"""
        peak_qps = basic_stats['qps_stats']['p99']  # 使用P99 QPS作为峰值
        
        if 'coefficient' in relationship_model:
            # 基于线性模型计算所需容量
            expected_usage = relationship_model['coefficient'] * peak_qps + relationship_model['intercept']
            required_capacity_factor = expected_usage / (self.max_usage_threshold * 100)
            required_capacity_factor *= (1 + self.safety_margin)  # 添加安全边际
            
            recommendation = {
                'based_on': '峰值QPS(P99)',
                'peak_qps': peak_qps,
                'expected_usage': expected_usage,
                'recommended_capacity_factor': max(required_capacity_factor, 1.0),
                'explanation': f'基于P99 QPS {peak_qps:.1f}，建议连接池容量调整为当前的{max(required_capacity_factor, 1.0):.2f}倍'
            }
        else:
            recommendation = {
                'based_on': '峰值QPS(P99)',
                'peak_qps': peak_qps,
                'recommended_capacity_factor': 1.5,  # 默认建议
                'explanation': f'基于P99 QPS {peak_qps:.1f}，建议连接池容量调整为当前的1.5倍（使用保守估计）'
            }
        
        return recommendation
    
    def _calculate_avg_load_recommendation(self, basic_stats, relationship_model):
        """基于平均负载计算容量建议"""
        avg_qps = basic_stats['qps_stats']['mean']
        
        if 'coefficient' in relationship_model:
            expected_usage = relationship_model['coefficient'] * avg_qps + relationship_model['intercept']
            required_capacity_factor = expected_usage / (self.max_usage_threshold * 100)
            
            recommendation = {
                'based_on': '平均QPS',
                'avg_qps': avg_qps,
                'expected_usage': expected_usage,
                'recommended_capacity_factor': max(required_capacity_factor, 1.0),
                'explanation': f'基于平均QPS {avg_qps:.1f}，建议连接池容量调整为当前的{max(required_capacity_factor, 1.0):.2f}倍'
            }
        else:
            recommendation = {
                'based_on': '平均QPS',
                'avg_qps': avg_qps,
                'recommended_capacity_factor': 1.0,
                'explanation': '基于平均负载，当前连接池容量基本合适'
            }
        
        return recommendation
    
    def _suggest_dynamic_adjustment(self, basic_stats):
        """建议动态调整策略"""
        qps_variance = basic_stats['qps_stats']['max'] / basic_stats['qps_stats']['mean']
        
        if qps_variance > 5:
            strategy = "高波动负载"
            suggestion = "建议实现连接池动态扩缩容，根据QPS变化自动调整池大小"
        elif qps_variance > 2:
            strategy = "中等波动负载"
            suggestion = "建议设置不同时段的固定连接池大小，或实现基础的动态调整"
        else:
            strategy = "稳定负载"
            suggestion = "固定连接池大小即可满足需求"
        
        return {
            'load_pattern': strategy,
            'qps_variance_ratio': qps_variance,
            'suggestion': suggestion
        }

def generate_report(analysis_results):
    """生成分析报告"""
    report = []
    report.append("=" * 60)
    report.append("连接池容量分析报告")
    report.append("=" * 60)
    
    # 当前状态评估
    assessment = analysis_results['recommendations']['current_assessment']
    report.append(f"\n1. 当前容量状态: {assessment['status']}")
    report.append(f"   原因: {assessment['reason']}")
    
    # 瓶颈分析
    bottlenecks = analysis_results['bottleneck_analysis']
    report.append(f"\n2. 瓶颈分析:")
    report.append(f"   高使用率时段占比: {bottlenecks['high_usage_ratio']*100:.2f}%")
    report.append(f"   排队时段占比: {bottlenecks['queue_ratio']*100:.2f}%")
    report.append(f"   严重瓶颈时段占比: {bottlenecks['critical_ratio']*100:.2f}%")
    
    # 容量建议
    recommendations = analysis_results['recommendations']
    report.append(f"\n3. 容量配置建议:")
    
    peak_rec = recommendations['peak_qps_recommendation']
    report.append(f"   - {peak_rec['based_on']}:")
    report.append(f"     建议调整倍数: {peak_rec['recommended_capacity_factor']:.2f}")
    report.append(f"     {peak_rec['explanation']}")
    
    avg_rec = recommendations['avg_load_recommendation']
    report.append(f"   - {avg_rec['based_on']}:")
    report.append(f"     建议调整倍数: {avg_rec['recommended_capacity_factor']:.2f}")
    report.append(f"     {avg_rec['explanation']}")
    
    # 动态调整建议
    dynamic = recommendations['dynamic_adjustment']
    report.append(f"\n4. 动态调整建议:")
    report.append(f"   负载模式: {dynamic['load_pattern']}")
    report.append(f"   QPS波动率: {dynamic['qps_variance_ratio']:.2f}")
    report.append(f"   建议: {dynamic['suggestion']}")
    
    # 关键指标
    stats = analysis_results['basic_stats']
    report.append(f"\n5. 关键性能指标:")
    report.append(f"   QPS - 平均: {stats['qps_stats']['mean']:.1f}, 峰值: {stats['qps_stats']['max']:.1f}")
    report.append(f"   P95: {stats['qps_stats']['p95']:.1f}, P99: {stats['qps_stats']['p99']:.1f}")
    report.append(f"   使用率 - 平均: {stats['usage_stats']['mean']:.1f}%, 峰值: {stats['usage_stats']['max']:.1f}%")
    report.append(f"   最大排队数: {stats['queue_stats']['max_queue']}")
    
    return "\n".join(report)

# 使用示例
if __name__ == "__main__":
    # 读取数据
    df = pd.read_csv('QPS&PoolUsage.csv')
    
    # 创建分析器
    analyzer = ConnectionPoolAnalyzer(safety_margin=0.2, max_usage_threshold=0.8)
    
    # 进行分析
    results = analyzer.analyze_pool_capacity(df)
    
    # 生成报告
    report = generate_report(results)
    print(report)