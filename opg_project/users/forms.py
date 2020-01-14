from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Profile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(), label='Korisničko ime')
    password = forms.CharField(widget=forms.PasswordInput(), label='Lozinka')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-3 text-right'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        Field('username', 'password')
    )
    helper.form_method = 'POST'


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['username'].widget.attrs.pop("autofocus", None)

    username = forms.EmailField(max_length=64, label='Email (korisničko ime)')
    confirm_username = forms.EmailField(max_length=64, label='Potvrda emaila')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Lozinka')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        Field('username', 'confirm_username', 'password1'),
    )
    helper.form_method = 'POST'
    helper.form_tag = False

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        email = cleaned_data.get('username')
        email_conf = cleaned_data.get('confirm_username')

        if email and email_conf and email != email_conf:
            self._errors['confirm_username'] = self.error_class(['Email-ovi ne odgovaraju.'])
            del self.cleaned_data['confirm_username']
        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        labels = {
            'name': 'Ime',
            'surname': 'Prezime',
            'opg_name': 'Naziv OPG-a',
            'address': 'Adresa',
            'phone': 'Telefon',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        Field('name', 'surname', 'opg_name', 'address', 'phone'),
    )
    helper.form_method = 'POST'


class ReadOnlyProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['readonly'] = True

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        Field('name', 'surname', 'opg_name', 'address', 'phone'),
    )
