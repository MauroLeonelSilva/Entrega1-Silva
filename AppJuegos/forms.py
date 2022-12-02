from django import forms

class CartasForm(forms.Form):
    juego = forms.CharField(max_length=50)
    nombre_carta= forms.CharField(max_length=50)
    rareza = forms.CharField(max_length=20)


class VideojuegosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    calificacion= forms.IntegerField()
    genero = forms.CharField(max_length=20)


class juegosdemesaform(forms.Form):
    Nombrejuego= forms.CharField(max_length=50)
    Tipo_juego= forms.CharField(max_length=50)
    Cantidad_jugadores= forms.IntegerField()


