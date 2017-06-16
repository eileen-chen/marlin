from django.forms import ModelForm
from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    # def save(self, commit=True):
    #     User = super(UserForm, self).save(commit=False)
    #     User.email = self.cleaned_data['email']
    #     if commit:
    #         User.save()
    #     return User  