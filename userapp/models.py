from django.db import models


class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.PositiveBigIntegerField()
    age=models.PositiveIntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    role=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=100)
    
    def __str__(self):
        return f"profile of {self.user.name}"
    
class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()   
    # default=1 here we use means it set as 1
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    course=models.ManyToManyField(Course)
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=100)
    state=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name