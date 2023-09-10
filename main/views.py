from django.shortcuts import render

def show_main(request):
    products = {
        'name': 'Muhammad Fawwaz Arshad Said',
        'amount': 20000,
        'price': 20000.00,
        'description': "Woi"
    },
    {
        'name': 'iudc',
        'amount': 10000,
        'price': 10000.00,
        'description': "ids"
    },

    context = {
        'products': products
    }

    return render(request, "main.html", context)