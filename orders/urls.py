from django.urls import path

from orders.views import (CanselTemplateView, OrderCreateView,
                          SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CanselTemplateView.as_view(), name='order_canceled'),
]
