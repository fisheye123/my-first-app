from django.contrib import admin
from comm_forms.models import Comm_Form

@admin.register(Comm_Form)
class AdminComm_Form(admin.ModelAdmin):
    list_display = ['book', 'name', 'date']
    ordering = ['book'] #sort by book