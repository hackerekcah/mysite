// disables form on initial load
$(window).load(function() {
    $('.conditional label').addClass('disabled');
    $('.conditional label span').addClass('hide');
    $("#listAliases .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
    enableDisableAlias();
    $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
    $("#nationalIDTooltip").attr("tabindex", -1).addClass('hidden');
    //$("#aliasesLastNameTooltip").attr("tabindex", -1).addClass('hidden');
    //$("#aliasesFirstNameTooltip").attr("tabindex", -1).addClass('hidden');
    $("#citizenshipMultiInfo .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
    //$("#otherCitizenCntryOfIssueTooltip").attr("tabindex", -1).addClass('hidden');
    //$("#otherCitizenPssprtNumberTooltip").attr("tabindex", -1).addClass('hidden');
    
    enableCitizenshipMultiInfo();
    checkPhoneNumberCount();
    //$("#citizenshipMultiInfo .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
    enableEmploymentInfo();
    var passport = new esta.individualApplication.passport();
    passport.setup();
    $("#employmentInfo .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
	// prevent paste into email confirm
	$('#emailAddress2').bind("paste",function(event) {
		event.preventDefault();
	});

});

resetTooltips = function() {
    $('[data-toggle="tooltip"]').tooltip();
}

/*
//Year
getYear = function(select, min, max) {
    var selectList = '#' + select;
    var year = new Date().getFullYear();
    var html = '<option></option>';
    var offsetmin = year - min;
    var offsetmax = year + max;
    
    if(offsetmax <= year) {
        for(var i = year; i >= offsetmin; i--) {
          html = '<option value="' + i + '">' + i + '</option>';
          $(selectList).append(html);  
        }
        $(selectList).unbind("click");
    } else {
        for(var i = offsetmax;  i >= offsetmin; i--) {
          html = '<option value="' + i + '">' + i + '</option>';
          $(selectList).append(html);  
        }
        $(selectList).unbind("click");
    }
}
$(function() {
    getYear('dobYear', 125, 0);
    getYear('passportIssueYear', 10, 0);
    getYear('expirationYear', 0, 11);
})
*/

//Enable/Disable "NEXT" Button
// $('#buttonNext').attr('disabled', true);


addAnother = function (item, max, fields) {
    var addGroup = $('.add-to-' + item + ' .add-to').last();
    if ($('.' + item + 'Set').length < max) {
        var groupClone = addGroup.clone();
        groupClone.insertAfter(addGroup);
        
        var lastInput = groupClone.find(".col-sm-5").last();
        // add minus button
        var hasMinus = groupClone.find(".col-sm-2");
        console.log(hasMinus.length);
        if(hasMinus.length == 0){
        	$('<div class="col-sm-2 form-group"><a class="btn btn-danger esta-btn-remove"><span class="glyphicon glyphicon-minus" aria-hidden="true"></span> </a></div>').insertAfter(lastInput);
        }
        
        $(".esta-btn-remove").on("click", function(){
        	$(this).parents(".add-to").remove();
        });
        
        var count = $('.' + item + 'Set').length;
        $('.' + item + "Set").last().attr("id", item + count);

        for (var i = 0; i < fields.length; i++) {
            var field = fields[i];
            $('.' + field + 'Label').last().attr("for", field + count);
            $('.' + field).last().attr("id", field + count);
            $('.' + field).last().val("");
        }

        resetTooltips();
        return false;
    }
};

onAliasChange = function() {
	aliasCount = $(".aliasesSet").children().length;
    if ($("#otherNames").val() == "Y") {
        $(".familyNameAlias").attr("disabled", false);
        $(".givenNameAlias").attr("disabled", false);
        if (aliasCount >= 10)
        	$("#aliasAdd").attr("disabled", true);
        else
        	$("#aliasAdd").attr("disabled", false);
        $("#listAliases .tooltip-trigger.conditional").attr("tabindex", 0).removeClass('hidden');
        $('#listAliases .conditional label').removeClass('disabled');
        $('#listAliases .conditional label span').removeClass('hide');
    } else {
        if ($("#otherNames").val() == "N") {
        	//$(".aliasesSet").children().remove();
            $(".familyNameAlias").attr("disabled", true);
            $(".givenNameAlias").attr("disabled", true);
            $("#aliasAdd").attr("disabled", true);
            $("#listAliases .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
            $('#listAliases .conditional label').addClass('disabled');
            $('#listAliases .conditional label span').addClass('hide');
        }
    }
};


onMultiCitizenChange = function() {
	citizenshipCount = $(".citizenshipSet > div").length / 2;
    if ($("#haveMultipleCitizenship").val() == "Y") {
        $(".citizenshipCountryMultiple").attr("disabled", false);
        $(".passportNumberMultiple").attr("disabled", false);
        if (citizenshipCount >= 4)
        	$("#passportAdd").attr("disabled", true);
        else
        	$("#passportAdd").attr("disabled", false);
        $("#citizenshipMultiInfo .tooltip-trigger.conditional").attr("tabindex", 0).removeClass('hidden');
        $('#citizenshipMultiInfo .conditional label').removeClass('disabled');
        $('#citizenshipMultiInfo .conditional label span').removeClass('hide');
    } else {
        if ($("#haveMultipleCitizenship").val() == "N") {
            $(".citizenshipCountryMultiple").attr("disabled", true).val('');
            $(".passportNumberMultiple").attr("disabled", true).val('');
            $("#passportAdd").attr("disabled", true);
            $("#citizenshipMultiInfo .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
            $('#citizenshipMultiInfo .conditional label').addClass('disabled');
            $('#citizenshipMultiInfo .conditional label span').addClass('hide');
        }
    }
}

onEmploymentChange = function() {
    if ($("#haveEmployer").val() == "Y") {
        $("#employmentTitle").attr("disabled", false);
        $("#employmentName").attr("disabled", false);
        $("#employmentAddressOne").attr("disabled", false);
        $("#employmentAddressTwo").attr("disabled", false);
        $("#employmentAddressCity").attr("disabled", false);
        $("#employmentAddressState").attr("disabled", false);
        $("#employmentAddressCountry").attr("disabled", false);
        $("#employmentPhonePhoneType").attr("disabled", false);
        $("#employmentPhoneCountry").attr("disabled", false);
        $("#employmentPhone").attr("disabled", false);
        $("#employmentInfo .tooltip-trigger.conditional").attr("tabindex", 0).removeClass('hidden');
        $('#employmentInfo .conditional label').removeClass('disabled');
        $('#employmentInfo .conditional label span').removeClass('hide');
    } else {
        if ($("#haveEmployer").val() == "N") {
            $("#employmentTitle").attr("disabled", true).val('');
            $("#employmentName").attr("disabled", true).val('');
            $("#employmentAddressOne").attr("disabled", true).val('');
            $("#employmentAddressTwo").attr("disabled", true).val('');
            $("#employmentAddressCity").attr("disabled", true).val('');
            $("#employmentAddressState").attr("disabled", true).val('');
            $("#employmentAddressCountry").attr("disabled", true).val('');
            $("#employmentPhonePhoneType").attr('disabled', true).val('');
            $("#employmentPhoneCountry").attr("disabled", true).val('');
            $("#employmentPhone").attr("disabled", true).val('');
            $("#employmentInfo .tooltip-trigger.conditional").attr("tabindex", -1).addClass('hidden');
            $('#employmentInfo .conditional label').addClass('disabled');
            $('#employmentInfo .conditional label span').addClass('hide');
        }

    }
}

visaModalClose = function() {
    $('#visaModalClose').trigger('click');
}

faqModalClose = function() {
    $('#faqModalClose').trigger('click');
}

faqFooterClick = function(item) {
    $("#estaFAQQuestion").html($("#estaFAQ" + item + "Question").html());
    $("#estaFAQContent").html($("#estaFAQ" + item + "Content").html());
}


// sets form timer
var idleSeconds = 900;

$(function(){
  var idleTimer;
  function resetTimer(){
    clearTimeout(idleTimer);
    idleTimer = setTimeout(formIdle,idleSeconds*1000);
  }
  $(document.body).bind('mousemove,keydown,click',resetTimer);
  resetTimer(); // Start the timer when the page loads
});

formIdle = function (){
  alert('Your session is about to timeout. Please click OK if you need more time.');
}


$(function(){
    $('form').trigger('reset');
});

$(window).unload(function() {
    $('.disabled').removeAttr('disabled');
    $("#nationalID").attr("disabled", true);
    $("#passportPIN").attr("disabled", true);
    $('#employmentInfo .conditional input').attr('disabled', true);
    $('#employmentInfo .conditional select').attr('disabled', true);
    $('.add-to-citizenship input').attr('disabled', true)
    $('.add-to-citizenship select').attr('disabled', true);
    $('.add-to-aliases input').attr('disabled', true)
});


showLastNameError = function() {
	alert('showLastNameError');
	$(".lastNameHasErr").addClass('has-error');
	
}

