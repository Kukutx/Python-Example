import requests
import json
# 获取豆瓣电影数据
if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': ' ',
        'start': '0',          # 从库里开始取出，以及次数
        'limit': '20',         # 一次能获取的电影个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    fp = open('./requestsDemotmp/demo4.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False, indent=4, separators=(',', ': '))
    fp.close()
    print('爬取数据结束')
