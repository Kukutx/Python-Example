
# SSHClient实现
# import paramiko
# # 实例化SSHClient
# client = paramiko.SSHClient()
# # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接SSH服务端，以用户名和密码进行认证
# client.connect(hostname='192.168.43.28', port=22,username='kukutx', password='65332120')
# # 打开一个Channel并执行命令
# stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
# # 打印执行结果
# print(stdout.read().decode('utf-8'))          # 以utf-8编码对结果进行解码)
# # 关闭SSHClient
# client.close()

# import paramiko
# import sys
# ssh_host = sys.argv[1]
# ssh_port = 22
# user = 'kukutx'
# password = '65332120'
# cmd = sys.argv[2]
# paramiko.util.log_to_file('./tmp/test.txt')  # 使用paramiko记录日志
# s = paramiko.SSHClient()  # 绑定一个实例
# s.load_system_host_keys()                              # 加载known_hosts文件
# s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 远程连接如果提示yes/no时，默认为yes
# s.connect(ssh_host, ssh_port, user, password, timeout=5)  # 连接远程主机
# # 执行指令，并将命令本身及命令的执行结果赋值到标准办入、标准输出或者标准错误
# stdin, stdout, stderr = s.exec_command(cmd)
# cmd_result = stdout.read(), stderr.read()  # 取得执行的输出
# for line in cmd_result:
#     print(line.decode('utf-8'))
# s.close()

# SFTPClient
import paramiko
tran = paramiko.Transport(('192.168.43.28', 22))     # 获取Transport传输实例
tran.connect(username="kukutx", password='65332120') # 连接SSH服务端
# # 或使用
# # 配置私人密钥文件位置
# private = paramiko.RSAKey.from_private_key_file( '/Users/root/.ssh/id_rsa')
# # 连接SSH服务端，使用pkey指定私钥
# tran.connect(username="root", pkey=private)
sftp = paramiko.SFTPClient.from_transport(tran)  # 获取SFTP客户端实例
# 设置上传的本地/远程文件路径
remotepath = "/home/kukutx/桌面/log.txt"     #远程文件路径
localpath = "./tmp/log.txt"                  #上传的本地文件
# sftp.put(localpath, remotepath) # 执行上传功能
sftp.get(remotepath, localpath)   # 执行下载功能
tran.close()   #关闭连接

# import os
# import sys
# import paramiko
# host = sys.argv[1]
# rfilename = sys.argv[2]
# lfilename = os.path.basename(rfilename)
# user = 'root'
# password = 'xxxx'
# paramiko.util.log_to_file('/tmp/test')
# t = paramiko.Transport((host,22))
# t.connect(username=user,password=password)
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.get(rfilename,lfilename)
# #sftp.put('paramiko1.py','/tmp/paramiko1.py')
# t.close()

# Paramiko的综合实例
# import uuid
# import paramiko
# class SSHConnection(object):

#     def __init__(self, host_dict):
#         self.host = host_dict['host']
#         self.port = host_dict['port']
#         self.username = host_dict['username']
#         self.pwd = host_dict['pwd']
#         self.__k = None
    
#     def create_file(self):
#         file_name = str(uuid.uuid4())
#         with open(file_name,'w') as f:
#             f.write('sb')
#         return file_name

#     def connect(self):
#         transport = paramiko.Transport((self.host, self.port))
#         transport.connect(username=self.username, password=self.pwd)
#         self.__transport = transport

#     def close(self):
#         self.__transport.close()
    
#     def run_cmd(self, command):
#         """
#         执行shell命令,返回字典
#         return {'color': 'red','res':error}或
#         return {'color': 'green', 'res':res}
#         :param command:
#         :return:
#         """
#         ssh = paramiko.SSHClient()
#         ssh._transport = self.__transport
#         # 执行命令
#         stdin, stdout, stderr = ssh.exec_command(command)
#         # 获取命令结果
#         res = self.to_str(stdout.read())
#         # 获取错误信息
#         error = self.to_str(stderr.read())
#         # 如果有错误信息，返回error
#         # 否则返回res
#         if error.strip():
#             return {'color': 'red', 'res': error}
#         else:
#             return {'color': 'green', 'res': res}

#     def upload(self, local_path, target_path):
#         # 连接，上传
#         # file_name = self.create_file()
#         sftp = paramiko.SFTPClient.from_transport(self.__transport)
#         # 将location.py 上传至服务器 /tmp/test.py
#         sftp.put(local_path, target_path, confirm=True)
#         # print(os.stat(local_path).st_mode)
#         # 增加权限
#         # sftp.chmod(target_path, os.stat(local_path).st_mode)
#         sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀

#     def download(self, target_path, local_path):
#         # 连接，下载
#         sftp = paramiko.SFTPClient.from_transport(self.__transport)
#         # 将location.py 下载至服务器 /tmp/test.py
#         sftp.get(target_path, local_path)

#     # 销毁
#     def __del__(self):
#         self.close()
    
#     def to_str(self,bytes_or_str):
#         """
#         把byte类型转换为str
#         :param bytes_or_str:
#         :return:
#         """
#         if isinstance(bytes_or_str, bytes):
#             value = bytes_or_str.decode('utf-8')
#         else:
#             value = bytes_or_str
#         return value


# dict = {'host': '192.168.43.28', 'port': 22, 'username': 'kukutx', 'pwd':'65332120'}
# test=SSHConnection(dict);
# test.connect();
# print(test.run_cmd('pwd'));
# test.close();


