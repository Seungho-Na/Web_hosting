from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('stock_news/', include('stock_news.urls')),
    path('admin/', admin.site.urls),
]