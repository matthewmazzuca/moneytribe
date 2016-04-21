from django.contrib import admin

# Register your models here.
from .models import Thread, Message

# class ThreadAdmin(admin.ModelAdmin):
# 	list_display = ["user", "first_name", "is_contractor"]
# 	list_display_links = ["user", "first_name"]
# 	# list_editable = ["user"]
# 	list_filter = ["first_name", "is_contractor"]

# 	search_fields = ["user", "first_name"]
# 	class Meta:
# 		model = UserData

# class MessageAdmin(admin.ModelAdmin):
# 	list_display = ["user", "first_name", "is_contractor"]
# 	list_display_links = ["user", "first_name"]
# 	# list_editable = ["user"]
# 	list_filter = ["first_name", "is_contractor"]

# 	search_fields = ["user", "first_name"]
# 	class Meta:
# 		model = UserData

admin.site.register(Message)
# admin.site.register(Variation)
admin.site.register(Thread)