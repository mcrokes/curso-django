from django.forms import ModelForm, TextInput, Textarea, FileInput

from core.erp.models import Category, Product


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_field = True
        # for form in self.visible_fields():
        #     if first_field:
        #         form.field.widget.attrs['autofocus'] = True
        #         first_field = False
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Category
        fields = '__all__'
        # labels = {
        #     'name': 'Descripción'
        # }

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data

    def clean(self):
        cleaned = super().clean()
        print(cleaned)
        return cleaned

class ProductForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.fields['name'].widget.attrs['aotofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data
