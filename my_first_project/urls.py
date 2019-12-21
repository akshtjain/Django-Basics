
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('HelloWorld.urls')),
    path('', include('HelloWorld.urls')),

]
