from django.contrib import admin
from django.urls import path
from home.views import home_views,raw_material_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home_views.home_view),
    path('raw-materials/',raw_material_views.rawMaterial_view),
    path('finished-goods/',)
]
