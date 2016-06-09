# coding: utf-8
from django.db import models

# 货物表(货物id,货物名称,货物类型,)
# Goods(goods_id,goods_name,category_name)
#
# 进货表（进货id,进货日期,货物,进货数量,进货单价)
# Purchase(purchase_id,date,goods,purchase_num,purchase_price)
#
# 操作记录表(操作id,操作日期,操作描述)
# ActionRecord(action_id,action_date,action_introduction)

class Goods(models.Model):
    goods_id = models.CharField(max_length=50,null=False,primary_key=True)
    goods_name= models.CharField(max_length=25,null=False)
    category_name =models.CharField(max_length=20,null=False)


class Purchase(models.Model):
    purchase_id = models.CharField(max_length=50,null=False,primary_key=True)
    purchase_date = models.DateTimeField(auto_now_add=True,null=False)
    goods = models.ForeignKey(Goods,null=False)
    purchase_num = models.IntegerField(null=False)
    purchase_price =models.DecimalField(max_digits=6,decimal_places=2,null=False)

class ActionRecord(models.Model):
    action_id = models.CharField(max_length=20,null=False,primary_key=True)
    action_date= models.DateTimeField(auto_now_add=True,null=True)
    action_introduciton = models.TextField(max_length=1000,default=None)

class Sale(models.Model):
    goods = models.ForeignKey(Goods,null=False)
    sale_date = models.DateTimeField(auto_now_add=True,null=False)
    sale_num = models.SmallIntegerField(null=False)
    cost_price = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    sale_earn_actual = models.DecimalField(max_digits=6,decimal_places=2,null=False)