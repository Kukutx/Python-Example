import requests
import json
# 获取肯德基查询数据
if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    kw = input('enter a word:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '99999'
    }
    response = requests.post(url=url, data=data, headers=headers)
    kcf_data = response.json()
    fp = open('./requestsDemotmp/demo5.json', 'w', encoding='utf-8')
    json.dump(kcf_data, fp=fp, ensure_ascii=False,indent=4, separators=(',', ': '))
    fp.close()
    print('爬取数据结束')
