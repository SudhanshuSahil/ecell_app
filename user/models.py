# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4
from django.db import models
from common.v1.utils.helpers import get_url_friendly
from common.models import LifeTimeTrackingModel, ActiveModel


STUDENT = 'student'
PROFESSIONAL = 'professional'
ENTREPRENEUR = 'entrepreneur'
PROFESSION_CHOICES = (
    (STUDENT, 'student'),
    (PROFESSIONAL, 'professional'),
    (ENTREPRENEUR, 'entrepreneur'),
)



class User(ActiveModel):

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	# str_id = models.CharField(max_length=58, editable=False, null=True)    
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40)
    email = models.CharField(max_length=255, null=True)
    esummit_id = models.CharField(max_length=255, null=True)
    profession = models.CharField(
        max_length=20, default=STUDENT, choices=PROFESSION_CHOICES)
    # password_hash = models.CharField(max_length=20)
    # secret_key = models.CharField(max_length=16)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.user_id),
                                   str(self.user_name),
                                   str(self.email),
                                   str(self.status))


class Login(LifeTimeTrackingModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    session_token = models.CharField(
        editable=False, blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'user_login'

    def __unicode__(self):
        return "%s__%s" % (str(self.user), str(self.session_token))
