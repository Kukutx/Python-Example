# [paramiko模块使用](https://www.cnblogs.com/zhujingzhi/p/9686208.html)

**目录**

- [一、paramiko 安装](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label0)
- 二、什么是paramiko
  - [2.1：paramiko包括两个核心的组件](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label1_0)
  - [2.2：paramiko有几个基础的名词](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label1_1)
- 三、SSHClient使用
  - [3.1：常用方法](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label2_0)
  - [3.2：使用密码连接(一)](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label2_1)
  - [3.3：使用密码连接(二)transport封装推荐使用](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label2_2)
  - [3.4：使用秘钥连接(一)](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label2_3)
  - [3.5：使用秘钥连接(二)transport封装推荐使用](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label2_4)
- 四、SFTPClient使用
  - [4.1：常用方法](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label3_0)
  - [4.2：上传功能](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label3_1)
  - [4.3：下载功能](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label3_2)
- 五、综合函数实现(复制粘贴即可使用)
  - [ 5.1：transport封装函数(推荐使用)](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label4_0)
  - [5.1：普通方式](https://www.cnblogs.com/zhujingzhi/p/9686208.html#_label4_1)

 

------

## 一、paramiko 安装

　　paramiko是Python的一个第三方库，所以我们要使用pip安装

```
pip install paramiko
```

## 二、什么是paramiko

　　SSH是一个协议，paramiko是使用SSHv2协议(底层使用的是cryptography)的一个第三方的库

#### 2.1：paramiko包括两个核心的组件

　　SSHClient：它的作用类似于Linux的SSH命令，是对SSH会话的一个类的封装，这个类封装了传输(Transport),通道(Channel)及SFTPClient建立的方法(open_sftp),通过用于执行远程命令。

　　SFTPClient：它的作用类似Linux的SFTP命令，是对SFTP客户端的一个类的封装。主要是实现对远程文件的操作，上传，下载，修改文件权限等操作。

#### 2.2：paramiko有几个基础的名词

- 　　Transport：是一种加密的会话，使用时会同步创建一个加密的Tunnels(通道)，这个Tunnels叫Channel
- 　　Channel：是一种类的Socket，一种安全的SSH通道
- 　　Session：是client和server保持连接的对象。实现方式是connect ---> start_client ---> start_server 开始会话。

## 三、SSHClient使用

#### 3.1：常用方法

```
connect()方法：
实现远程服务器的连接认证，对于该方法自由一个hostname是必须传的参数
常用参数：
hostname：连接的目标主机
port：目标主机的端口
username：验证的用户可以为None
password：验证的密码可以为None
pkey：私钥的验证方式可以为None
key_filename：一个文件名或者一个文件列表，指定私钥文件
timeout：TCP连接的超时时间，可以为None
allow_agent：是否允许连接到ssh代理，默认为True
look_for_keys：是否在~/.ssh中搜索秘钥文件，默认为True
compress：是否打开压缩，默认False
 
set_missing_host_key_policy()方法：
设置远程服务器没有在know_hosts文件中记录时的应对策略，目前支持三种策略
AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项
 
exec_command()方法：
在远程服务器执行Linux命令的方法
 
open_sftp()方法：
在当前ssh会话的基础上建立一个sftp会话，该方法会返回一个SFTPClient对象
通过这个对象可以实现上传下载的功能
```

#### 3.2：使用密码连接(一)

```python
import paramiko
# 实例化SSHClient
client = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing.host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务器，用户名密码认证
client.connect(hostname='192.168.163.129',port=22,username='root',password='zhujingzhi')
# 打开一个Chanent并执行命令
stdin,stdout,stderr = client.exec_command('df -h')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
# 打印结果
print(stdout.read().decode('utf8'))
# 关闭连接
client.close()
```

#### 3.3：使用密码连接(二)transport封装推荐使用

```python
import paramiko
# 创建一个通道
transport = paramiko.transport(('192.168.163.129', 22))
transport.connect(username='root', password='zhujingzhi')
# 实例化SSHClient
client = paramiko.SSHClient()
client._transport = transport
# 打开一个Chanent并执行命令
stdin,stdout,stderr = client.exec_command('df -h')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
# 打印结果
print(stdout.read().decode('utf8'))
# 关闭连接
transport.close()
```

#### 3.4：使用秘钥连接(一)

```python
import paramiko
 
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/zjz/.ssh/id_rsa')
  
#实例化SSHClient
client = paramiko.SSHClient()
  
#自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
#连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='192.168.163.129',port=22,username='root',pkey=private)
 
# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
  
# 打印执行结果
print(stdout.read().decode('utf-8'))
  
# 关闭SSHClient
client.close()
```

#### 3.5：使用秘钥连接(二)transport封装推荐使用

```python
import paramiko
 
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/zjz/.ssh/id_rsa')
  
# 创建一个通道
transport = paramiko.Transport(('192.168.163.129', 22))
transport.connect(username='root', pkey=private_key)
 
#实例化SSHClient
client = paramiko.SSHClient()
client._transport = transport
  
# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
  
# 打印执行结果
print(stdout.read().decode('utf-8'))
  
# 关闭SSHClient
transport.close()
```

## 四、SFTPClient使用

#### 4.1：常用方法

```
SFTPCLient作为一个sftp的客户端对象，根据ssh传输协议的sftp会话，实现远程文件操作，如上传、下载、权限、状态
  
from_transport(cls,t) 创建一个已连通的SFTP客户端通道
put(localpath, remotepath, callback=None, confirm=True) 将本地文件上传到服务器 参数confirm：是否调用stat()方法检查文件状态，返回ls -l的结果
get(remotepath, localpath, callback=None) 从服务器下载文件到本地
mkdir() 在服务器上创建目录
remove() 在服务器上删除目录
rename() 在服务器上重命名目录
stat() 查看服务器文件状态
listdir() 列出服务器目录下的文件
```

#### 4.2：上传功能

```python
import paramiko
  
# 获取Transport实例
tran = paramiko.Transport(('192.168.163.129', 22))
  
# 连接SSH服务端，使用password
tran.connect(username="root", password='zhujingzhi')
# 或使用
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/zjz/.ssh/id_rsa')
# 连接SSH服务端，使用pkey指定私钥
tran.connect(username="root", pkey=private)
  
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
  
# 设置上传的本地/远程文件路径
localpath = "/Users/zjz/Downloads/1.txt"
remotepath = "/tmp/1.txt"
  
# 执行上传动作
sftp.put(localpath, remotepath)
  
# 关闭连接
tran.close()
```

#### 4.3：下载功能

```python
import paramiko
  
# 获取Transport实例
tran = paramiko.Transport(('192.168.163.129', 22))
  
# 连接SSH服务端，使用password
tran.connect(username="root", password='zhujingzhi')
# 或使用
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/zjz/.ssh/id_rsa')
# 连接SSH服务端，使用pkey指定私钥
tran.connect(username="root", pkey=private)
  
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
  
# 设置上传的本地/远程文件路径
localpath = "/Users/zjz/Downloads/1.txt"
remotepath = "/tmp/1.txt"
  
# 执行下载动作
sftp.get(remotepath, localpath)
  
# 关闭连接
tran.close()　
```

## 五、综合函数实现(复制粘贴即可使用)

####  5.1：transport封装函数(推荐使用)

```python
import paramiko
 
class ssh(object):
    def __init__(self,hostdata):
        """
        初始化连接信息和ftp方法
        :param hostdata: 连接信息字段
        """
        self.ip = hostdata['ip']
        self.port = hostdata['port']
        self.user = hostdata['user']
        self.passwd = hostdata['passwd']
        self.transport = paramiko.Transport((self.ip, self.port))
        self.transport.connect (username=self.user, password=self.passwd)
        self.obj = paramiko.SSHClient()
        self.obj._transport = self.transport
        self.objsftp = self.obj.open_sftp ()
 
    def run_cmd(self, cmd):
        """
        执行命令方法
        :param cmd: 需要执行的命令
        :return:
        """
        stdin, stdout, stderr = self.obj.exec_command (cmd)
        return stdout.read ()
 
    def run_cmdlist(self, cmdlist):
        """
        执行命令方法列表
        :param cmdlist: 命令列表
        :return:
        """
        self.resultList = []
        for cmd in cmdlist:
            stdin, stdout, stderr = self.obj.exec_command (cmd)
            self.resultList.append (stdout.read ())
        return self.resultList
 
    def get(self,remotepath,localpath):
        """
        下载文件方法(两个路径都要指定文件名)
        :param remotepath: 服务器路径
        :param localpath:  本地路径
        :return:
        """
        self.objsftp.get(remotepath,localpath)
 
    def put(self,localpath,remotepath):
        """
        上传文件方法(两个路径都要指定文件名)
        :param localpath: 本地路径
        :param remotepath: 服务器路径
        :return:
        """
        self.objsftp.put(localpath,remotepath)
 
    def close(self):
        """
        关闭方法
        :return:
        """
        self.objsftp.close ()
        self.transport.close ()
 
# 函数的使用
if __name__ == '__main__':
    hostdata = {
        'ip':'192.168.163.129',
        'port':22,
        'user':'root',
        'passwd':'zhujingzhi',
    }
    host = ssh (hostdata)                                      # 实例化远程函数给数据库里面的IP 端口 用户名 密码信息
    v = host.run_cmd ('df -h')                                 # 执行单个命令
    vstr = v.decode (encoding='utf-8', errors='strict')        # bytes转字符串
    v1 = host.run_cmdlist (['ls', 'df'])                       # 执行命令列表
    print(hostdata['ip'])
    print(vstr)
    v = host.get('/root/anaconda-ks.cfg','D:\\采集\\a.cfg')     # 下载文件
    v = host.put('D:\\采集\\a.cfg','/opt/a.cfg')                # 上传文件
    host.close()　
```

#### 5.1：普通方式

```python
import paramiko
 
class ssh(object):
    def __init__(self,hostdata):
        """
        初始化连接信息和ftp方法
        :param hostdata: 连接信息字段
        """
        self.ip = hostdata['ip']
        self.port = hostdata['port']
        self.user = hostdata['user']
        self.passwd = hostdata['passwd']
        self.obj = paramiko.SSHClient()
        self.obj.set_missing_host_key_policy(paramiko.AutoAddPolicy ())
        self.obj.connect (self.ip, self.port, self.user, self.passwd)
        self.objsftp = self.obj.open_sftp ()
 
    def run_cmd(self, cmd):
        """
        执行命令方法
        :param cmd: 需要执行的命令
        :return:
        """
        stdin, stdout, stderr = self.obj.exec_command (cmd)
        return stdout.read ()
 
    def run_cmdlist(self, cmdlist):
        """
        执行命令方法列表
        :param cmdlist: 命令列表
        :return:
        """
        self.resultList = []
        for cmd in cmdlist:
            stdin, stdout, stderr = self.obj.exec_command (cmd)
            self.resultList.append (stdout.read ())
        return self.resultList
 
    def get(self,remotepath,localpath):
        """
        下载文件方法(两个路径都要指定文件名)
        :param remotepath: 服务器路径
        :param localpath:  本地路径
        :return:
        """
        self.objsftp.get(remotepath,localpath)
 
    def put(self,localpath,remotepath):
        """
        上传文件方法(两个路径都要指定文件名)
        :param localpath: 本地路径
        :param remotepath: 服务器路径
        :return:
        """
        self.objsftp.put(localpath,remotepath)
 
    def close(self):
        """
        关闭方法
        :return:
        """
        self.objsftp.close ()
        self.obj.close ()
 
# 函数的使用
if __name__ == '__main__':
    hostdata = {
        'ip':'192.168.163.129',
        'port':22,
        'user':'root',
        'passwd':'zhujingzhi',
    }
    host = ssh (hostdata)                                      # 实例化远程函数给数据库里面的IP 端口 用户名 密码信息
    v = host.run_cmd ('df -h')                                 # 执行单个命令
    vstr = v.decode (encoding='utf-8', errors='strict')        # bytes转字符串
    v1 = host.run_cmdlist (['ls', 'df'])                       # 执行命令列表
    print(hostdata['ip'])
    print(vstr)
    v = host.get('/root/anaconda-ks.cfg','D:\\采集\\a.cfg')     # 下载文件
    v = host.put('D:\\采集\\a.cfg','/opt/a.cfg')                # 上传文件
    host.close()
```