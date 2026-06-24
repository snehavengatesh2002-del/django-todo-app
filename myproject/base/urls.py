from django.urls import path
from .views import*

urlpatterns =[
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('completed/',completed,name='completed'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('update/<int:pk>/',update,name='update'),
    path('hcomplete/<int:pk>/',hcomplete,name='hcomplete'),
    path('hdelete/<int:pk>/',hdelete,name='hdelete'),
    path('hcompleteall/',hcompleteall,name='hcompleteall'),
    path('hdeleteall/',hdeleteall,name='hdeleteall'),

    path('crestore/<int:pk>',crestore,name='crestore'),

    path('crestoreall/',crestoreall,name='crestoreall'),
    path('tdelete/<int:pk>',tdelete,name='tdelete'),

    
]
