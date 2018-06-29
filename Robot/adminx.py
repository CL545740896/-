# _*_ coding:utf-8 _*_
__author__ = 'xxx'
__date__ = '2018/5/16 23:56'

import xadmin
from xadmin import views
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from django.utils.translation import ugettext as _
from .models import *


# 添加后台主题
class BaseSettings(object):
    enable_themes = True    #启用主题
    use_bootswatch = True   #boot主题

class GlobleSetting(object):
    site_title = u'微信机器人后台管理系统' #左上角
    site_footer = u'Power By Eric'            #底部
    menu_style = 'accordion'        #左部可折叠菜单


#机器人管理类
class BotAdmin(object):
    list_display = ['id','bot_name','ip','status','action','account','password','login_time','showText']
    search_fields =['id','bot_name','login_time','status','login_qr']
    list_filter = ['id','bot_name','login_time','status','login_qr']
    list_editable = ['id','bot_name','ip','status','action','account','password','login_time','login_qr']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class LogAdmin(object):
    list_display = ['id','bot_name','ip','log_level','log_msg','create_time']
    search_fields =['id','bot_name','ip','log_level','log_msg','create_time']
    list_filter = ['id','bot_name','ip','log_level','log_msg','create_time']
    list_editable = ['id','bot_name','ip','log_level','log_msg','create_time']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class OrderAdmin(object):
    list_display = ['id','pay_order','referee']
    search_fields =['id','pay_order','referee']
    list_filter = ['id','pay_order','referee']
    list_editable = ['id','pay_order','referee']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class RedUserAdmin(object):
    list_display = ['id','phone','counter']
    search_fields =['id','phone','counter']
    list_filter = ['id','phone','counter']
    list_editable = ['id','phone','counter']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class ArticleAdmin(object):
    list_display = ['id','article_name','article_title','article_url','read','like','last_edit_time']
    search_fields =['id','article_name','article_title','article_url','read','like','last_edit_time']
    list_filter = ['id','article_name','article_title','article_url','read','like','last_edit_time']
    list_editable = ['id','article_name','article_title','article_url','read','like','last_edit_time']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class GroupAdmin(object):
    list_display = ['id','group_id','group_name','number']
    search_fields =['id','group_id','group_name','number']
    list_filter = ['id','group_id','group_name','number']
    list_editable =['id','group_id','group_name','number']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class GroupMsgAdmin(object):
    list_display = ['id','group_id','member','text','picture','recording','duration','create_time']
    search_fields =['id','group_id','member','text','picture','recording','duration','create_time']
    list_filter = ['id','group_id','member','text','picture','recording','duration','create_time']
    list_editable = ['id','group_id','member','text','picture','recording','duration','create_time']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

class PushMsgAdmin(object):
    list_display = ['id','content']
    search_fields = ['id','content']
    list_filter =  ['id','content']
    list_editable =  ['id','content']
    # show_detail_fields = ['title'] # 需要省略显示的内容
    model_icon = 'fa fa-newspaper-o'
    # style_fields = {'content':'ueditor'}
    refresh_times = [1, 3, 5, 10, 60]
    list_per_page = 15
    ordering = ['id']
    pass

xadmin.site.register(Bot, BotAdmin)
xadmin.site.register(PushMsg, PushMsgAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Group, GroupAdmin)
xadmin.site.register(GroupMsg, GroupMsgAdmin)
xadmin.site.register(RedUser, RedUserAdmin)
xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(Log, LogAdmin)

# 注册主题
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobleSetting)
#xadmin.site.app_name = u'好易贷1'
#xadmin.site.name = u'好易贷2'
#xadmin.site.login_view = u'好易贷3'
xadmin.site.site_header = u'微信机器人后台管理'
xadmin.site.site_title = u'Power By Eric'
