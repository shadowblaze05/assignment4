from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.DateField()

    def __str__(self):
        return f"{self.title} published by {self.author}"

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
    
#     def __str__(self):
#        return f"{self.first_name} {self.last_name}"

# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category)
#     published = models.DateField()
    
#     def __str__(self):
#         return self.title
                                                    
