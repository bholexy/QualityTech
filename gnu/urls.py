from django.urls import path, re_path,  include

from . import views

app_name = 'gnu'

urlpatterns = [    
    path('signup/', views.signup, name='signup'), 
    path('index/', views.index, name='index'),    
    path('accounts/', include('django.contrib.auth.urls')),
]
