from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django import forms
# from .models import Profile

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    # def get_initial_for_field(self, field, field_name):
    #     if field_name in self.Meta.profile_fields:
    #         try:
    #             return getattr(self.instance.profile, field_name)
    #         except Profile.DoesNotExist:
    #             return None
    #     return super().get_initial_for_field(field, field_name)


    # def save_profile(self, commit=True):
    #     try:
    #         profile = self.instance.profile
    #     except Profile.DoesNotExist:
    #         profile = Profile.objects.create(profile=self.instance)
    #     for field in self.Meta.profile_fields:
    #         setattr(profile, field, self.cleaned_data[field])
    #     if not profile.photo:
    #         profile.photo = None
    #     if commit:
    #         profile.save()

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name']
        # profile_fields = ['phone_number']


