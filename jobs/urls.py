from  django.urls import path,include
from . import views

urlpatterns=[
    path('',view=views.home,name='landing'),
    path('jobs',views.cronjob_list,name='cronjob_list'),
    path('jobs/create',views.cronjob_create,name='cronjob_create'),
    path('jobs/logs/<int:pk>',views.cronjob_create,name='log_list'),
    path('jobs/edit/<int:pk>',views.cronjob_create,name='cronjob_edit'),
    path('jobs/delete/<int:pk>',views.cronjob_create,name='cronjob_delete'),

]