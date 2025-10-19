
import json

# json: 一种表示数据的格式
# json的2种表现形式:
#    1.json字符串
#    2.json对象(Python字典)


# json解析(json反序列化): (重点)
#   字符串 => Python字典
s = '{"name": "邓超", "age": 40}'
d = json.loads(s)
print(d, type(d))  # {'name': '邓超', 'age': 40} <class 'dict'>

# json序列化:  (了解)
#    Python字典 => 字符串
s2 = json.dumps(d)
print(s2, type(s2))  # {"name": "\u9093\u8d85", "age": 40} <class 'str'>
