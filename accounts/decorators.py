# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
import functools

# Create your decorators here.
def login_required(func):
    @functools.wraps(func)
    def wrapper(request,*args, **kw):
        user = request.session.get('username')
        if user is not None:
            return func(request,*args, **kw)
        else:
            return HttpResponseRedirect('/accounts/login/')
    return wrapper