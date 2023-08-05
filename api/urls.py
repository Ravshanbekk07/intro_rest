from django.urls import path
from .views import getask,postask#@#,putask#,deletetask

urlpatterns=[
    # path('hello/',hello_world),
    # path('hello/<str:name>/',hello_world),

    path('get/',getask),
    path('get/<str:title>/',getask),
    path('postask/',postask),
    #path('putask/<int:pk>/',putask),
    # path('deletetask/<int:pk>/',deletetask),
]