from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

