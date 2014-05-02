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
    url(r'^login_index/$', views.login_index),
    url(r'^suggestion/$', views.suggestion, name='suggestion'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<album_name>.*)/$', views.album, name='album'),
    url(r'^like/(?P<food_menu_id>\d+)/$', views.food_menu_like, name='food_menu_like'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
	url(r'^logout_redirect/$', views.logout_redirect, name='logout_redirect'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

