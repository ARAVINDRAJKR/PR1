from django.urls import path
from .import views
urlpatterns = [
    path('h/',views.hi),
    path('p/',views.obj),
    path('b/',views.aabasoft),
    path('ar/',views.aravind),
    path('t/',views.student),
    path('f/',views.fl),
    path('c/',views.c),
    path('e/',views.en),
    path('s/',views.od),
    path('o/',views.order),
    path('upd',views.updt),
    path('del',views.delete),
    path('email',views.mail),
    path('email2',views.mail2),
    path('email3',views.mail3),
    path('email4',views.mail4),
    path('',views.page)
]