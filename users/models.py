# coding; utf-8
from hashlib import sha1
from django.db import models
from db.BaseModels import BaseModel

# Create your models here.

# 定义一个对密码加密的hash函数
def get_hash(str):
    '''取一个字符串的hash值'''
    sh = sha1()
    sh.update(str.encode('utf-8'))

    return sh.hexdigest()


# 用户管理器 ：添加和查找功能
class UsersManager(models.Manager):

    def add_one_user(self, username, password, email):
        '''添加一个账户'''
        user = self.create(username=username,
                           password=get_hash(password),
                           email=email)

        return user
    def get_user(self, username, password):
        '''根据用户密码查询'''
        try:
            user_message = self.get(username=username, password=get_hash(password))

        except self.model.DoesNotExist:
            user_message = None

        return user_message


    def get_user_username(self, username):
        '''根据用户名查找账户信息'''
        try:
            user = self.get(username=username)

        except self.model.DoesNotExist:
            # 账户不存在
            user = None

        return user

    def get_user_password(self, password):
        '''密码验证'''
        try:
            password = self.get(password=get_hash(password))

        except self.model.DoesNotExist:
            # 密码不存在
            password = None

        return password


# 设计用户表
class UserSheet(BaseModel):
    '''用户模型类'''
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    is_active = models.BooleanField(default=False ,verbose_name='激活状态')

    # 用户表管理器
    objects = UsersManager()

    class Meta:
        # 数据库表名
        db_table = 's_user_message'





