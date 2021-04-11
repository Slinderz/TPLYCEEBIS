from django.contrib import admin

# Register your models here.
from.models import Student,Cursus



class StudentAdmin(admin.ModelAdmin):
  list_display = ('first_name', "last_name", 'mail', 'phone', 'cursus', 'birth_date')
  #fields = ['first_name', 'last_name', 'mail', 'phone', 'cursus', 'birth_date']
  fieldsets = [('zone1', {'fields': ['first_name', 'last_name', 'birth_date']}),
  ('zone2', {'fields': ['mail', 'phone', 'cursus'], 'classes':['collapse']})]
admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus)