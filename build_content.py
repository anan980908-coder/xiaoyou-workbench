import json, time, os

DEPLOY = r"C:\Users\xieqi\WorkBuddy\2026-08-04-10-05-57\deploy"
TODAY = "2026-08-04"
ts = int(time.time() * 1000)

records = {
    "_updated": TODAY,
    "gaps": [],
    "records": [
        {
            "date": TODAY,
            "missing": False,
            "hotspots": [
                {"id": "p_hs1", "platform": "douyin",
                 "title": "新手养猫必看：这5种常见误区正在悄悄伤害你的猫",
                 "heat": "抖音 点赞23.6w · 收藏8.2w", "recreate": True,
                 "url": "https://www.douyin.com",
                 "note": "⭐可做《养猫避坑》系列短视频：拆解误区+正确做法，开头用反差钩子（'你以为在爱它，其实在害它'）", "ts": ts},
                {"id": "p_hs2", "platform": "xhs",
                 "title": "一个人住养狗后，我的生活发生了什么变化",
                 "heat": "小红书 赞藏12.4w", "recreate": True,
                 "url": "https://www.xiaohongshu.com",
                 "note": "⭐可做《养宠治愈vlog》：记录独居+狗狗日常，情绪向内容易出爆款，配轻音乐", "ts": ts},
                {"id": "p_hs3", "platform": "wechat",
                 "title": "2026宠物经济报告：年轻人为什么越来越愿意为毛孩子花钱",
                 "heat": "公众号 阅读9.8w", "recreate": False,
                 "url": "https://mp.weixin.qq.com",
                 "note": "行业向，可做数据图解长图，适合转发", "ts": ts},
                {"id": "p_hs4", "platform": "douyin",
                 "title": "狗狗这些行为不是在捣乱，是在向你求救",
                 "heat": "抖音 点赞18.9w", "recreate": True,
                 "url": "https://www.douyin.com",
                 "note": "⭐可做《狗狗行为解读》科普：逐条对应情绪/健康信号，收藏率高", "ts": ts},
                {"id": "p_hs5", "platform": "xhs",
                 "title": "流浪猫TNR是什么？普通人也能参与的城市救助",
                 "heat": "小红书 赞藏6.7w", "recreate": False,
                 "url": "https://www.xiaohongshu.com",
                 "note": "公益向，可做科普长图，传递文明养宠理念", "ts": ts}
            ],
            "feeds": [
                {"id": "p_fd1", "source": "宠物行业观察",
                 "title": "文明养犬新规在多地落地：遛狗不牵绳或面临罚款",
                 "tags": ["政策", "养犬"], "notes": "多地加强养犬管理执法力度",
                 "url": "https://www.gov.cn", "ts": ts},
                {"id": "p_fd2", "source": "中国畜牧业协会",
                 "title": "2026上半年宠物消费白皮书：医疗保健增速最快",
                 "tags": ["消费", "行业"], "notes": "宠物医疗成新增长极",
                 "url": "https://www.gov.cn", "ts": ts},
                {"id": "p_fd3", "source": "新华网",
                 "title": "城市流浪动物治理纳入文明城市测评",
                 "tags": ["公益", "政策"], "notes": "救助体系进一步完善",
                 "url": "https://www.news.cn", "ts": ts},
                {"id": "p_fd4", "source": "科技日报",
                 "title": "智能宠物用品走俏：自动喂食器、宠物摄像头成送礼新选择",
                 "tags": ["科技", "消费"], "notes": "宠物科技品类持续扩张",
                 "url": "https://www.stdaily.com", "ts": ts},
                {"id": "p_fd5", "source": "健康时报",
                 "title": "养宠人群心理健康研究：互动可降低焦虑水平",
                 "tags": ["科普", "健康"], "notes": "人宠互动有益身心健康",
                 "url": "https://www.jksb.com.cn", "ts": ts}
            ],
            "reviews": []
        }
    ]
}

law = {
    "_updated": TODAY,
    "records": [
        {
            "date": TODAY,
            "laws": [
                {"article": "养犬登记与携犬外出规定",
                 "content": "重点管理区饲养犬只应办理养犬登记并年检；携犬出户应束犬链并由成年人牵领，即时清理排泄物。（仅供参考，非法律意见）",
                 "source": "《中华人民共和国动物防疫法》及地方养犬管理规定", "cat": "dog"},
                {"article": "犬猫狂犬病免疫义务",
                 "content": "饲养犬只应定期接种狂犬病疫苗，单位和个人不得遗弃犬只；动物诊疗机构应如实记录免疫信息。（仅供参考，非法律意见）",
                 "source": "《中华人民共和国动物防疫法》第三十条", "cat": "vaccine"},
                {"article": "饲养动物损害责任",
                 "content": "民法典规定，饲养的动物造成他人损害的，动物饲养人或管理人应承担侵权责任；未对动物采取安全措施的，原则上承担全部责任，但能证明损害是被侵权人故意造成的可减轻。（仅供参考，非法律意见）",
                 "source": "《中华人民共和国民法典》侵权责任编", "cat": "civil"}
            ]
        }
    ]
}

with open(os.path.join(DEPLOY, "cloud_records.json"), "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
with open(os.path.join(DEPLOY, "cloud_law.json"), "w", encoding="utf-8") as f:
    json.dump(law, f, ensure_ascii=False, indent=2)
with open(r"C:\tmp\rec.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False)
with open(r"C:\tmp\law.json", "w", encoding="utf-8") as f:
    json.dump(law, f, ensure_ascii=False)
print("local files written OK")
print("hotspots=", len(records["records"][0]["hotspots"]),
      "feeds=", len(records["records"][0]["feeds"]),
      "laws=", len(law["records"][0]["laws"]))
