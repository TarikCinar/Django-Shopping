"""bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="home"),
                  path('login/', giris, name="login"),
                  path('kayit/', kayit, name="kayit"),
                  path('iletisim/', iletisim, name="iletisim"),
                  path('sepetim/', sepetim, name="sepetim"),
                  path('sepeti_sil/', sepeti_sil, name="sepeti_temizle"),
                  path('ara/', ara, name="ara"),
                  path('<int:id>/urun_icerigi', icerik, name="urun_icerigi"),
                  path('<str:name>/<int:id>', kategori, name="kategori"),
                  path('<int:id>/<str:name>/sirala', filtre, name="filtrele"),
                  path("logout/", LogoutView.as_view(), name="logout"),
                  path('siparis_et/', siparis_et, name="siparis_et")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
