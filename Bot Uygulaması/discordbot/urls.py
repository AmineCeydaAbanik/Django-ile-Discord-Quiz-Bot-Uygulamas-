from django.contrib import admin
from django.urls import path, include
from api.views import RastgeleSoru,formlar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rastgele/', RastgeleSoru.as_view(), name='rastgele'),
    path('', formlar),
]
