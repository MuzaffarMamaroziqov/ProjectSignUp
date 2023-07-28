from django.urls import path
from . import views

urlpatterns=[

    path('',views.Blog, name='home'),
    path('salom/',views.Backup, name='back'),
]