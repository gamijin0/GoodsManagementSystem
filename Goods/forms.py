# coding: utf-8
from django import forms

class GoodsForm(forms.Form):
    goods_name= forms.CharField(label=u"名称",
                                error_messages={"required":u"名称不能为空"},
                                widget=forms.TextInput(attrs={"class":"form-control"})
                                )
    category_name =forms.CharField(label=u"类型",
                                   error_messages={"required":u"类型不能未空"},
                                   widget=forms.TextInput(attrs={"class":"form-control"}),
                                   )

class PurchaseForm(forms.Form):
    purchase_num = forms.IntegerField(
        label=u"进货数量",
        error_messages = {"required": u"数量不能为空"},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    purchase_price=forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        label=u"进货价格",
        error_messages={"required": u"价格不能为空"},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )


class SaleForm(forms.Form):
    sale_num = forms.IntegerField(
        label=u"卖出数量",
        error_messages={"required": u"数量不能为空"},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sale_earn_actual = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        label=u"实际收入",
        error_messages={"required": u"收入不能为空"},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )