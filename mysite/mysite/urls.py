from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('stock_recommender/', include('stock_recommender.urls')),
    path('admin/', admin.site.urls),
]