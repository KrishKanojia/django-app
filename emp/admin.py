from django.contrib import admin
from .models import Emp,Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_Id','phone',)
    list_editable=('working','emp_Id')
    search_fields=('name','phone',)
    list_filter=('working',)

# Register your models here.
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
