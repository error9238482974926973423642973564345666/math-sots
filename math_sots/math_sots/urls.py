from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('mathapp.urls'))
    path('admin/', admin.site.urls),
]
