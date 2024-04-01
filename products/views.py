from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                "image": '/static/vendor/img/products/Adidas-hoodie.png',
                "name": 'Худі чорного кольору з монограмами adidas Originals',
                "price": 1500,
                "description": 'М\'яка тканина для світшотів. Стиль і комфорт - це спосіб життя.',
            },
            {
                "image": '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                "name": 'Синя куртка The North Face',
                "price": 5000,
                "description": 'Гладка тканина. Водонепроникне покриття. Легкий і теплий пуховий наповнювач.',
            },
            {
                "image": '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                "name": 'Коричневий спортивний oversized-топ ASOS DESIGN',
                "price": 1200,
                "description": 'Матеріал із плюшевою текстурою. Зручний і м\'який.',
            },
            {
                "image": '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                "name": 'Чорний рюкзак Nike Heritage',
                "price": 1300,
                "description": 'Щільна тканина. Легкий матеріал.',
            },
            {
                "image": '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                "name": 'Чорні туфлі на платформі з 3 парами люверсів Dr Martens 1461 Bex',
                "price": 2300,
                "description": 'Гладкий шкіряний верх. Натуральний матеріал.',
            },
            {
                "image": '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                "name": 'Темно-сині широкі строгі брюки ASOS DESIGN',
                "price": 1890,
                "description": 'Легка еластична тканина сирсакер Фактурна тканина.',
            },
        ]
    }
    return render(request, 'products/products.html', context)
