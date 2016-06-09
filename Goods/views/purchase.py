# coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@login_required()
@PermissionVerify()
def Purchase(request,goods_id):
    from Goods.models import Purchase as PurchaseModel
    from Goods.models import Goods
    from django.utils import timezone
    oneToPurchase = PurchaseModel(
        purchase_id=str(timezone.now())[:-6].replace(' ','-').replace(',','-').replace('.','-'),
        goods=Goods.objects.get(goods_id=goods_id),
        purchase_num=int(request.POST['purchase_num']),
        purchase_price=float(request.POST['purchase_price'])
    )
    print (oneToPurchase.goods.goods_name)
    print "添加了一条进货记录"
    oneToPurchase.save()
    return HttpResponseRedirect(reverse('goodsmanage'))
