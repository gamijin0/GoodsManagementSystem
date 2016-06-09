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
