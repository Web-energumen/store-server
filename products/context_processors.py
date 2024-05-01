from products.models import Basket


def baskets(request):
    user = request.user
    baskets_queryset = Basket.objects.filter(user=user) if user.is_authenticated else []

    total_sum = baskets_queryset.total_sum() if baskets_queryset else 0
    total_quantity = baskets_queryset.total_quantity() if baskets_queryset else 0

    return {
        'baskets': baskets_queryset,
        'total_sum': total_sum,
        'total_quantity': total_quantity
    }

