from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django_recaptcha.fields import ReCaptchaField

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Никнейм или email',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField()


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='E-mail',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username.lower()


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'email': 'Email',
            'username': 'Никнейм'
        }


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
        labels = {
            'old_password': 'Старый пароль',
            'new_password1': 'Новый пароль',
            'new_password2': 'Повтор нового пароля'
        }
