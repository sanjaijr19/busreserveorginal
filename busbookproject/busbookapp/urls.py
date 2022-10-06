from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('home/', views.empDetails,name="home"),
    path('draccess/', views.driverDetails,name="draccess"),
    path('signin/home/', views.empDetails,name="home"),
    path('create/', views.create_view),
    path('update/', views.update_view),
    path('delete/<id>', views.delete_view,name="delete"),
    path('update/<id>', views.update_view,name="update"),
    path('homepage/', views.homepage, name="homepage"),
    path('signout', views.signout, name="signout"),
    # path('consumerlogin/', views.consumerlogin, name='consumerlogin'),
    path('consumer/', views.consumer_view),
    path('addconsumer/', views.consumer_view),
    path('deleteconsumer/<id>', views.deleteconsumer_view),
    path('updateconsumer/<id>', views.updateconsumer_view),
    path('consumerdisplay/', views.consumerdisplay_view, name='consumerdisplay'),
    path('login/consumerdisplay/', views.consumerdisplay_view, name='loginconsumerdisplay'),
    path('login/draccess/',views.driverDetails, name='loginemployee'),
    path('login/home/',views.driverDetails, name='loginemployee'),
    path('login/customerview/',views.customerview, name='logincustomer'),
    path('foreignkey/',views.foreignkey, name='foreignkey'),
    path('selectionfield/',views.selectionfeild, name='selectionfield'),
    path('busseat/',views.busseat, name='busseat'),
    path('seat/',views.seat, name='seat'),
]