from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Seleccione un archivo Excel")
