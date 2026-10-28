from django.contrib import admin
from django.urls import path


admin.site.site_header = "Livraria | Administração"
admin.site.site_title = "Administração da Livraria"
admin.site.index_title = "Gestão da livraria"

urlpatterns = [
    path("admin/", admin.site.urls),
]
