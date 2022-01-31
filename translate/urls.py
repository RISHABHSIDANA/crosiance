from django.urls import path
from translate import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sign/',views.sign,name='sign'),
]