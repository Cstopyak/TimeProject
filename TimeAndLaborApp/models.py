from django.db import models
import re
from datetime import date
import calendar
import bcrypt


class UserManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        userswithSameEmail = User.objects.filter(email = postData['email'])
        

        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["fnamereq"] = "First name is Required"
        
        if len(postData['lname']) < 2:
            errors["lnamereq"] = "Last name is Required"

        if len(postData['email']) == 0:
            errors["emailreq"] = "Email is Required"

        elif not EMAIL_REGEX.match(postData['email']):
            errors["emailpattern"] = "Email is invalid"
        elif len(userswithSameEmail)>0:
            errors ['emailtaken'] = "Try another email."

        if len(postData['pass']) == 0:
            errors["passreq"] = "Password is Required"
        
        elif len(postData['pass']) < 8:
            errors["passreq"] = "8 characters required for password"

        if postData['pass'] != postData['confpass']:
            errors["confpassmatch"] = "Password must match"
        
        return errors



    def loginValidation(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors["emailreq"] = "Email is Required"
        userswithSameEmail = User.objects.filter(email = postData['email'])
        
        if len(userswithSameEmail) == 0:
            errors ['emailnotregistered'] = "Please register your email"
        else:
            print(userswithSameEmail[0].password)
            # if userswithSameEmail[0].password != postData['pass']:
            #     errors['incorrectpassword'] = "Incorrect Password. Please put correct password in."
            if not bcrypt.checkpw(postData['pass'].encode(), userswithSameEmail[0].password.encode()):
                errors['incorrectpassword'] = 'Password is incorrect!'

        return errors

class RequestedManager(models.Manager):
    def PtoValidator(self, postData):
        errors = {}
        if int(postData['RequestedTimeOff']) < 0:
            errors["no Pto time remaining"] = "You have no Pto Time left scrub"

        return errors



class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    Pto = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Requested(models.Model):
    RequestedTimeOff = models.IntegerField()
    description = models.TextField(null=True)
    UserPTO = models.ForeignKey(User, related_name="MyTimeOff", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RequestedManager()

class Scheduler(models.Model):
    
    employee = models.ForeignKey(User, related_name="timesheet", on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    clock_in = models.TimeField(null=True)
    clock_out = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

