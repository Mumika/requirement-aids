from django.urls import path
from . import views
urlpatterns = [
    #首页
    path('',views.login,name='login'),
    # 以下为成员，任务，日志数据库增删改及显示的相关功能
    path('addmember/',views.addMember,name='addmember'),
    path('memberlist/',views.memberList,name='memberlist'),
    path('addlog/',views.addLog,name='addlog'),
    path('loglist/',views.logList,name="loglist"),
    path('addtask/',views.addTask,name="addtask"),
    path('tasklist/',views.taskList,name='tasklist'),
    #以下为index页面显示的相关功能
    path('index/', views.index, name='index'),
    path('left/',views.left,name='left'),
    path('head/',views.head,name='head'),
    path('head2/',views.head2,name='head2'),
    path('main/',views.main,name='main'),
    #以下为需求获取模块显示的相关功能
    path('selectmodel/',views.selectmodel,name='selectmodel'),
    path('fieldwork/',views.fieldwork,name='fieldwork'),#兼顾标准的显示
    path('interview/',views.interview,name='interview'),
    path('questionnaire',views.questionnaire,name='questionnaire'),
    path('addgb/', views.addgb, name='addgb'),
    path('requdemo/',views.requDemo,name='requdome'),
    path('addhoder/',views.addhoder,name='addhoder'),
    path('addtaskremarks',views.addtaskremarks,name='addtaskremarks'),
    path('hoderlist',views.hoderlist,name='hoderlist'),
    path('addstory/', views.addStory, name='addstory'),
    path('addque/',views.addque,name='addque'),
    path('addsetting/',views.addsetting,name='addsetting'),
]
