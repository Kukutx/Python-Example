import requests
import json
# 获取化妆品生产许可信息管理系统服务平台信息
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    id_list=[]                         #存储企业id
    all_data_list=[]                   #存储企业详情数据
    # 批量获取不同企业的id
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    # 定义参数的页数
    for page in range(1,6):
        page=str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        joson_ids = requests.post(url=url, data=data, headers=headers).json()
        for dict in joson_ids['list']:
            id_list.append(dict['ID'])
    #获取企业的详情数据
    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        all_data_list.append(detail_json)
    fp = open('./requestsDemotmp/demo6.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False,indent=4, separators=(',', ': '))
    fp.close()
    print('爬取数据结束')
