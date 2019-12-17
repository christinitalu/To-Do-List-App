
from django.contrib import admin
from django.urls import path ,include
from atodo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('atodo_list.urls')),
]
