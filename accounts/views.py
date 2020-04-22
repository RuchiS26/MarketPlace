from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 

from .models import Profile
from .forms import UserForm, ProfileForm

def login_view(request):
	if request.user.is_authenticated:
		return redirect('marketplace:marketplace-index')

	if(request.method == 'POST'):
		authForm = AuthenticationForm(data = request.POST)
		if(authForm.is_valid()):
			user = authForm.get_user()
			login(request,user)

			if(Profile.objects.filter(user = user).exists()):
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:
					return redirect('marketplace:marketplace-index')
			else:
				return redirect('accounts:accounts-setup')

	else:
		authForm = AuthenticationForm()

	return render(request, 'accounts/accounts-login.html', {'authForm':authForm})

def logout_view(request):
	logout(request)
	return redirect('accounts:accounts-login')

@login_required(login_url = 'accounts:accounts-login')
def setup(request):
	if request.method == 'POST':
		userForm = UserForm(request.POST, instance = request.user)
		profileForm = ProfileForm(request.POST, request.FILES)
		if(profileForm.is_valid() and userForm.is_valid()):
			instance = profileForm.save(commit = False)
			instance.user = request.user
			instance.save()

			userForm.save()

			return redirect('marketplace:marketplace-index')
	else:
		userForm = UserForm(instance = request.user)
		profileForm = ProfileForm()

	return render(request, 'accounts/accounts-setup.html',{'profileForm':profileForm,'userForm':userForm})

def edit_profile(request):

	user = request.user 

	if request.method == 'POST':

		userform = UserForm(request.POST,instance = user)
		profileform = ProfileForm(request.POST, request.FILES, instance = user.profile)

		if(userform.is_valid() and profileform.is_valid()):
			userform.save()
			profileform.save()

			return redirect("marketplace:marketplace-user",user)

	else:
		userform = UserForm(instance = user)
		profileform = ProfileForm(instance = user.profile)

	return render(request, "accounts/accounts-edit.html", {'userform':userform, 'profileform':profileform})

