from django.db import models

class Events(models.Model):



class UserProfile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    ldap_id = models.CharField(max_length=50, null=True, blank=True)
    roll_no = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.URLField(null=True, blank=True)
    fcm_id = models.CharField(max_length=200, null=True, blank=True)
    Interested_Events=models.ForeignKey(Events, on_delete=models.CASCADE)
    Going_Events = models.ForeignKey(Events, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    contact_number=models.BigAutoField(null=True, blank=True)
    
