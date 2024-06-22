from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Page

# Create your views here.

def about_view(request):
    # Vista de "Acerca de mí"
    return render(request, 'about.html')

def pages_list_view(request):
    # Vista para listar todas las páginas
    pages = Page.objects.all()
    return render(request, 'pages_list.html', {'pages': pages})

def page_detail_view(request, page_id):
    # Vista para ver detalles de una página específica
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'page_detail.html', {'page': page})