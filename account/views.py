from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, permission_required

def CreateUser():
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.last_name = 'Lennon'
    user.save()

def ChangePassword():
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

def logout_view(request):
    logout(request)
    # Redirect to a success page.



@login_required
#@permission_required('polls.add_choice', raise_exception=True)
def Profile(request):
    ...

