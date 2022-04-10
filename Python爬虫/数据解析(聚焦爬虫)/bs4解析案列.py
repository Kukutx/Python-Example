import requests
from bs4 import BeautifulSoup
# 爬取三国演义小说所有章节
if __name__ == "__main__":
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).content       #linux 写text/本应该写text的因为字符集问题所以写content
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节标题
    li_list = soup.select('.book-mulu >ul > li')
    fp = open('./Demotmp/demo1.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).content    #linux 写text
        # 解析详情页相关章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节的内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title,"爬取成功。")

