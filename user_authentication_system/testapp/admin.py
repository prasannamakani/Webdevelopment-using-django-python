from django.contrib import admin
from testapp.models import People 


class PeopleAdmin(admin.ModelAdmin):
    list_display=['Username', 'Email','Password']


admin.site.register(People,PeopleAdmin)


# Register your models here.
