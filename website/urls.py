from django.conf.urls import patterns, include, url

from django.conf import settings
from website.views import Home,About
import LolSpider.views as LolSpider_views
import MyPhaser.views as MyPhaser_views
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$',LolSpider_views.index),
    url(r'^$',Home),
    url(r'^index.html$', Home),

    url(r'^PK/$',MyPhaser_views.index),
    url(r'^query/$',LolSpider_views.GetData),

    url(r'^about/$',About),

    url(r'^accounts/',include('UserManage.urls' )),


    #static
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,}),
)
