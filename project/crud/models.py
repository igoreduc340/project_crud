from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator


text_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message='The field must contain only letters and spaces.',
)

# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=100,validators=[text_validator])
    idade = models.IntegerField(
       validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    
    email = models.EmailField()
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
    

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'idade', 'email', 'telefone']