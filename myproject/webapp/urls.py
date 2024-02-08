from django.urls import path
from .views import loginlist,loginpage
from webapp import views

urlpatterns = [
    path('login1/', loginlist.as_view(), name='login1'),
    path('login1/<int:pk>/', loginlist.as_view(), name='login-detail'),
    path('login1/<int:pk>/', loginlist.as_view(), name='login-detail'),
    path('loginpage/',views.loginpage,name='loginpage')


    ]