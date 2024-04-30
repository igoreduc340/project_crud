from django.shortcuts import render
from .models import FormularioForm,Formulario
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            
           
            form.save()
            formularios = Formulario.objects.all()
            return render(request,'cadastros.html',{'formularios' : formularios})
        
        else:
            return render(request, 'index.html', {'form': form})

    else:
        form = FormularioForm()
        return render(request, 'index.html', {'form': form})
    
    

    


