#coding :utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@login_required()
@PermissionVerify()
def Manage(request):

    if(request.method=="POST"):
        from Goods.models import Goods
        from django.utils import timezone

        goods_name = request.POST['goods_name']
        category_name = request.POST['category_name']
        oneToCreate = Goods(goods_name=goods_name,
                            category_name=category_name,
                            goods_id=str(timezone.now())[:-6].replace(' ','-').replace('.','-').replace(',','-')+"-"+str(request.POST['goods_name'])
                            )
        oneToCreate.save()
        return HttpResponseRedirect(reverse('goodsmanage'))

    else:
        from Goods.models import Goods,Purchase
        from Goods.forms import GoodsForm,PurchaseForm
        goodslist = Goods.objects.all()
        purchaselist = Purchase.objects.all()
        kwvars = {
            'goodslist':goodslist,
            'purchaselist':purchaselist,
            'request':request,
            'goodsform':GoodsForm(),
            'purchaseform':PurchaseForm(),
        }

        return render_to_response('Goods/GoodsManage.html',kwvars,RequestContext(request))

@login_required()
@PermissionVerify()
def DelGoods(request,goods_id):
    from Goods.models import Goods
    onrToDel =Goods.objects.get(goods_id=goods_id)
    Goods.delete(onrToDel)
    return HttpResponseRedirect(reverse('goodsmanage'))
