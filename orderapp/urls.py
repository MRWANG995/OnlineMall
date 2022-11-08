#coding=utf-8
from django.conf.urls import url
from orderapp import views

urlpatterns=[

    url(r'^$',views.order_view),
    url(r'^toOrder/$',views.toOrder),
    url(r'^toPay/$',views.toPay),
    url(r'^checkPay/$',views.checkPay),
]