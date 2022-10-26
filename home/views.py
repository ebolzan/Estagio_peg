from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'disciplina': 'tecnico em informatica da UFSM - Politecnico',
        'tecnologia': 'Pỳthon e Django',
    }
    return render(request, 'index.html', context)

