from django import forms

# from models import User

'''
class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ['name', 'role', 'email', 'description']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
'''
'''
        name = cleaned_data.get("name")
        role = cleaned_data.get("role")
        email = cleaned_data.get("email")
        description = cleaned_data.get("description")
'''
