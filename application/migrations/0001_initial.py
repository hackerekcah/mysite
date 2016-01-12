# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=60)),
                ('given_name', models.CharField(max_length=60)),
                ('nationality', models.CharField(max_length=2)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1)),
                ('address_in_china', models.CharField(max_length=250)),
                ('tel', models.CharField(default=b'86403742', max_length=8)),
                ('school_in_china', models.CharField(default=b'\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8\xe5\xb7\xa5\xe4\xb8\x9a\xe5\xa4\xa7\xe5\xad\xa6', max_length=32)),
                ('passport_type', models.CharField(default=b'\xe6\x99\xae\xe9\x80\x9a', max_length=8)),
                ('passport_number', models.CharField(max_length=32)),
                ('passport_expire_date', models.DateField()),
                ('current_visa_category', models.CharField(choices=[(b'JL', b'\xe5\xb1\x85\xe7\x95\x99\xe8\xaf\x81\xe4\xbb\xb6'), (b'MQ', b'\xe5\x85\x8d\xe7\xad\xbe'), (b'F', b''), (b'L', b''), (b'M', b''), (b'Q2', b''), (b'S2', b''), (b'X2', b''), (b'X1', b'')], max_length=2)),
                ('date_of_entry', models.DateField()),
                ('visa_number', models.CharField(max_length=32)),
                ('visa_expire_date', models.DateField()),
                ('student_category', models.CharField(max_length=8)),
                ('is_JW202', models.NullBooleanField()),
                ('graduate_year', models.CharField(max_length=4, null=True)),
                ('graduate_month', models.CharField(max_length=2, null=True)),
                ('tuition_fee_type', models.CharField(choices=[(b'H', b'Half Year'), (b'F', b'Full Year')], max_length=1, null=True)),
            ],
        ),
    ]
