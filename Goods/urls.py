from django.conf.urls import patterns, include, url

urlpatterns = patterns('Goods.views',
    # url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^manage/$','goodsManage.Manage',name='goodsmanage'),
    url(r'^delgoods/(.+)/$','goodsManage.DelGoods',name='delgoods'),
    url(r'^purchase/(.+)/$','purchase.Purchase',name='purchase'),
    url(r'^delpurchase/(.+)/$','purchase.DelPurchase',name='delpurchase'),
    url(r'^sale/(.+)/$','sale.Sale',name='sale'),

)
