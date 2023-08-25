from django import forms 
from .models import xailox

class AdvForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control form-control-lg '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg '}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg '}))
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input '}),required=False)
    
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-lg '})) 
    class Meta:
        model = xailox()
        fields = '__all__'
        labels = {
            # Здесь можно указать нужные метки для полей
        }
        widgets = {
            # Здесь можно указать нужные виджеты для полей
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Здесь можно добавить кастомную логику, если необходимо

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Здесь можно добавить кастомную логику, если необходимо
        if commit:
            instance.save()
        return instance