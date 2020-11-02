# from django.db import models
# from django.utils import timezone
# # from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
# # from django.contrib.auth.models import django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)

# class User(models.Model):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=25, unique=True)
#     first_nameUser = models.CharField(max_length=40)
#     last_nameUser = models.CharField(max_length=140)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     facility = models.CharField(max_length=140)
#     jobdescription = models.CharField(max_length=140)
#     positiondescription = models.CharField(max_length=140)
    
    
# class Employee(models.Model):
#     firstname = models.TextField()
#     lastname = models.TextField()
#     gender = models.CharField(max_length =50)
#     roleemp = models.ForeignKey('Role', on_delete=models.CASCADE) 
#     nameemp= models.ForeignKey('Industry', on_delete=models.CASCADE)
#     def __str__(self):
#         return "%s %s" % (self.firstname, self.lastname)
    
    
# class Review(models.Model):
#     finalrating = models.TextField()
#     firstname = models.ForeignKey('Employee', on_delete=models.CASCADE)
#     valuesrev = models.ForeignKey('Values', on_delete=models.CASCADE)
#     namerev =   models.ForeignKey('Industry', on_delete=models.CASCADE)
#     contentrev = models.ForeignKey('Competences', on_delete=models.CASCADE)
#     questionrev = models.ForeignKey('QuestionsValues', on_delete=models.CASCADE)
#     answerrev = models.ForeignKey('AnswerValues', on_delete=models.CASCADE)
#     questionrev = models.ForeignKey('QuestionsRole', on_delete=models.CASCADE)
#     answerrev = models.ForeignKey('AnswerRole', on_delete=models.CASCADE)
#     questionrev = models.ForeignKey('QuestionsCompetences', on_delete=models.CASCADE)
#     answerrev = models.ForeignKey('AnswerCompetences', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.finalrating 
    
# class Industry(models.Model):
#     name = models.CharField(max_length =100)
#     date_selectedIndustry = models.DateTimeField(default =timezone.now)
#     authorindu = models.ForeignKey('User', on_delete=models.CASCADE)
#     roleindus = models.ForeignKey('Role', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name  

# class Role(models.Model):
#     title = models.CharField(max_length =100)
#     date_selectedRole = models.DateTimeField(default = timezone.now)
#     authorRole = models.ForeignKey('User', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title  
    
# class Values(models.Model):
#     value = models.CharField(max_length =150)
#     date_selectedValues = models.DateTimeField(default =timezone.now)
#     authorval =models.ForeignKey('User', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.value 
    
# class Competences(models.Model):
#     content = models.TextField()
#     date_postedCompetences = models.DateTimeField(default = timezone.now)
#     authorcomp = models.ForeignKey('User', on_delete=models.CASCADE)
#     valuecomp = models.ForeignKey('Values', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.content 
    
# class QuestionsValues(models.Model):
#     valueque = models.ForeignKey('Values', on_delete=models.CASCADE)
#     questionvalue = models.TextField()
#     ansvalue = models.ForeignKey('AnswerValues', on_delete=models.CASCADE )
#     def __str__(self):
#         return "%s" % (self.questionvalue) 
    
# class QuestionsRole(models.Model):
#     titleque = models.ForeignKey('Role', on_delete=models.CASCADE)
#     questionrole = models.TextField()
#     ansrole = models.ForeignKey('AnswerRole', on_delete=models.CASCADE )
#     def __str__(self):
#         return "%s" % (self.questionrole)
    
# class QuestionsCompetences(models.Model):
#     contentque = models.ForeignKey('Competences', on_delete=models.CASCADE)
#     questioncomp = models.TextField()
#     anscomp = models.ForeignKey('AnswerCompetences', on_delete=models.CASCADE )
#     def __str__(self):
#         return "%s" % (self.questioncomp)
    
# class AnswerValues(models.Model):
#     valuean = models.ForeignKey('Values', on_delete=models.CASCADE)
#     questvalue = models.ForeignKey('QuestionsValues', on_delete=models.CASCADE )
#     answervalue = models.TextField()
#     def __str__(self):
#         return "%s" % (self.answervalue) 
    
# class AnswerRole(models.Model):
#     titlean = models.ForeignKey('Role', on_delete=models.CASCADE)
#     questrole = models.ForeignKey('QuestionsRole', on_delete=models.CASCADE)
#     answerrole = models.TextField()
#     def __str__(self):
#         return "%s" % (self.answerrole)
    
# class AnswerCompetences(models.Model):
#     contentan = models.ForeignKey('Competences', on_delete=models.CASCADE)
#     questcomp = models.ForeignKey('QuestionsCompetences', on_delete=models.CASCADE)
#     answercomp = models.TextField()
#     def __str__(self):
#         return "%s" % (self.answercomp)
    
    
# class Notes(models.Model):
#     note = models.TextField()
#     def __str__(self):
#         return self.note 
