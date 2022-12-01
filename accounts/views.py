from django.shortcuts import redirect, render
from .models import Profile, AllowedEmail
from .forms import RegisterUserForm
from uuid import uuid4
from django.contrib.auth.models import User
from threading import Thread
from django.core.mail import send_mail


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
                # TODO: Send Mail
                print("Confirmation uuid: ", newuuid)
                # render info page about email confirmation
                return redirect('registration_email')
        else:
            email_error = True
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {'form': form, 'email_error': email_error})


def registration_email(request):
    return render(request, 'registration/registration_email.html', {})


def confirm_email(request, uuid):
    # set user active:
    error = False
    try:
        u = User.objects.get(profile__uuid=uuid)
        u.is_active = True
        u.save()
    except User.DoesNotExist:
        error = True

    return render(request, 'registration/email_success.html', {'error': error})


class mail_thread(Thread):
    # TODO: Anpassen
    def __init__(self, student_ids):
        super(mail_thread, self).__init__()
        self.student_ids = student_ids
        self.noreply = Config.objects.get(name="noreply-mail")

    # run method is automatically executed on thread.start()
    def run(self):
        for id in self.student_ids:
            student = Student.objects.get(id=id)
            oldcode = student.code
            # put oldcode on delete list if exists
            if oldcode is not None:
                CodeDeletion.objects.create(
                    code_to_delete=oldcode,
                    name=student.name,
                    firstname=student.firstname,
                    group=student.group
                )
            newcode = Code.objects.filter(type='y').first()
            student.code = newcode.code
            # delete used code
            newcode.delete()
            student.date = datetime.today()
            student.save()
            mail_text_obj = Config.objects.get(name='mail_text')
            mail_text = mail_text_obj.text
            mail_text = mail_text.replace('#NAME#', student.firstname)
            mail_text = mail_text.replace('#CODE#', student.code)

            send_mail(
                'WLAN-CODE',
                mail_text,
                self.noreply,
                [student.email],
                fail_silently=True,
            )