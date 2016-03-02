# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.conf import settings


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

VISA_TYPE_CHOICES =(
    ('JL','居留证件'),
    ('MQ','免签'),
    ('F','F'),
    ('L','L'),
    ('M','M'),
    ('Q2','Q2'),
    ('S2','S2'),
    ('X2','X2'),
    ('X1','X1'),
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
class ApplicationForm(models.Model):
#################################Address & Contact################################
    #在华地址
    address_in_china = models.CharField(max_length=64)

    #手机号码
    mobile_phone = models.CharField(max_length=32)

    user_email  = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    )
#################################Passport Info################################
    #姓
    surname = models.CharField(max_length=60)
    #名
    given_name = models.CharField(max_length=60)

    #sex is gender,which is M or F
    sex = models.CharField(max_length=1,choices=GENDER_CHOICES)

    #nationality use the alpha2 country code for efficiency
    nationality = models.CharField(max_length=2)

    #date of birth
    date_of_birth =models.DateField()

    #护照号码
    passport_number = models.CharField(max_length=32)

    #护照有效期至
    passport_valid_until = models.DateField()
#################################Visa Info######################################
    #现持有效签证种类,可能取值为
    #JL(代表居留证件)，MQ(免签)，F,L,M,Q2,S2,X2,X1
    current_visa_category = models.CharField(max_length=2,choices=VISA_TYPE_CHOICES)

    #visa free 入境日期
    date_of_entry_visa_free = models.DateField(null=True,blank=True)

    #签证号码
    visa_number_x1 = models.CharField(max_length=32,null=True,blank=True)

    #x1入境日期
    date_of_entry_x1 = models.DateField(null=True,blank=True)


    #签证号码
    visa_number_residence_permit = models.CharField(max_length=32,null=True,blank=True)

    #签证有效期至
    visa_valid_until_rp = models.DateField(null=True,blank=True)


    #签证号码
    visa_number_special = models.CharField(max_length=32,null=True,blank=True)

    #special入境日期
    date_of_entry_special = models.DateField(null=True,blank=True)

    duration_of_each_stay_special = models.PositiveSmallIntegerField(null=True,blank=True)


    #签证号码
    visa_number_x2 = models.CharField(max_length=32,null=True,blank=True)

    once_left_china_x2 = models.NullBooleanField()

    visa_valid_until_x2 = models.DateField(null=True,blank=True)

    date_of_departure_x2 = models.DateField(null=True,blank=True)

    date_of_reentry_x2 = models.DateField(null=True,blank=True)

    duration_of_each_stay_x2 = models.PositiveSmallIntegerField(null=True,blank=True)

    #签证有效期至，最终填在申请表上的，师弟用这个
    visa_valid_until_final = models.DateField()
#################################Admission Info######################################
    #学生类别,可能取值
    #LANGUAGE,SELFPAID,CSCORHIT,EXCHANGE
    student_category = models.CharField(max_length=8,choices=STUDENT_CATEGORY_CHOICES)

    #学习期限，开始时间，举例2014-02-23
    study_duration_start = models.DateField()

    #学习期限，结束时间，用来判断是否在一年内毕业。还可判断交换时长，超过9个月就是一年的
    study_duration_end = models.DateField()

    #现已缴纳学费类别
    tuition_fee_type_language = models.CharField(max_length=1,choices=TUITION_FEE_CHOICES,null=True,blank=True)

    #现已缴纳学费类别，师弟不要用这个
    tuition_fee_type_selfpaid = models.CharField(max_length=1,choices=TUITION_FEE_CHOICES,null=True,blank=True)

    #是否填写过JW202,可能取值True,Fals,Null
    is_JW202_selfpaid = models.NullBooleanField(null=True,blank=True)


    def save(self, *args, **kwargs):
        for var in vars(self):
            if not var.startswith('_'):
                if self.__dict__[var] == '':
                    self.__dict__[var] = None
        super(ApplicationForm, self).save(*args, **kwargs)
