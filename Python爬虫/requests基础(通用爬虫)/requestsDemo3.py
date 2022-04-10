import requests
import json
# 破解百度翻译
# 通过百度翻译的Ajax请求或许对应的json格式数据进行爬取   （可以查看 Network 的 XHR 实时数据）
if __name__ == "__main__":
    post_url = "https://fanyi.baidu.com/sug"  # ajax的请求文件
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    word=input('enter a word:')
    # post请求参数处理
    data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取json数据:json()返回的是obj
    dic_obj = response.json()
    # print(dic_obj)
    # 持久化存储
    fp = open('./requestsDemotmp/demo3.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False, indent=4, separators=(',', ': '))
    fp.close()
    print('爬取数据结束')
