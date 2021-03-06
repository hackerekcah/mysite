# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 02:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_in_china', models.CharField(max_length=64)),
                ('mobile_phone', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=60)),
                ('given_name', models.CharField(max_length=60)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('nationality', models.CharField(max_length=2)),
                ('date_of_birth', models.DateField()),
                ('passport_number', models.CharField(max_length=32)),
                ('passport_valid_until', models.DateField()),
                ('current_visa_category', models.CharField(choices=[('JL', '\u5c45\u7559\u8bc1\u4ef6'), ('MQ', '\u514d\u7b7e'), ('F', 'F'), ('L', 'L'), ('M', 'M'), ('Q2', 'Q2'), ('S2', 'S2'), ('X2', 'X2'), ('X1', 'X1')], max_length=2)),
                ('date_of_entry_visa_free', models.DateField(blank=True, null=True)),
                ('visa_number_x1', models.CharField(blank=True, max_length=32, null=True)),
                ('date_of_entry_x1', models.DateField(blank=True, null=True)),
                ('visa_number_residence_permit', models.CharField(blank=True, max_length=32, null=True)),
                ('visa_valid_until_rp', models.DateField(blank=True, null=True)),
                ('visa_number_special', models.CharField(blank=True, max_length=32, null=True)),
                ('date_of_entry_special', models.DateField(blank=True, null=True)),
                ('duration_of_each_stay_special', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('visa_number_x2', models.CharField(blank=True, max_length=32, null=True)),
                ('once_left_china_x2', models.NullBooleanField()),
                ('visa_valid_until_x2', models.DateField(blank=True, null=True)),
                ('date_of_departure_x2', models.DateField(blank=True, null=True)),
                ('date_of_reentry_x2', models.DateField(blank=True, null=True)),
                ('duration_of_each_stay_x2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('visa_valid_until_final', models.DateField()),
                ('student_category', models.CharField(choices=[('LANGUAGE', 'Chinese Language Student'), ('SELFPAID', 'Self-Financed Degree Student'), ('CSCORHIT', 'CSC/HIT Scholarship Student'), ('EXCHANGE', 'Exchange Student')], max_length=8)),
                ('study_duration_start', models.DateField()),
                ('study_duration_end', models.DateField()),
                ('tuition_fee_type_language', models.CharField(blank=True, choices=[('H', 'Half Year'), ('F', 'Full Year')], max_length=1, null=True)),
                ('tuition_fee_type_selfpaid', models.CharField(blank=True, choices=[('H', 'Half Year'), ('F', 'Full Year')], max_length=1, null=True)),
                ('is_JW202_selfpaid', models.NullBooleanField()),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
