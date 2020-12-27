from django.contrib import admin
from blog.models import Blog
from blog.models import Contact

# Register your models here.
# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['sno','title','slug','time']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','desc']