from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import ClientRegistrationForm
from django.contrib import messages
from .models import CustomUser

import string
import random

# Create your views here.
def registerClient(request):
    pw_charset_lower = list(string.ascii_lowercase)
    pw_charset_upper = list(string.ascii_uppercase)
    pw_charset_digit = list(string.digits)
    password = ""
    charset = list()
    charset += pw_charset_lower
    charset += pw_charset_upper
    charset += pw_charset_digit
    for _ in range(16):
        password += random.choice(charset)
    print(password)
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('full_name')
            messages.success(request, '{} is successfully added!'.format(username))
            send_mail(
                'Net CMS Member',
                """Dear {name},
Welcome to Net CMS. You can access the site by login in 
with the your email and password: {pas} """.format(name=form.cleaned_data['full_name'],pas=form.cleaned_data['password1']),
                'mugabwaallan18071@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            
            return redirect('user_list')
    else:
        form = ClientRegistrationForm()
    return render(request, 'registerClient.html', {'form':form,'pwd':password})

def currentUsers(request):
    allusers = CustomUser.objects.all().order_by('full_name')
    context = {
        'c_users':allusers
    }
    return render(request, 'users_list.html', context)