from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        self.category_id = kwargs.get('category_id')
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        return queryset.filter(category_id=self.category_id) if self.category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
