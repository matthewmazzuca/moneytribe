from django.contrib import admin

# Register your models here.
from .models import Loan, LoanDetail, LoanShare

admin.site.register(Loan)
admin.site.register(LoanDetail)
admin.site.register(LoanShare)