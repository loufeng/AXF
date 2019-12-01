#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 
# author:loufeng
from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^cart/', views.car, name='cart'),
    url(r'^market/', views.market, name='market'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.market_with_params, name='market_with_params'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^checkuser/', views.checkuser, name='checkuser'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^activate/', views.activate, name='activate'),
    url(r'^addtocart/', views.addtocart, name='addtocart'),
    url(r'^changecartstate/', views.changecartstate, name='changecartstate'),
    url(r'^subshopping/', views.subshopping, name='subshopping'),
    url(r'^allselect/', views.allselect, name='allselect'),
    url(r'^makeorder/', views.makeorder, name='makeorder'),
    url(r'^orderdetail/', views.orderdetail, name='orderdetail'),
    url(r'^orderlistnotpay/', views.orderlistnotpay, name='orderlistnotpay'),
    url(r'^payed/', views.payed, name='payed'),
]