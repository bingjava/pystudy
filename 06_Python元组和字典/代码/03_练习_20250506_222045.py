
# 练习: 下面是斗鱼的接口数据，请得到每个主播的名字nn和图像rs1
douyu = {
    "code": 0,
    "msg": "success",
    "data": {
        "ct": {
            "iv": 1,
            "ivcv": 1,
            "tag": 0,
            "tn": "",
            "vmcrr": 0,
            "vmcm": ""
        },
        "rl": [
            {
                "rid": 3853457,
                "rn": "承蒙厚爱我是小爵啊",
                "uid": 180315123,
                "nn": "一条小爵不可爱茶miya",
                "rs1": "https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/14/3853457_20190814094651_big.jpg/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/14/3853457_20190814094651_small.jpg/dy1",
            },
            {
                "rid": 533813,
                "rn": "粉丝牌",
                "uid": 36922190,
                "nn": "TD丶正直博",
                "rs1": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_small.png/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_big.png/dy1",
            },
            {
                "rid": 533813,
                "rn": "感谢翘哥",
                "uid": 36922190,
                "nn": "TD丶正直博",
                "rs1": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_small.png/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_big.png/dy1",
            },
            {
                "rid": 533813,
                "rn": "翘哥三十",
                "uid": 36922190,
                "nn": "TD丶正直博",
                "rs1": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_small.png/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_big.png/dy1",
            },
        ],
        "pgcnt": 6
    }
}

rl_list = douyu['data']['rl']
# print(rl_list)
for rl in rl_list:
    nn = rl['nn']  # 昵称
    rs1 = rl['rs1']  # 图片url
    print(nn, rs1)

