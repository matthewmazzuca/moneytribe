from django.contrib import admin

# Register your models here.
from .models import UserData, UserDataImage, UserAddress

class UserdataModelAdmin(admin.ModelAdmin):
	list_display = ["user", "first_name"]
	list_display_links = ["user", "first_name"]
	# list_editable = ["user"]
	# list_filter = ["first_name", "is_contractor"]

	search_fields = ["user", "first_name"]
	class Meta:
		model = UserData

admin.site.register(UserData, UserdataModelAdmin)
admin.site.register(UserDataImage)
admin.site.register(UserAddress)
