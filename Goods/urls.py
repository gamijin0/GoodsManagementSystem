from django.conf.urls import patterns, include, url

urlpatterns = patterns('Goods.views',
    # url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^manage/$','goodsManage.Manage',name='goodsmanage')
)
