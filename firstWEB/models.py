from django.db import models
# Create your models here.
class members(models.Model):
    empno=models.CharField(max_length=20,primary_key=True)
    empwd=models.CharField(max_length=10)
    empname=models.CharField(max_length=20)
    age=models.CharField(max_length=10,null=True)
    sex=models.CharField(max_length=10,null=True)
    pos=models.CharField(max_length=5,null=True)
    group=models.CharField(max_length=5,null=True,default='0')
class log(models.Model):
    stakeholder=models.CharField(max_length=20,default='未知')
    logno=models.CharField(max_length=20,primary_key=True)
    logname=models.CharField(max_length=10)
    doc=models.CharField(max_length=3000,null=True)
    remarks=models.CharField(max_length=500,null=True)
class task(models.Model):
    taskno = models.CharField(max_length=20,primary_key=True)
    taskname = models.CharField(max_length=10)
    time = models.CharField(max_length=20,null=True)
    ddl = models.CharField(max_length=20,null=True)
    taskgroup = models.CharField(max_length=10,null=True)
    taskperson = models.CharField(max_length=20,null=True)
    state=models.CharField(max_length=10,null=True)
    remarks = models.CharField(max_length=500,null=True)
class story(models.Model):
    storyno=models.CharField(max_length=20,primary_key=True)
    stakeholder=models.CharField(max_length=20,default='未知')
    role=models.CharField(max_length=20,default='未知')
    activity=models.CharField(max_length=20)
    value=models.CharField(max_length=20)
    itview=models.CharField(max_length=200,null=True)
    quenaire=models.CharField(max_length=200,null=True)
    remarks=models.CharField(max_length=500,null=True,default='无')
class hd(models.Model):
    hdno=models.CharField(max_length=10,primary_key=True)
    hdname=models.CharField(max_length=20)
    hdstyle=models.CharField(max_length=20,default='普通用户')
class gb(models.Model):
    gbno=models.CharField(max_length=20,primary_key=True)
    gbname=models.CharField(max_length=100)
class que(models.Model):
    queno=models.CharField(max_length=20,primary_key=True)
    quename=models.CharField(max_length=200)
    quemodel=models.CharField(max_length=20,null=True)
    queans=models.CharField(max_length=200,default="未输入答案")
class interview(models.Model):
    itviewno=models.CharField(max_length=20,primary_key=True)
    itviewque=models.CharField(max_length=200)
    itviewans=models.CharField(max_length=200)
class setting(models.Model):
    bg=models.CharField(max_length=1000)
    goal=models.CharField(max_length=1000)
    success=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=1000,default='无')