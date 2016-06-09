# coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@login_required()
@PermissionVerify()
def SaleCollect(request):
    from Goods.models import Sale
    salelist =Sale.objects.all()

    kwvars = {
        'request': request,
        'salelist':salelist
    }
    return render_to_response('Goods/GoodsManage.html', kwvars, RequestContext(request))

