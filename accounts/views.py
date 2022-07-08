from django.shortcuts import render
from .models import Profile, AllowedEmail
from .forms import RegisterUserForm
from uuid import uuid4
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    email_error = False
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        allowed_emails = AllowedEmail.objects.get(school="genm")
        if request.POST.get('email') in allowed_emails.emails:
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                newuuid = uuid4().hex
                Profile.objects.create(
                    user=user,
                    uuid=newuuid
                )
                print("Confirmation uuid: ", newuuid)
                # render info page about email confirmation
                # set user active:
                u = User.objects.get(profile__uuid=newuuid)
                u.is_active = True
                u.save()
        else:
            email_error = True
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form': form, 'email_error': email_error})
