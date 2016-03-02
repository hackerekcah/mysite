# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=60)),
                ('given_name', models.CharField(max_length=60)),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('nationality', models.CharField(max_length=2)),
                ('date_of_birth', models.DateField()),
                ('address_in_china', models.CharField(max_length=250)),
                ('passport_number', models.CharField(max_length=32)),
                ('passport_valid_until', models.DateField()),
                ('current_visa_category', models.CharField(max_length=2, choices=[('JL', '\u5c45\u7559\u8bc1\u4ef6'), ('MQ', '\u514d\u7b7e'), ('F', ''), ('L', ''), ('M', ''), ('Q2', ''), ('S2', ''), ('X2', ''), ('X1', '')])),
                ('visa_number', models.CharField(max_length=32)),
                ('date_of_entry_x1', models.DateField(null=True)),
                ('visa_valid_until_rp', models.DateField(null=True)),
                ('date_of_entry_special', models.DateField(null=True)),
                ('duration_of_each_stay_special', models.PositiveSmallIntegerField(null=True)),
                ('once_left_china_x2', models.NullBooleanField()),
                ('visa_valid_until_x2', models.DateField(null=True)),
                ('date_of_departure_x2', models.DateField(null=True)),
                ('date_of_reentry_x2', models.DateField(null=True)),
                ('duration_of_each_stay_x2', models.PositiveSmallIntegerField(null=True)),
                ('visa_valid_until_final', models.DateField(null=True)),
                ('student_category', models.CharField(max_length=8, choices=[('LANGUAGE', 'Chinese Language Student'), ('SELFPAID', 'Self-Financed Degree Student'), ('CSCORHIT', 'CSC/HIT Scholarship Student'), ('EXCHANGE', 'Exchange Student')])),
                ('study_duration_start', models.DateField()),
                ('study_duration_end', models.DateField()),
                ('tuition_fee_type_language', models.CharField(max_length=1, null=True, choices=[('H', 'Half Year'), ('F', 'Full Year')])),
                ('tuition_fee_type_selfpaid', models.CharField(max_length=1, null=True, choices=[('H', 'Half Year'), ('F', 'Full Year')])),
                ('is_JW202_selfpaid', models.NullBooleanField()),
            ],
        ),
    ]
