from lxml import etree                       #lxml是一个解析模块
if __name__ == "__main__":
    # 实例化一个etree对象，且解析了文件网页源码到该etree对象
    tree = etree.parse('./Demotmp/test.html')
    # r = tree.xpath('/html/body/div')                          #/  :表示从根节点进行定位，表示一个层级
    # r = tree.xpath('/html//div')                              #// :表示多个层级
    # r = tree.xpath('//div')                                   #// :表示从任意位置多个层级
    # r = tree.xpath('//div[@class="song"]')                    #[@]:表示属性定位
    # r = tree.xpath('//div[@class="song"]/p[3]')               #索引定位:表示索引定位，是从1开始的
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0] #取文本:/text()获取文本数据
    # r = tree.xpath('//li[7]//text()')                         #层级取文本://text()获取文本数据，非直系
    r = tree.xpath('//div[@class="song"]/img/@src')             #获取属性：获取标签内的属性的值
    print(r)
