from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('course/<slug>/', views.view_course, name="course"),
    # path('become_pro/',views.become_project, name='become_pro'),
    path('charge', views.charge, name='charge'),
    path('become_pro1/',views.become_project1, name='become_pro1'),
    path('pro/', views.become_pro, name="become_pro"),
    path('charge1', views.charge1, name='charge1'),
    path('become_pro2/',views.become_project2, name='become_pro2'),

]