from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from restaurant import views
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menu/(?P<menu_cat_name>.*)/$', views.menu_cat, name='menu_cat'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^accounts/', include('allauth.urls'), name='accounts'),
    url(r'^fb', views.fb_index),
    #url(r'^gallery/$', views.gallery, name='gallery')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

