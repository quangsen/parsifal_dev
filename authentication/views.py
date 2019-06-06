from django.shortcuts import render
from authentication.forms import SignUpForm
from django.contrib import messages
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.add_message(
                request, messages.ERROR, 'There was some problems while creating your account. Please review some fields before submiting again.')
            return render(request, 'auth/signup.html', {'form': form})
        else:
            return HttpResponse('is valid')
    else:
        return render(request, 'auth/signup.html', {'form': SignUpForm()})
