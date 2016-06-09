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
    from Goods.models import Goods
    goodslist = Goods.objects.all()

    kwvars = {
        'goodslist':goodslist,
        'request':request,
    }

    return render_to_response('Goods/GoodsManage.html',kwvars,RequestContext(request))
