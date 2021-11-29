from django.urls import path 

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name= 'index'),  #Be consistent here, the only path we have here is our home page 
    path('topics',views.topics, name='topics'),
    path('topics/<int:topic_id>/',views.topic, name='topic')
]

