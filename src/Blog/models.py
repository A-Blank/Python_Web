# coding:utf-8

from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField

# Create your models here.

class Blog_Post(models.Model):
    title = models.CharField('标题',max_length = 50)
    summary=models.TextField('简介',max_length=150)
    body = UEditorField('内容', height=300, width=1000,default=u'', blank=True, 
                        imagePath="images/",toolbars='besttome', filePath='files/')
#     timestamp = models.DateTimeField(u'123', auto_now=True, editable = True)
    timestamp = models.DateTimeField(auto_now=True, editable = True)
    
    def __str__(self):
        return self.title

class Post_Admin(admin.ModelAdmin):  
    # 此处添加tinymce的脚本，前提是静态文件访问已经配置上去了  
    class Media:  
        js = (  
#             '/static/js/tinymce/tinymce.min.js',  
#             '/static/js/tinymce/textareas.js',  
     )  