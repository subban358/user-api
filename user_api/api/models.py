from django.db import models

# Create your models here.
class Student(models.Model):
    """ Details about Students """
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)
    dept = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.name + ' ' + self.dept