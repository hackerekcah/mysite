/**
 * @author FBA1B78
 * Passport object for use in individual application
 * 
 */
(function(global) {
	
	global.esta = global.esta || {};
	global.esta.individualApplication = global.esta.individualApplication || {};
	global.esta.individualApplication.passport = function(){
		
		this.NIDCountries = [];
		var hasCheckedIssuanceDate = false;
		var instance = this;
		
		this.setup = function(){
			
			// select countries that require NID
			var optionElements = "#citizenshipCountry option[data-esta-nidrequired='true']";
			
			$( optionElements ).each(function( index ) {
				var nidReq = $(this).attr("data-esta-nidrequired");
				if(nidReq == "true"){
					instance.NIDCountries.push( $(this).val() );
				}
			});
			
			// bind option select events
			$("#citizenshipCountry").on("change", instance.checkNationalID);
			$("#passportCountry").on("change", instance.checkPersonalID);
			if(typeof $("#PptIssueDate").val() !== "undefined"){
				if($("#PptIssueDate").val().length > 0){
					$("[name='passport.whenIssuedDay']").on("blur", instance.checkIssueDate);
					$("[name='passport.whenIssuedMonth']").on("blur", instance.checkIssueDate);
					$("[name='passport.whenIssuedYear']").on("blur", instance.checkIssueDate);
				}
			}
			// if on review page, check ...
			// do a check at the beginning in case it is already filled out
			instance.checkNationalID(null);

		};
		
		this.checkNationalID = function (event) {
		    $("#passportPIN").attr("disabled", true);
		    $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
		    $('#passPin.conditional label').addClass('disabled');
		    $('#passPin.conditional label span').addClass('hide');
		    $('#alertPIN').addClass('hide');

		    var countriesArray = instance.NIDCountries,
		        countryOpt = $('#citizenshipCountry option:selected').val(),
		        issuingOpt = $('#passportCountry option:selected').val();
		    for (index in countriesArray){
		        if($.inArray(countryOpt, countriesArray) != -1) {
		            $("#nationalID").attr("disabled", false);
		            $("#nationalIDTooltip").attr("tabindex", 0).removeClass('hidden');
		            $('#passNIN.conditional label').removeClass('disabled');
		            $('#passNIN.conditional label span').removeClass('hide');

		                // console.log(countryOpt);
		            if (countryOpt == 'TW' || issuingOpt == 'TW') {
		                $("#passportPIN").attr("disabled", false);
		                $("#passportPINTooltip").attr("tabindex", 0).removeClass('hidden');
		                $('#passPin.conditional label').removeClass('disabled');
		                $('#passPin.conditional label span').removeClass('hide');
		                $('#alertPIN').removeClass('hide');
		            } else {
		                $("#passportPIN").attr("disabled", true);
		                $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
		                $('#passPin.conditional label').addClass('disabled');
		                $('#passPin.conditional label span').addClass('hide');
		                $('#alertPIN').addClass('hide');
		            }
		        } else {
		            $("#nationalID").attr("disabled", true).val('');
		            $("#nationalIDTooltip").attr("tabindex", -1).addClass('hidden');
		            $('#passNIN.conditional label').addClass('disabled');
		            $('#passNIN.conditional label span').addClass('hide');
		            if(issuingOpt !== 'TW') {
		                $("#passportPIN").attr("disabled", true).val('');
		                $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
		                $('#passPin.conditional label').addClass('disabled');
		                $('#passPin.conditional label span').addClass('hide');
		                $('#alertPIN').addClass('hide');
		            }
		        }
		    }
		};

		this.checkPersonalID = function (event) {
		        var countryStr = 'TW',
		            countryOpt = $('#passportCountry option:selected').val(),
		            citOpt = $('#citizenshipCountry option:selected').val();
		    if ($("#passportPIN").attr("disabled") == false) {
		        if(countryOpt.indexOf(countryStr) > -1) {
		            $("#passportPIN").attr("disabled", false);
		            $("#passportPINTooltip").attr("tabindex", 0).removeClass('hidden');
		            $('#passPin.conditional label').removeClass('disabled');
		            $('#passPin.conditional label span').removeClass('hide'); 
		            $('#alertPIN').removeClass('hide');               
		        } else {
		            $("#passportPIN").attr("disabled", true).val('');
		            $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
		            $('#passPin.conditional label').addClass('disabled');
		            $('#passPin.conditional label span').addClass('hide'); 
		            $('#alertPIN').addClass('hide');   
		        }                
		    } else {
		        if(countryOpt.indexOf(countryStr) > -1 || citOpt.indexOf(countryStr) > -1) {
		            $("#passportPIN").attr("disabled", false);
		            $("#passportPINTooltip").attr("tabindex", 0).removeClass('hidden');
		            $('#passPin.conditional label').removeClass('disabled');
		            $('#passPin.conditional label span').removeClass('hide'); 
		            $('#alertPIN').removeClass('hide');               
		        } else {
		            $("#passportPIN").attr("disabled", true).val('');
		            $("#passportPINTooltip").attr("tabindex", -1).addClass('hidden');
		            $('#passPin.conditional label').addClass('disabled');
		            $('#passPin.conditional label span').addClass('hide'); 
		            $('#alertPIN').addClass('hide');   
		        }  
		    }
		    
		};
		
		this.checkIssueDate = function(event){
			//<input id="PptIssueDate" name="PptIssueDate" type="hidden" value="20061010"/> 
			//$("#passport.whenIssuedDay")
			//$("#passport.whenIssuedMonth")
			//$("#passport.whenIssuedYear")
			
			var yearMin = Number($("#PptIssueDate").val().substring(0, 4));
			var monthMin = Number($("#PptIssueDate").val().substring(4, 6));
			var dayMin = Number($("#PptIssueDate").val().substring(6, 8));
			
			var day = Number($("[name='passport.whenIssuedDay']").val());
			var month = Number($("[name='passport.whenIssuedMonth']").val());
			var year = Number($("[name='passport.whenIssuedYear']").val());
			
			if(day > 0 && month > 0 && year > 0){
				
				removeIssuanceWarning();
				
				if( yearMin > year ){
					notifyIssuanceWarning("all");
				} else if( yearMin == year ) {
					if(monthMin > month){
						notifyIssuanceWarning("all");
					} else if(monthMin == month){
						if(dayMin > day){
							notifyIssuanceWarning("all");
						} 
					}
				} 
				
			}
			
		};
		
		function removeIssuanceWarning(){
			$("[name='passport.whenIssuedDay']").removeClass("esta-has-errors has-error");
			$("[name='passport.whenIssuedMonth']").removeClass("esta-has-errors has-error");
			$("[name='passport.whenIssuedYear']").removeClass("esta-has-errors has-error");
		}
		
		function notifyIssuanceWarning(highlight){
			
			/* disabled for now
			if(highlight == "day"){
				$("[name='passport.whenIssuedDay']").addClass("esta-has-errors has-error");
			}
			
			if(highlight == "month"){
				$("[name='passport.whenIssuedMonth']").addClass("esta-has-errors has-error");
			}
			
			if(highlight == "year"){
				$("[name='passport.whenIssuedYear']").addClass("esta-has-errors has-error");
			}
			
			if(highlight == "all"){
				$("[name='passport.whenIssuedDay']").addClass("esta-has-errors has-error");
				$("[name='passport.whenIssuedMonth']").addClass("esta-has-errors has-error");
				$("[name='passport.whenIssuedYear']").addClass("esta-has-errors has-error");
			}
			*/
			
			if(!hasCheckedIssuanceDate){
				hasCheckedIssuanceDate = true;
				$("#passportIssueModal").modal();
			}
			
		}
		
	};
	
})(typeof window === 'undefined' ? this : window);