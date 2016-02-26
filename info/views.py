from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext, loader
from django.http import Http404

from info.models import ApplicationForm

import sys
import datetime


def info_to_db(request):

    postList = request.POST

    visaType = postList.get("applicant.current_visa_category")

    if(visaType == "JL"):
        visa_valid_until_final = postList.get("applicant.visa_valid_until_rp")
    elif (visaType == "X1"):
        entryDateStr = postList.get("applicant.date_of_entry_x1")
        entryDate = datetime.datetime.strptime(entryDateStr, "%Y-%m-%d").date()
        visa_valid_until_final = entryDate + datetime.timedelta(days=29)

        visa_valid_until_final.strftime('%Y-%m-%d')
    elif (visaType == "MQ"):
        entryDateStr = postList.get("applicant.date_of_entry_visa_free")
        entryDate = datetime.datetime.strptime(entryDateStr, "%Y-%m-%d").date()
        visa_valid_until_final = entryDate + datetime.timedelta(days=29)

        visa_valid_until_final.strftime('%Y-%m-%d')
    elif (visaType == "F") or (visaType == "L") or (visaType == "M") or (visaType == "Q2") or (visaType == "S2"):
        entryDateStr = postList.get("applicant.date_of_entry_special")
        entryDate = datetime.datetime.strptime(entryDateStr, "%Y-%m-%d").date()
        duration_of_each_stay_special_str = postList.get("applicant.duration_of_each_stay_special")
        visa_valid_until_final = entryDate + datetime.timedelta(int(duration_of_each_stay_special_str))

        visa_valid_until_final.strftime('%Y-%m-%d')
    elif (visaType == "X2"):
        if "T" == postList.get("applicant.once_left_china_x2"):
            date_of_reentry_x2_str = postList.get("applicant.date_of_reentry_x2")
            date_of_reentry_x2 = datetime.datetime.strptime(date_of_reentry_x2_str, "%Y-%m-%d").date()
            duration_of_each_stay_x2_str = postList.get("applicant.duration_of_each_stay_x2")
            visa_valid_until_final = date_of_reentry_x2 + datetime.timedelta(int(duration_of_each_stay_x2_str))

            visa_valid_until_final.strftime('%Y-%m-%d')

        elif "F" == postList.get("applicant.once_left_china_x2"):
            visa_valid_until_final = postList.get("applicant.visa_valid_until_x2")
    else:
        print "unknown visa type!"

    newApt = ApplicationForm(
        address_in_china =              postList.get("applicant.address_in_china",None),
        mobile_phone=                   postList.get("applicant.mobile_phone",None),
########################################################################################################
        surname =                       postList.get("applicant.surname",None),
        given_name=                     postList.get("applicant.given_name",None),
        sex=                            postList.get("applicant.sex",None),
        nationality=                    postList.get("applicant.nationality",None),
        date_of_birth=                  postList.get("applicant.date_of_birth",None),
        passport_number=                postList.get("applicant.passport_number",None),
        passport_valid_until=           postList.get("applicant.passport_valid_until",None),
#########################################################################################################
        current_visa_category=          postList.get("applicant.current_visa_category",None),

        date_of_entry_visa_free=        postList.get("applicant.date_of_entry_visa_free",None),

        visa_number_x1=                 postList.get("applicant.visa_number_x1",None),
        date_of_entry_x1=               postList.get("applicant.date_of_entry_x1",None),

        visa_number_residence_permit=   postList.get("applicant.visa_number_residence_permit",None),
        visa_valid_until_rp=            postList.get("applicant.visa_valid_until_rp",None),

        visa_number_special=            postList.get("applicant.visa_number_special",None),
        date_of_entry_special=          postList.get("applicant.date_of_entry_special",None),
        duration_of_each_stay_special=  postList.get("applicant.duration_of_each_stay_special",None),

        visa_number_x2=                 postList.get("applicant.visa_number_x2",None),
        once_left_china_x2=             postList.get("applicant.once_left_china_x2",None),
        visa_valid_until_x2=            postList.get("applicant.visa_valid_until_x2",None),
        date_of_departure_x2=           postList.get("applicant.date_of_departure_x2",None),
        date_of_reentry_x2=             postList.get("applicant.date_of_reentry_x2",None),
        duration_of_each_stay_x2=       postList.get("applicant.duration_of_each_stay_x2",None),
        visa_valid_until_final=         visa_valid_until_final,
##########################################################################################################
        student_category=               postList.get("applicant.student_category",None),
        study_duration_start=           postList.get("applicant.study_duration_start",None),
        study_duration_end=             postList.get("applicant.study_duration_end",None),

        tuition_fee_type_language=      postList.get("applicant.tuition_fee_type_language",None),

        tuition_fee_type_selfpaid=      postList.get("applicant.tuition_fee_type_selfpaid",None),
        is_JW202_selfpaid=              postList.get("applicant.is_JW202_selfpaid",None)
    )
    newApt.save()

    return render(request, 'info/submit_result.html', {"postList": postList.items()})

def info_form(request):
    return render(request, 'info/info_form.html',{})

