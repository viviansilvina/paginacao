from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista/lista_produtos.html', {'page_obj': page_obj})

def nomes(request):
    return render(request, 'lista/nomes.html')
