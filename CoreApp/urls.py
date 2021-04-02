from django.urls import path
# from . import views
from .views import Home,Sports

urlpatterns=[
    # path('',views.Home,name='home')
    path('',Home.as_view(),name='home'),
    path('sports/',Sports.as_view(),name='sports')
]
