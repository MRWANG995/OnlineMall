#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from cartapp.cartmanager import *


class CartView(View):
    def post(self,request):
        #在多级字典中使用以下设置，能够实时更新session中的数据
        request.session.modified = True

        #获取当前用户操作类型变量值
        flag = request.POST.get('flag','')

        #判断用户当前操作类型
        if flag == 'add':
            #获取cartManager对象
            cartManager = getCartManger(request)
            #加入购物车操作
            cartManager.add(**request.POST.dict())

        elif flag == 'minus':
            # 获取cartManager对象
            cartManager = getCartManger(request)
            # 修改购物项数量
            cartManager.update(step=-1,**request.POST.dict())

        elif flag == 'plus':
            # 获取cartManager对象
            cartManager = getCartManger(request)
            # 修改购物项数量
            cartManager.update(step=1, **request.POST.dict())

        elif flag == 'delete':
            # 获取cartManager对象
            cartManager = getCartManger(request)
            #移除购物车中相应商品
            cartManager.delete(**request.POST.dict())


        return HttpResponseRedirect('/cart/queryAll/')


def queryAll(request):
    # 获取cartManager对象
    cartManager = getCartManger(request)
    #获取当前登录用户购物项表中的所有信息
    cartItemList = cartManager.queryAll()

    return render(request,'cart.html',{'cartItemList':cartItemList})