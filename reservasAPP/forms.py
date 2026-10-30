from django import forms
from reservasAPP.models import Estado, Reserva
from django.core.validators import MinValueValidator, MaxValueValidator

class ReservaForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), validators=[MinValueValidator(1), MaxValueValidator(15)] )
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Reserva
        fields = '__all__'



class EstadoForm(forms.ModelForm):
    estado = forms.CharField()
    
    estado.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Estado
        fields = '__all__'