# _*_ coding:utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.utils.safestring import mark_safe
import django.utils.timezone as timezone
from django.db import models
import os

#机器人表
class Bot(models.Model):
    bot_name =models.CharField(max_length=100, verbose_name=u'机器人名称')
    ip =models.CharField(max_length=100, verbose_name=u'服务器IP')
    status =models.CharField(max_length=100, verbose_name=u'在线状态')
    action =models.CharField(max_length=100, verbose_name=u'操作',choices = [['1',u'登录'],['0',u'退出']], default = '0')
    account = models.CharField(max_length=100, verbose_name=u'服务器帐号')
    password = models.CharField(max_length=100, verbose_name=u'服务器密码')
    login_time=models.CharField(max_length=100, verbose_name=u'登录时间')
    login_qr=models.ImageField(upload_to='Robot/qr/',verbose_name=u'登录二维码',default='')

    def showText(self):
         # os.system('workon haoyidai')
         # os.system('python Bot/demo.py')
         return mark_safe('<a href="http://localhost:8000/start">显示二维码</a>')
    showText.short_description = u"二维码"

    class Meta:
        verbose_name = u'机器人管理'
        verbose_name_plural = verbose_name


#日志表
class Log(models.Model):
    bot_name =models.CharField(max_length=100, verbose_name=u'机器人名称')
    ip =models.CharField(max_length=100, verbose_name=u'服务器IP')
    log_level =models.CharField(max_length=100, verbose_name=u'日志等级')
    log_msg =models.CharField(max_length=500, verbose_name=u'日志消息')
    create_time=models.DateTimeField(default=timezone.now, verbose_name=u'产生时间') #日期

    class Meta:
        verbose_name = u'日志管理'
        verbose_name_plural = verbose_name




#订单表
class Order(models.Model):
    pay_order =models.CharField(max_length=100, verbose_name=u'订单号')
    referee =models.CharField(max_length=100, verbose_name=u'推荐人')

    class Meta:
        verbose_name = u'订单管理'
        verbose_name_plural = verbose_name



#饿了么用户
class RedUser(models.Model):
    phone = models.CharField(max_length=100, verbose_name=u'电话号码')
    counter = models.IntegerField(verbose_name=u'次数')

    class Meta:
        verbose_name = u'饿了么用户'
        verbose_name_plural = verbose_name


#公众号文章监控
class Article(models.Model):
    article_name = models.CharField(max_length=200, verbose_name=u'公众号名称')
    article_title = models.CharField(max_length=200, verbose_name=u'文章标题')
    article_url = models.CharField(max_length=200, verbose_name=u'文章地址')
    read = models.IntegerField( verbose_name=u'阅读次数')
    like = models.IntegerField( verbose_name=u'点赞量')
    last_edit_time=models.CharField(max_length=100, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'公众号文章监控'
        verbose_name_plural = verbose_name

#微信群监控
class Group(models.Model):
    group_id = models.CharField(max_length=200, verbose_name=u'微信群ID')
    group_name = models.CharField(max_length=200, verbose_name=u'微信群名称')
    number = models.IntegerField( verbose_name=u'微信群人数')

    class Meta:
        verbose_name = u'微信群监控'
        verbose_name_plural = verbose_name

#微信群消息监控
class GroupMsg(models.Model):
    group_id = models.CharField(max_length=200, verbose_name=u'微信群ID')
    member = models.CharField(max_length=200, verbose_name=u'微信群名称')
    text = models.CharField(max_length=10000, verbose_name=u'微信群消息')  #Base64编码保存  显示的时候需要用Base64解码
    picture= models.ImageField(upload_to='Group/img/', verbose_name=u'微信群图片')  # 图片  upload_to 路径
    recording= models.CharField( max_length=200,verbose_name=u'录音文件')
    duration= models.IntegerField( verbose_name=u'录音时长')
    create_time= models.CharField(max_length=200, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'微信群消息监控'
        verbose_name_plural = verbose_name

#推送消息
class PushMsg(models.Model):
    content = models.CharField(max_length=600, verbose_name=u'推送消息')

    class Meta:
        verbose_name = u'推送消息'
        verbose_name_plural = verbose_name









