from django import forms
from app.models import modelo_mas

class form_mas (forms.ModelForm):
    class Meta:
        model = modelo_mas
        fields = '__all__'