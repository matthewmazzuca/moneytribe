from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from files.models import File
from .forms import ContactForm, SignUpForm
from .models import SignUp
from projects.models import Project
from userdata.models import UserData, UserDataImage
from posts.models import Post
from chat.models import Message, Thread
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	# file_form = FileForm()

	if request.user.is_authenticated():
		try:
			if request.user.userdata:
				pass
		except:
			init_userdata(request)
			# addable=UserData.objects.get(user=request.user)

		try:
			profile_img = UserDataImage.objects.get(user=request.user, selected=True)
		except:
			profile_img = False

		projects = Project.objects.all().filter(user=request.user)
		# print projects
		userdata = UserData.objects.all().filter(user=request.user)
		posts = Post.objects.all()
		users = User.objects.all()
		user_files = File.objects.all().filter(user=request.user)
		all_user_imgs = UserDataImage.objects.all().filter(selected=True)

		if check_threads(request) == True:
			threads = Thread.objects.all().order_by('-last_reply')
			messages= Message.objects.all().order_by('sent_at')
			hasthreads = True


	context = {
		"title": title,
		"form": form,
		
	}
	
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you",
			"projects": projects,
			"userdata": userdata,
		}

	if request.user.is_authenticated():
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1

		queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())

		if check_threads(request) == True:
		
			context = {
				"queryset": queryset,
				"projects": projects,
				"userdata": userdata,
				"posts": posts,
				# "addable": addable,
				"threads": threads,
				"messages": messages,
				"hasthreads": hasthreads,
				"users": users,
				"user_files": user_files,
				"profile_img":profile_img,
				"all_user_imgs":all_user_imgs
			}
		else:
			context = {
				"queryset": queryset,
				"projects": projects,
				"userdata": userdata,
				"posts": posts,
				# "addable": addable,
				"users":users, 
				"user_files": user_files,
				"profile_img": profile_img,
				"all_user_imgs":all_user_imgs
			}

	return render(request, "home.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)

def init_userdata(request):
	# first_name = models.CharField(blank=True, max_length=50)
	# last_name = models.CharField(blank=True, max_length=50)
	# first_time = models.BooleanField(default=True)
	# is_contractor = models.BooleanField(default=True)
	# company_name = models.CharField(blank=True, max_length=50)
	# ctype = models.CharField(blank=True, max_length=10)
	# phone = models.CharField(blank=True, max_length=12)
	# street = models.CharField(blank=True, max_length=100)
	# postal = models.CharField(blank=True, max_length=10)
	# city = models.CharField(blank=True, max_length=100)
	# country = models.CharField(blank=True, max_length=100)
	# username = models.CharField(blank=True, max_length=30)
	# image = models.ImageField(upload_to=image_upload_to, blank=True)

	u = UserData(user=request.user, first_name=request.user.username, first_time=True)
	u.save()
	return HttpResponseRedirect('/')


def check_threads(request):
	uid = request.user.id
	if Thread.objects.filter(start_user=uid):
		return True
	elif Thread.objects.filter(second_user=uid):
		return True
	else:
		return False


def check_messages(request):
	uid = request.user.id
	if Message.objects.filter(sender=uid):
		return True
	elif Message.objects.filter(recipient=uid):
		return True
	else:
		return False

def dev(request):

	

	return render(request, "index.html")














