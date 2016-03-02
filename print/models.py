# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

from time import timezone

from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

VISA_TYPE_CHOICES =(
    ('JL','居留证件'),
    ('MQ','免签'),
    ('F',''),
    ('L',''),
    ('M',''),
    ('Q2',''),
    ('S2',''),
    ('X2',''),
    ('X1',''),
)
#tuition_fee
TUITION_FEE_CHOICES = (
    ('H','Half Year'),
    ('F','Full Year'),
)


#LANGUAGE,SELFPAID,CSC,EXCHANGE
STUDENT_CATEGORY_CHOICES =(
    ('LANGUAGE','Chinese Language Student'),
    ('SELFPAID','Self-Financed Degree Student'),
    ('CSCORHIT','CSC/HIT Scholarship Student'),
    ('EXCHANGE','Exchange Student'),
)

# Create your models here.
class Applicant2(models.Model):
    #姓
    surname = models.CharField(max_length=60)
    given_name = models.CharField(max_length=60)

    #sex is gender,which is M or F
    sex = models.CharField(max_length=1,choices=GENDER_CHOICES)

    #nationality use the alpha2 country code for efficiency
    nationality = models.CharField(max_length=2)

    #date of birth
    date_of_birth =models.DateField()

    #在华地址
    address_in_china = models.CharField(max_length=250)

    #护照号码
    passport_number = models.CharField(max_length=32)

    #护照有效期至
    passport_valid_until = models.DateField()

    #现持有效签证种类,可能取值为
    #JL(代表居留证件)，MQ(免签)，F,L,M,Q2,S2,X2,X1
    current_visa_category = models.CharField(max_length=2,choices=VISA_TYPE_CHOICES)

    #签证号码
    visa_number = models.CharField(max_length=32)

    #x1入境日期
    date_of_entry_x1 = models.DateField(null=True)

    #签证有效期至
    visa_valid_until_rp = models.DateField(null=True)

    #special入境日期
    date_of_entry_special = models.DateField(null=True)

    duration_of_each_stay_special = models.PositiveSmallIntegerField(null=True)

    once_left_china_x2 = models.NullBooleanField()

    visa_valid_until_x2 = models.DateField(null=True)

    date_of_departure_x2 = models.DateField(null=True)

    date_of_reentry_x2 = models.DateField(null=True)

    duration_of_each_stay_x2 = models.PositiveSmallIntegerField(null=True)

    #签证有效期至，最终填在申请表上的，师弟用这
    visa_valid_until_final = models.DateField(null=True)

    #学生类别,可能取值
    #LANGUAGE,SELFPAID,CSCORHIT,EXCHANGE
    student_category = models.CharField(max_length=8,choices=STUDENT_CATEGORY_CHOICES)

    #学习期限，开始时间，举例2014-02-23
    study_duration_start = models.DateField()

    #学习期限，结束时间，用来判断是否在一年内毕业。还可判断交换时长，超过9个月就是一年的
    study_duration_end = models.DateField()

    #现已缴纳学费类别
    tuition_fee_type_language = models.CharField(max_length=1,choices=TUITION_FEE_CHOICES,null=True)

    #现已缴纳学费类别，师弟不要用这个
    tuition_fee_type_selfpaid = models.CharField(max_length=1,choices=TUITION_FEE_CHOICES,null=True)

    #是否填写过JW202,可能取值True,Fals,Null
    is_JW202_selfpaid = models.NullBooleanField(null=True)
