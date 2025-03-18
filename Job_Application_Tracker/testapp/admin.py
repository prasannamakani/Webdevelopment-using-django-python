from django.contrib import admin
from testapp.models import People,JobApplication 


class PeopleAdmin(admin.ModelAdmin):
    list_display=['Username', 'Password','Confirm_Password']


admin.site.register(People,PeopleAdmin)

# Register your models here.

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['Company', 'Position', 'Ctc', 'Date']

admin.site.register(JobApplication, JobApplicationAdmin)
