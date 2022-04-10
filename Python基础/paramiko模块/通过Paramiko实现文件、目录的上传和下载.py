import os
import time
import paramiko
from stat import S_ISDIR
from common.utils import get_logger

logger = get_logger()

BUF_SIZE = 32 * 1024


class SSH(object):
    def __init__(self, asset, timeout=30):
        '''
        请将asset封装成一个namedtuple
        :param asset:
        :param timeout:
        '''
        self.ip = asset.ip
        self.username = asset.username
        self.password = asset.password
        self.timeout = timeout
        self.chan = ''
        self.sftp = ''
        # 如果只是做文件的上传和下载，ssh可以不需要
        self.ssh = paramiko.SSHClient()
        self.Transport = paramiko.Transport(sock=(self.ip, 22))

    # 连接远程主机
    def connect(self):
        logger.debug('Connecting to {}'.format(self.ip))
        self.Transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.Transport)
        # 如果只是做文件的上传和下载，ssh可以不需要
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, port=22, username=self.username,password=self.password, timeout=6)
        self.chan = self.ssh.invoke_shell(term='xterm')

    # 断开连接
    def close(self):
        logger.debug('Disconnecting to {}'.format(self.ip))
        self.Transport.close()
        self.chan.close()
        self.ssh.close()

    # 重启服务
    def service_restart(self, service_name):
        logger.debug('开始重启{}'.format(service_name))
        self.command('systemctl restart {}'.format(service_name))

    # 发送命令
    def command(self, cmd):
        self.chan.send('{}\n'.format(cmd))
        time.sleep(5)

    def get_msg(self):
        msg = self.chan.recv(BUF_SIZE)
        logger.debug(msg.decode('utf-8'))

    # 递归创建目录
    def mkdir(self, remote_dir):
        self.command('mkdir -p {}'.format(remote_dir))
        time.sleep(0.3)

    # 获取目录下所有的文件
    def __get_all_files_from_remote_dir(self, remote_dir):
        all_files = list()

        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = self.sftp.listdir_attr(remote_dir)
        for x in files:
            # remote_dir目录中每一个文件或目录的完整路径
            filename = remote_dir + '/' + x.filename
            # 如果是目录，则递归处理该目录
            if S_ISDIR(x.st_mode):
                all_files.extend(
                    self.__get_all_files_from_remote_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    # 获取本地指定目录下的所有文件
    def __get_all_files_from_local_dir(self, local_dir):
        # 保存所有文件的列表
        all_files = list()

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = os.listdir(local_dir)
        for x in files:
            # local_dir目录中每一个文件或目录的完整路径
            filename = os.path.join(local_dir, x)
            # 如果是目录，则递归处理该目录
            if os.path.isdir(filename):
                all_files.extend(self.__get_all_files_from_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    # get单个文件
    def get_file(self, remote_file, local_file):
        logger.debug('')
        # 获取remote_file的属性值
        r_file = self.sftp.lstat(remote_file)
        if S_ISDIR(r_file.st_mode):
            logger.debug('{} is a directory'.format(remote_file))
            return
        if os.path.isdir(local_file):
            filename = remote_file.split('/')[-1]
            local_file = os.path.join(local_file, filename)
        logger.debug('file {} is downloading...'.format(remote_file))
        self.sftp.get(remote_file, local_file)

    # put单个文件
    def put_file(self, local_file, remote_file):
        r_file = self.sftp.lstat(remote_file)
        if S_ISDIR(r_file.st_mode):
            filename = local_file.split('/')[-1]
            remote_file = os.path.join(remote_file, filename)

        if os.path.isdir(local_file):
            logger.debug('{} is a directory'.format(local_file))
            return
        logger.debug('file {} is uploading...'.format(local_file))
        self.sftp.put(local_file, remote_file)

    # get 目录
    def get_dir(self, remote_dir, local_dir):
        all_files = self.__get_all_files_from_remote_dir(remote_dir)
        for x in all_files:
            filename = x.split('/')[-1]
            r_d = os.path.dirname(x).split('/')
            base_d = remote_dir.split('/')
            l_d = os.path.join(
                local_dir, '/'.join(list(set(r_d) ^ set(base_d))))
            if not os.path.exists(l_d):
                os.mkdir(l_d)
            local_filename = os.path.join(l_d, filename)
            logger.debug('file {} is downloading...'.format(filename))
            self.sftp.get(x, local_filename)

    # put目录
    def put_dir(self, local_dir, remote_dir):
        # 去掉路径字符穿最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取本地指定目录及其子目录下的所有文件
        all_files = self.__get_all_files_from_local_dir(local_dir)
        # 依次put每一个文件
        for x in all_files:
            filename = os.path.split(x)[-1]
            if os.path.isdir(x):
                l_d = x.split('/')
            else:
                l_d = os.path.dirname(x).split('/')

            base_d = local_dir.split('/')
            r_dir = os.path.join(
                remote_dir, '/'.join(list(set(l_d) ^ set(base_d))))
            try:
                self.sftp.lstat(r_dir)
            except Exception as e:
                self.mkdir(r_dir)
            if os.path.isdir(x):
                continue
            remote_filename = os.path.join(r_dir, filename)
            logger.debug('file {} is uploading...'.format(x))
            self.sftp.put(x, remote_filename)
