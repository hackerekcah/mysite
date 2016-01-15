# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals

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
    ('CSC','CSC Scholarship Student'),
    ('EXCHANGE','Exchange Student'),
)

# Create your models here.
class Applicant(models.Model):
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

    #单位电话，默认为 86403742
    #这一项其实没什么用，打印pdf的时候可以用常量
    tel = models.CharField(max_length=8,default="86403742")

    #在华学校，默认为 哈尔滨工业大学
    #这一项其实没什么用，打印pdf的时候可以用常量
    school_in_china = models.CharField(max_length=32,default="哈尔滨工业大学")

    #护照类型，默认为 普通
    #这一项其实没什么用，打印pdf的时候可以用常量
    passport_type = models.CharField(max_length=8,default="普通")

    #护照号码
    passport_number = models.CharField(max_length=32)

    #护照有效期至
    passport_expire_date = models.DateField()

    #现持有效签证种类,可能取值为
    #JL(代表居留证件)，MQ(免签)，F,L,M,Q2,S2,X2,X1
    current_visa_category = models.CharField(max_length=2,choices=VISA_TYPE_CHOICES)

    #入境日期
    date_of_entry = models.DateField()

    #签证号码
    visa_number = models.CharField(max_length=32)

    #签证有效期至
    visa_expire_date = models.DateField()

    #学生类别,可能取值
    #LANGUAGE,SELFPAID,CSC,EXCHANGE
    student_category = models.CharField(max_length=8)

    #是否填写过JW202
    is_JW202 = models.NullBooleanField(null=True)

    #预计毕业年份
    graduate_year = models.CharField(max_length=4,null=True)

    #预计毕业月份
    graduate_month = models.CharField(max_length=2,null=True)

    #现已缴纳学费类别
    tuition_fee_type = models.CharField(max_length=1,choices=TUITION_FEE_CHOICES,null=True)




