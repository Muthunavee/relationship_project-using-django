from django.contrib import admin
from userapp.models import User,UserProfile
from userapp.models import Category,Product
from userapp.models import Course,Student

admin.site.register(User)
admin.site.register(UserProfile)

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Course)
admin.site.register(Student)