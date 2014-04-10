from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from restaurant import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menu/(?P<menu_cat_id>\d+)/$', views.menu_cat, name='menu_cat')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
