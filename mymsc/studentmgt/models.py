from django.db import models
from datetime import datetime

# Create your models here.
class Teacher(models.Model):
    SUBJECTS = (('Maths','Maths'),('English','English'),('Physics','Physics'),
                ('Chemistry','Chemistry'),('Biology','Biology'),('Geography','Geography'))
    QUALIFICATION = (('NCE','NCE'),('HND','HND'),('BSc','BSc'))
    MS = (('Single','Single'),('Married','Married'),('Widowed','Widowed'))
    GENDER = (('male', 'male'), ('female', 'female'))
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    age = models.IntegerField()
    date_recruited = models.DateField(default=datetime.now)
    course = models.CharField(max_length=255, choices=SUBJECTS)
    qualification = models.CharField(max_length=255, choices=QUALIFICATION)
    position = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    phone_num = models.IntegerField()
    marital_status = models.CharField(max_length=255, choices=MS)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    GENDER = (('male','male'),('female','female'))
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255, choices=GENDER)
    date_enrolled = models.DateField(default=datetime.now)
    address = models.CharField(max_length=255)
    phone_num = models.IntegerField()

    def __str__(self):
        return self.full_name

class Exam(models.Model):
    student_id = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    maths = models.IntegerField()
    english = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    biology = models.IntegerField()
    geography = models.IntegerField()


class Test(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    maths = models.IntegerField()
    english = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    biology = models.IntegerField()
    geography = models.IntegerField()


