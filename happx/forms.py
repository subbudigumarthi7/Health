from django import forms
from django.contrib.auth.models import User

from happx.models import patmodels


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')


select = [('select', 'select'),('male', 'male'),
        ('female', 'Female')
        ]

choice = [('select', 'select'),('ortho', 'Ortho'),
        ('Dental', 'Dental'),
        (' Gynaecologist', 'Gynaecologist'),
        ('Veterinarian', 'Veterinarian'),
        ('Neurologist', 'Neurologist'),
        ('Pulmonologist', 'Pulmonologist'),
        ('Radiologist', 'Radiologist')
]

class Proform(forms.ModelForm):
    sex = forms.CharField(label="select Gender", widget=forms.Select(choices=select))
    Doctortype = forms.CharField(label="select Doctor",widget=forms.Select(choices=choice))
    problem = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = patmodels
        fields = ('sex', 'Doctortype', 'problem')
