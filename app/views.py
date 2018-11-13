from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Village, User, SHG
from django.contrib import auth
# Create your views here.
def home(request):
	return render(request, 'app/home.html', {})

def vlogin(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		ps = request.POST.get("pass")

		user = authenticate(request,username=name, password=ps)
		if user is not None:
			n = user.is_village
			if n==True:
				auth.login(request, user)

				return render(request, 'app/village.html', {'user':user})
			else:
				messages.success(request, 'Incorrect email or password')
				return HttpResponseRedirect('/vlogin/')
		else:
			messages.success(request, 'Incorrect email or password')
			return HttpResponseRedirect('/vlogin/')
	else:
		return render(request, 'app/villogin.html', {})

def slogin(request):
	return render(request, 'app/shglogin.html', {})

def ssignup(request):
	return render(request, 'app/ssignup.html', {})

def vsignup(request):
	if request.method == 'POST':
		vname = request.POST.get("vname")
		fname = request.POST.get("fname")
		lname = request.POST.get("lname")
		labour = request.POST.get("labour")
		raw1 = request.POST.get("raw1")
		raw2 = request.POST.get("raw2")
		raw3 = request.POST.get("raw3")
		ps = request.POST.get("password")
		land = request.POST.get("land")
		lat = request.POST.get("lat")
		lang = request.POST.get("lang")
		water = request.POST.get("water")

		user = authenticate(username=vname, password=ps)
		if user is not None:
			messages.success(request, 'User already exists. Please Login!')
		else:
			user = User.objects.create_user(name, email, ps)
			user.is_village = True

			user.save()

			vil = Village.objects.create(user=user,village_name=vname,raw1=raw1,raw2=raw2,raw3=raw3,labour=labour,water=water,landsize=land,contact=7788996655)
			vil.save()
			messages.success(request,'Your profile was successfully updated!')

		return HttpResponseRedirect('/vlogin/')

	else:
		return render(request, 'app/vsignup.html', {})

"""
@login_required
def vdashboard(request):
	if request.method == 'POST':
		#user=request.user
		#uname = user.username
		uname=request.POST.get("name")
		v = VillageIndustry.objects.filter(vname=uname)
		return render(request, 'app/village.html', {'v':v})
"""

def vdashboard(request):
	user=request.user
	uname = user.username
	print(uname)
	v = VillageIndustry.objects.filter(vname=uname)
	return render(request, 'app/village.html', {'v':v})

def ind(request):
	return render(request, 'app/ind.html')