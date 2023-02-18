from django.urls import path

from .views import (CreateCheckoutSessionView, PaymentFailedView,
                PaymentSuccessView, ProductDetailView, ProductListView)


app_name = 'my_shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('item/<int:id>/',ProductDetailView.as_view(), name='detail'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('buy/<int:id>/', CreateCheckoutSessionView.as_view(), name='buy'),
]