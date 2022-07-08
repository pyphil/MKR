from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def register(request):
    email_error = False
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if request.POST.get('email') in ['abc@genm.info', 'test13@genm.info']:
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # render info page about email confirmation
        else:
            email_error = True
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form': form, 'email_error': email_error})
