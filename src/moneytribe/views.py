from django.shortcuts import render, get_object_or_404

def home(request):
	return render(request, "base.html", {})

def _404(request):
	return render(request, "404.html", {})

def agents(request):
	return render(request, "agents.html", {})

def blog_single(request):
	return render(request, "blog-single.html", {})

def blog(request):
	return render(request, "blog.html", {})

def car_insurance(request):
	return render(request, "car-insurance.html", {})

def claims(request):
	return render(request, "claims.html", {})

def contact(request):
	return render(request, "contact.html", {})

def get_a_car_insurance_quote(request):
	return render(request, "get-a-car-insurance-quote.html", {})

def get_a_house_insurance_quote(request):
	return render(request, "get-a-house-insurance-quote.html", {})

def get_a_life_insurance_quote(request):
	return render(request, "get-a-life-insurance-quote.html", {})

def get_a_travel_insurance_quote(request):
	return render(request, "get-a-travel-insurance-quote.html", {})

def house_insurance(request):
	return render(request, "house-insurance.html", {})

def life_insurance(request):
	return render(request, "life-insurance.html", {})

def travel_insurance(request):
	return render(request, "travel-insurance.html", {})

def profile(request):

	try:
		profile_img = UserDataImage.objects.get(user=request.user, selected=True)
	except:
		profile_img = False

	context = { "profile_img": profile_img,

	}
	return render(request, "profile.html", context	)

def usersettings(request):

	try:
		profile_img = UserDataImage.objects.get(user=request.user, selected=True)
	except:
		profile_img = False

	context = { "profile_img": profile_img,

	}
	return render(request, "profile_settings.html", context	)
# def features(request):

# 	return render(request, "features.html", {})

# def pricing(request):
	
# 	return render(request, "pricing.html", {})