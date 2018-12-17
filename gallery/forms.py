from django import forms


class CreateGallery(forms.Form):
    name = forms.CharField(label='Name', max_length=40)
    description = forms.CharField(label='Description', max_length=255)


class LoadPhoto(forms.Form):
    photo = forms.ImageField(label='Load photo')
