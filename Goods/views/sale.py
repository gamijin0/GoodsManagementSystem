#coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@login_required()
@PermissionVerify()
def Sale(request,goods_id):
    from Goods.models import Sale as SaleModel,Goods as GoodsModel,Purchase as PurchaseModel
    goods = GoodsModel.objects.get(goods_id=goods_id)

    purchaseList = PurchaseModel.objects.filter(goods=goods)

    #先统计所有剩余数量
    remain_num_total =0
    actual_earn = request.POST['sale_earn_actual']
    want_to_sell_num =request.POST['sale_num']

    for p in purchaseList:
        remain_num_total+=p.purchase_num

    if(want_to_sell_num>remain_num_total):
        res = u"试图卖出"+str(want_to_sell_num)+u"个货物,但剩余数量为"+str(remain_num_total)
        res+=u"个,操作失败！"
        return HttpResponse(res)
    else:
        for p in purchaseList:
            if(want_to_sell_num>=p.purchase_num):
                #某一价格的被售完
                oneToSale = SaleModel(
                    goods=goods,
                    sale_num=p.purchase_num,
                    cost_price=p.purchase_price,
                    sale_earn_actual=0
                )
                oneToSale.save()
                want_to_sell_num-=p.purchase_num
                PurchaseModel.delete(p)
            else:
                #剩余某一价格
                oneToSale = SaleModel(
                    goods=goods,
                    sale_num=want_to_sell_num,
                    cost_price=p.purchase_price,
                    sale_earn_actual=actual_earn,
                )
                oneToSale.save()
                p.purchase_num-=want_to_sell_num
                p.save()

        return HttpResponseRedirect(reverse('goodsmanage'))