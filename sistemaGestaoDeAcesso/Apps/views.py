from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def configuracoes(request):
    return render(request, 'configuracoes.html')

def perfil(request):
    return render(request, 'perfil.html')

def consultas(request):
    return render(request, 'consultas.html')

def cadastros(request):
    return render(request, 'cadastros.html')

def manual(request):
    return render(request, 'manual.html')

def search(request):
    query = request.GET.get('q', '')
    return render(request, 'search.html', {'query': query})
