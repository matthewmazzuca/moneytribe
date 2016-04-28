from django.shortcuts import render, get_object_or_404

def home(request):
	return render(request, "base.html", {})



# def features(request):

# 	return render(request, "features.html", {})

# def pricing(request):
	
# 	return render(request, "pricing.html", {})