import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .models import Product

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
domain = settings.DOMAIN


class ProductListView(ListView):
    model = Product
    template_name = 'my_shop/list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'my_shop/detail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        print('kwargs',*kwargs)
        product = Product.objects.filter(available=True)
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product = Product.objects.get(id=product_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'product_data': {
                            'name': product.name,
                        },
                        'currency': 'usd',
                        'unit_amount': product.price,
                    },
                    'quantity': 1,
                },
            ],
            metadata={'product_id': product.id},
            mode='payment',
            success_url=f'{domain}/success/',
            cancel_url=f'{domain}/failed/',
        )
        print(session)
        return JsonResponse({'id': session.id})


class PaymentSuccessView(TemplateView):
    template_name = 'my_shop/success.html'


class PaymentFailedView(TemplateView):
    template_name = 'my_shop/failed.html'
