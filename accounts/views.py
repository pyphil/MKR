from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST.get('username'))
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
