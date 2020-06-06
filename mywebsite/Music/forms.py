from django import forms
from . import models

class Add_Album_Form(forms.ModelForm):
    class Meta:
        model=models.Album
        exclude=()
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control','placeholder':'Album Name','required':''}),
            "artist":forms.TextInput(attrs={'class':'form-control','placeholder':'Artist Name','required':''}),
            "img_path":forms.FileInput(attrs={'class':'form-control-file','required':''}),


        }



