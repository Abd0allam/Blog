from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from .sitemaps import CategorySitemap, PostSitemap
from core.views import frontpage, about, robots_txt


sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('blog/', include('blog.urls')),
    path('frontbage/', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
