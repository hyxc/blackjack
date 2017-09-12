# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# Create your forms here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
