from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name="register"),
    path('login/',views.login, name="login"),
    path('logout',views.logout,name="logout"),
    path('add/', views.add, name='add'),
    path("addrec/",views.addrec,name="addrec"),
    path('new/',views.new, name='new'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('new/update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
    
]