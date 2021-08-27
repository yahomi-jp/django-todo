from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from todo.views import top

urlpatterns = [
    path('', top, name='top'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('todo/', include('todo.urls'),),
]
