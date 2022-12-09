from django.contrib import admin
from django.contrib.auth.models import User ,Group
from .models import Profile ,Dweet


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]
    # Only display the "username" field
    fields = ["username"]
   
    
    
    

#admin.site.register(User,UserAdmin)
#admin.site.register(Dweet)
#admin.site.unregister(User)
#admin.site.unregister(Group)