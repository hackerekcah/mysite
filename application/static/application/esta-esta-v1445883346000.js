/* legacy_esta.js */
/* begin addLoadEvent function */
function addLoadEvent(func) {
    var oldonload = window.onload;
        if (typeof window.onload != 'function') {
        window.onload = func;
        } else {
            window.onload = function() {
                if (oldonload) {
                    oldonload();
                }
            func();
         };
      }      
   }      
//addLoadEvent(init);
addLoadEvent(function() {
/* more code to run on page load */ 
//addLoadEvent(openClose);
});
/* end addLoadEvent function */
/* /legacy_esta.js */

/* main template */
visaModalClose = function() {
	$('#visaModalClose').trigger('click');
}

securityModalClose = function() {
	$('#securityModalClose').trigger('click');
}

faqModalClose = function() {
	$('#faqModalClose').trigger('click');
}

faqFooterClick = function(item) {
	$("#estaFAQQuestion").html($("#estaFAQ" + item + "Question").html());
	$("#estaFAQContent").html($("#estaFAQ" + item + "Content").html());
	$("#estaFAQQuestion").focus(); // for css disabled
}
/* /main template */

/**
 * ESTA Team Scripts
 */
$(document).ready(function() {

	// always try to turn on tool tips
	$('[data-toggle="tooltip"]').tooltip();
	
	// The navigation bar stays hidden until the page is loaded to avoid a user
	// clicking on an action before the modal dialog for Security Notification being ready
	$('#navigationBar').removeClass('hidden');

	$('#closeSecurityModal').click(function() {
		//alert('hiding');
		$(".securityModal").modal('hide');
	});

	if (typeof confirmAndContinueLabel === 'undefined') {
		confirmAndContinueLabel = 'CONFIRM & CONTINUE';
	}

	$(".individual-app").click(function() {
		//alert('ind-app');
		$("#submitButton").empty();
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
				'<input type="hidden" name="language" value="en"/>' + 
				'<input type="hidden" name="apply" value="please"/>' +
				'<input type="submit" id="_eventId_apply" name="_eventId_apply" value="' +
				confirmAndContinueLabel +
				'" tabindex="0" ' +
				'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
				'</form>';

		$("#submitButton").append($(formHTML));

	});

	$(".group-app").click(function() {
		var flowExec = $(this).attr('flowExecKey');
		$("#submitButton").remove('input');
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
		'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />' +
		'<input type="hidden" name="applyGrp" value="please"/>' +
		'<input type="submit" id="_eventId_applyGrp" name="_eventId_applyGrp" value="' +
		confirmAndContinueLabel +
		'" tabindex="0" ' +
		'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
		'</form>';
		$("#submitButton").append($(formHTML));
	});

	$(".check-individual-app").click(function() {
		var flowExec = $(this).attr('flowExecKey');
		$("#submitButton").remove('input');
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
			'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />' +
			'<input type="hidden" name="retrieveSingleApplication" value="please"/>' +
			'<input type="submit" id="_eventId_retrieveSingleApplication" name="_eventId_retrieveSingleApplication" value="' +
			confirmAndContinueLabel +
			'" tabindex="0" ' +
			'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
			'</form>';
		$("#submitButton").append($(formHTML));
		
	});

	$(".check-group-app").click(function() {
		$("#submitButton").remove('input');
		var flowExec = $(this).attr('flowExecKey');
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
			'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />' +
			'<input type="hidden" name="retrieveGroupApplication" value="please"/>' +
			'<input type="submit" id="_eventId_retrieveGroupApplication" name="_eventId_retrieveGroupApplication" value="' +
			confirmAndContinueLabel +
			'" tabindex="0" ' +
			'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
			'</form>';
		$("#submitButton").append($(formHTML));
	
	});

	$(".individual-app2").click(function() {
		//alert($(this).attr('flowExecKey'));
		var flowExec = $(this).attr('flowExecKey');
		$("#submitButton").empty();
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
				'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />' +
				'<input type="hidden" name="apply" value="please"/>' +
				'<input type="submit" id="_eventId_apply" name="_eventId_apply" value="' +
				confirmAndContinueLabel +
				'" tabindex="0" ' +
				'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
				'</form>';

		$("#submitButton").append($(formHTML));
	});

	$(".check-individual-app2").click(function() {
		//alert($(this).attr('flowExecKey'));
		var flowExec = $(this).attr('flowExecKey');
		$("#submitButton").empty();
		$("#submitButton").html('');
		var formHTML = '<form id="ETAApplication" action="application.html" method="post">' +
			'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />' +
			'<input type="hidden" name="retrieveSingleApplication" value="please"/>' +
			'<input type="submit" id="_eventId_retrieveSingleApplication" name="_eventId_retrieveSingleApplication" value="' +
			confirmAndContinueLabel +
			'" tabindex="0" ' +
			'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
			'</form>';
		$("#submitButton").append($(formHTML));
	});

    // Setup handler to reset the Yes button on close
    $("#securityModal").on("hidden.bs.modal", function (e) {
    	$("#submitButton").html('');
    });

	
});


// enable console logging
jQuery.log = function( text ){
	if( (window['console'] !== undefined) ){
		console.log( text );
	}
};


/**
 * BA Scripts
 */

    //skip link focus function
	focusIt = function(anchor) {
		$(anchor).focus();
	};

	//resets the menu when window resizes
	$( window ).resize(function() {
		var win_width = $( window ).width();
		if(win_width >= 768 && $('#navbar-menu').attr('aria-expanded', 'true')) {
			$('#navbar-menu').removeClass('in');
		} 
	});

    $(function() {
	    // Progress bar
	    $('.esta-progress .circle.done .label').html('&#10003;');
	
	    //language menu hover
	    var hoverTimeout;
	    var $container = $('.toggle-language');
	    // var $dropmenu = $('.dropdown-menu.language-dropdown');
	    $('.header .button.esta-language').hover(function() {
	        clearTimeout(hoverTimeout);
	        // $dropmenu.addClass('open');
	        $container.addClass('open');
	        $('.button.esta-language').attr('aria-expanded', 'true');
	    }, function() {
	        hoverTimeout = setTimeout(function() {
	            // $dropmenu.removeClass('open');
	        $container.removeClass('open');
	        $('.button.esta-language').attr('aria-expanded', 'false');        
	        }, 800);
	    });
		

        $('.last .language-dropdown li:last-child a').on('blur', function () {
            $container.removeClass('open');
            $('.button.esta-language').attr('aria-expanded', 'false');
        });    	    

	    //smooth scrolling
	    $(function() {
	      $('a[href*=#]:not([href*=#][data-toggle])').on('click', function() {
	        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
	          var target = $(this.hash);
	          if (this.hash.slice(1) != '') {
		          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
		          if (target.length) {
		            $('html,body').animate({
		              scrollTop: target.offset().top
		            }, 500);
		            return false;
		          }
	          }
	        }
	      });
	    });
    });

    // Sets Security Notification button URL path per Applicant status (new) or (returning)
    securityModalClick = function(modal, item) {
    	$(modal + " .modal-footer .esta-button-primary").removeAttr('data-dismiss');

        $(modal + " .modal-footer .esta-button-primary").attr('href', item);
        if (item == '#') $(modal + " .modal-footer .esta-button-primary").attr('data-dismiss', 'modal');

        $(window).off("beforeunload");
    };

    printClick = function(openDialog) {
   	 $("#mainStyle").attr("href", contextPath + "/css/print.css");
        $('body').addClass('print-view');
        //$('.header .language-container.pull-right, .navigation, .homepage-body, .help-floater, .questions-footer, .esta-button-primary, input, select, .print-view .appReview a, .appReviewPrint a, .print-view .appRemove a').addClass('hidden');
        $('.header .language-container.pull-right, .navigation, .homepage-body, .help-floater, .questions-footer, .esta-button-primary, select, .print-view .appReview a, .appReviewPrint a, .print-view .appRemove a').addClass('hidden');
        $('#closePrintDialog').removeClass('hidden');
        $(".faq-hidden").hide();
        //hidee Review text on application review
        $(".faq-body").hide();
        $("#printInstructions").hide();

        // Force the table style of application list to be the one printed
        $("#lgApplicationTable").removeClass('hidden-xs');
        $("#xsApplicationTable").hide();
        $("#xsApplicationTable").removeClass('visible-xs');
        $("#xsApplicationTable").addClass('hidden-print');

        // Expand and then disable accordions in  Print View Application
        $("[data-toggle='collapse']").click();
        $("[data-toggle='collapse']").on('click', function(event){ event.preventDefault(); });
        $("[data-toggle='collapse']").attr("data-untoggle", "");
        $("[data-toggle='collapse']").removeAttr("data-toggle");
        
        // Remove the accordion symbold if it's there
        var bracket = $('#reviewAccordion #applicantLink').text().indexOf("[ ");
        if (bracket != -1) {
    		$('#reviewAccordion #applicantLink').text($('#reviewAccordion #applicantLink').text().substring(6));
        }
    	bracket = $('#reviewAccordion #travelLink').text().indexOf("[ ");
        if (bracket != -1) {
            $('#reviewAccordion #travelLink').text($('#reviewAccordion #travelLink').text().substring(6));
        }
    	bracket = $('#reviewAccordion #eligibilityLink').text().indexOf("[ ");
        if (bracket != -1) {
    		$('#reviewAccordion #eligibilityLink').text($('#reviewAccordion #eligibilityLink').text().substring(6));
        }
		$('#reviewAccordion #verificationLink').hide();
		$('#reviewAccordion #verificationEditContainer').hide();
		

        $('#reviewAccordion').addClass('print-mode');
        if($('.flag-logo.flag-customs')) $('.flag-logo.flag-customs').attr('src', contextPath + '/img/CBPlogo.png');
        if($('.flag-logo.flag-esta')) $('.flag-logo.flag-esta').attr('src', contextPath + '/img/estaPrintLarge.png');
        // Default is to open the dialog unless it's specified as 'false'
        if (openDialog == null || openDialog) {
            window.print();
        }
        return false;
   };

   /*
    * This function reverses the efects fo printClick()
    */
   closePrintClick = function() {
	   location.reload();
	   return false;
  };

    $(function() {
        $('#discAccordion a.accordion-toggle').on('click', function () {
            if ($(this).attr("data-toggle") != 'collapse') return;

            if ($(this).attr("aria-expanded") == 'true') {
                $(this).text("[ + ] " + $(this).text().substring(6));
            } else {
                var self = this;
                $(this).text("[ - ] " + $(this).text().substring(6));
            }
        });

        // Expands first Disclaimer tab panel by default
        $('#discAccordion #disclaimerLink').trigger('click');

        //Enable/Disable "NEXT" Button
        $('#buttonNext').attr('disabled', true);
    });

    validateQuestions = function() {
        if ($('#disclaimerYes').is(":checked") &&
            $('#travelYes').is(":checked")) {
            $('#buttonNext').attr('disabled', false);
        } else {
            $('#buttonNext').attr('disabled', true);
        }
    };

    onDisclaimerYes = function() {
        $('#discAccordion #travelLink').removeClass('disabled').attr('data-toggle', 'collapse').trigger('click');
        focusIt('#travel');
        $('#travel').removeClass('hide');
        $('#discAccordion #disclaimerLink').trigger('click');
        validateQuestions();
        $('input[id="disclaimerYes"]').unbind("click");
        $('input[id="disclaimerNo"]').click(onDisclaimerNo);
    };

    onDisclaimerNo = function() {
        if (!$('#discAccordion #travelLink').hasClass("collapsed")) $('#discAccordion #travelLink').trigger('click');
        $('#discAccordion #travelLink').addClass('disabled');
        $('#discAccordion #travelLink').attr('data-toggle', '');
        $('#buttonNext').attr('disabled', true);
        // $('input[id="disclaimerNo"]').unbind("click");
        $('input[id="disclaimerYes"]').click(onDisclaimerYes);
    };

    onTravelYes = function() {
        focusIt('#buttonNext');
        validateQuestions();
        $('input[id="travelYes"]').unbind("click");
        $('input[id="travelNo"]').click(onTravelNo);
    };

    onTravelNo = function() {
        $('#buttonNext').attr('disabled', true);
        // $('input[id="travelNo"]').unbind("click");
        $('input[id="travelYes"]').click(onTravelYes);
		focusIt('#travel');
    };

    $(function() {
        // YES Conditional field function
        $('input[id="disclaimerYes"]').click(onDisclaimerYes);
        $('input[id="travelYes"]').click(onTravelYes);
        // NO Conditional field function
        $('input[id="disclaimerNo"]').click(function() {
            $('#faqModal').modal('toggle');
        });
        $('input[id="travelNo"]').click(function () {
            $('#faqModal').modal('toggle');
        });

        $('form').trigger('reset');
    });

    //Form exit popup
//    $(window).on('beforeunload', function(event){
//    	// inside onbeforeunload function
//    	if ( /Firefox[\/\s](\d+)/.test(navigator.userAgent) && new Number(RegExp.$1) >= 4) {
//            return("You are now leaving the ESTA Application Process. Your information will not be saved until you have reviewed and submitted your application. Are you sure you want to continue?");
//        }
//    	return "You are now leaving the ESTA Application Process. Your information will not be saved until you have reviewed and submitted your application. Are you sure you want to continue?";
//    });

    exitModalClose = function() {
    	$('#exitModalClose').trigger('click');
    };

//    onLinkClick = function() {
//        $(window).off("beforeunload");
//    };
    
    
    //for Application removal
    $('#removeWarningModal').on('show.bs.modal', function(e) {
        //get data-id attribute of the clicked element
        var bookId = $(e.relatedTarget).data('id');
        var flow = $(e.relatedTarget).data('flow');
        //populate the textbox
        $(e.currentTarget).find('input[name="id"]').val(bookId);
        $(e.currentTarget).find('input[name="flow"]').val(flow);
    });
    
    //trigger removal hyperlink
    $('#yesRemove').on('click',function(e){
    	var id = $('input[name="id"]' ).val();
    	var flow = $('input[name="flow"]' ).val();
    	var part = flow+"&_eventId=remove&updateApplTrackingID="+id;
    	//construct the hyperlink and trigger it for removal
    	$(location).attr('href', part);
    	//window.location.href="http://localhost:7001/esta/application.html";
    });
    
    
/**
* HELP floater hide function
* hides the "Need Help" link near bottom of page
*/
(function(global, $){
	
	var helpElement = $("#HELP").get(0) || $("[name='HELP']").get(0);
	var helpOffset = 150;
	
	// page in pixels where "floater" is hidden
	var offset_hide = (typeof helpElement === 'undefined') ? 750 : getOffset(helpElement).top - helpOffset; 
	var $help_float = $('.help-floater');

	$(global).scroll(function() {
		if ($(this).scrollTop() > offset_hide) {
			$help_float.addClass('hide');
		} else {
			$help_float.removeClass('hide'); // "redisplays" button when
												// scrolling back up
		}
	});
	
	function getOffset(elem) {
		if (elem.getBoundingClientRect) {
			return getOffsetRect(elem)
		} else { // old browser
			return getOffsetSum(elem)
		}
	}
	
	function getOffsetSum(elem) {
	  var top=0, left=0
	 
	  while(elem) {
		top = top + parseInt(elem.offsetTop)
		left = left + parseInt(elem.offsetLeft)
		elem = elem.offsetParent       
	  }
		
	  return {top: top, left: left}
	}
	
	function getOffsetRect(elem) {
		
		// (1)
		var box = elem.getBoundingClientRect()
		 
		var body = document.body
		var docElem = document.documentElement
		 
		// (2)
		var scrollTop = global.pageYOffset || docElem.scrollTop || body.scrollTop
		var scrollLeft = global.pageXOffset || docElem.scrollLeft || body.scrollLeft
		 
		// (3)
		var clientTop = docElem.clientTop || body.clientTop || 0
		var clientLeft = docElem.clientLeft || body.clientLeft || 0
		 
		// (4)
		var top  = box.top +  scrollTop - clientTop
		var left = box.left + scrollLeft - clientLeft
		 
		return { top: Math.round(top), left: Math.round(left) }
		
	}
	
})(typeof window === 'undefined' ? this : window, jQuery);


/**
* Keyboard navigation for accessibility
* @param window 
* @param esta 
* @param $ 
*/
(function(window, esta, $){
	
	esta.accessibility = esta.accessibility || {};
	esta.accessibility.$lastFocused = esta.accessibility.$lastFocused || {};
	esta.accessibility.Keyboard = function(){
	
		var instance = this;
		var isMobileMode; // will be set to boolean value later on, undefined for startup
		var isLanguageMenuExpanded;
		var $lastFocusItem;
		
		this.setup = function(){
		
			setupSkipToMainContent();
			setupMainMenu();
			
		};
		
		function setupMainMenu(){
		
			// keyboard accessibility, main menu flyout on focus and blur
			$("#dropdownMain1").focus(function(event){
				$("#apply_link").addClass("open");
				$("#check_link").removeClass("open");
			});
			$("#dropdownMain2").focus(function(event){
				$("#apply_link").removeClass("open");
				$("#check_link").addClass("open");
			});
			
			$("#homeMenu").focus(function(event){
				$("#apply_link").removeClass("open");
			});
			$("#faqMenu").focus(function(event){
				$("#check_link").removeClass("open");
			});
			
			$("#mobile-navbar-menu").focus(function(event){
				$("#mobile-navbar-menu").click();
				closeLanguageMenu();
			});
			
			// language menu
			$("#languageDrop").keypress(function(event){
				if(event.key == "Enter"){
					$(this).click();
				}
				isLanguageMenuExpanded = $("#languageDrop").attr("aria-expanded");
			});
			
			$("#languageDropMobile").focus(function(event){
				closeLanguageMenu();
			});
			
			$("#languageDropMobile").keypress(function(event){
				if(event.key == "Enter"){
					$(this).click();
				}
				isLanguageMenuExpanded = $("#languageDrop").attr("aria-expanded");
			});
			$("#cbpSiteLink").focus(function(event){
				closeLanguageMenu();
			});
			$("#skippy").focus(function(event){
				closeLanguageMenu();
			});
			$("#content").focus(function(event){
				closeLanguageMenu();
				$('#navbar-menu').removeClass('in');
			});

			// if zoom gets too large or screen too small, 
			// the smaller menu needs to be tabindexable
			$(window).resize(onWindowResize);
			
			onWindowResize(); // kick off on first load
			
		}
		
		function closeLanguageMenu(){
			if(isLanguageMenuExpanded){
				if(isMobileMode){
					$("#languageDropMobile").parent().removeClass("open");
					$("#languageDropMobile").attr("aria-expanded", false);
				} else {
					$("#languageDrop").parent().removeClass("open");
					$("#languageDrop").attr("aria-expanded", false);
				}
				isLanguageMenuExpanded = false;
			}
		}
		
		function closeMobileMenu(){
			if(isMobileMode){
				$("#languageDropMobile").parent().removeClass("open");
				$("#languageDropMobile").attr("aria-expanded", false);
			}
		}
		
		function onWindowResize(event){
		
			//resets the menu when window resizes
			
			var DESKTOP_SIZE_MINIMUM = 768;
			var width = $( window ).width();
			
			if(width < DESKTOP_SIZE_MINIMUM && isMobileMode == false){
				isMobileMode = true;
				enableMainMenuTabIndexFor("mobile");
			} else if(width > DESKTOP_SIZE_MINIMUM && (isMobileMode == true || typeof isMobileMode === "undefined")) {
				isMobileMode = false;
				enableMainMenuTabIndexFor("desktop");
			}
			
		}
		
		function setupSkipToMainContent(){
			$("#skippy").click(function(event){
				event.preventDefault();
				$("#content").focus();
			});
		}
		
		function enableMainMenuTabIndexFor(menuItem){
			if(menuItem == "mobile"){
				// enable mobile menu tabindex, disable desktop
				$("#navbar-menu").attr("tabindex", "-1");
				$("#mobile-navbar-menu").attr("tabindex", "0");
				//esta.log.comment("enabling tabindex for mobile menu");
			} else {
				// enable desktop menu tabindex, disable mobile
				$("#navbar-menu").attr("tabindex", "0");
				$("#mobile-navbar-menu").attr("tabindex", "-1");
				//esta.log.comment("enabling tabindex for desktop menu");
			}
		}
		
		this.getStatus = function(){
			var str = "Accessibility mode enabled\n";
			if(isMobileMode){
				str += "Keyboard for mobile sized screen";
			} else {
				str += "Keyboard for desktop sized screen";
			}
			esta.log.comment(str);
		};
		
		
		
	};
	
})(typeof window === 'undefined' ? this : window, esta, jQuery);

/**
 * Stylesheet monitor for when CSS file is disabled
 * watches for computed style signature to detect change 
 * @param esta
 * @param $
 */
(function(esta, $){

	/**
	* broadcasts:
	*   esta.events.css.STYLES_DISABLED,
	*   esta.events.css.STYLES_ENABLED
	* disabled will always get broadcasted first followed by enabled if styles come back. 
	*/
	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.CSSMonitor = function() {
		
		var isMonitoring = false;
		var isCSSEnabled = true;
		
		var INTERVAL = 1000;
		var STYLES_DISABLED = esta.events.css.STYLES_DISABLED;
		var STYLES_ENABLED = esta.events.css.STYLES_ENABLED;
		
		var instance = this;
		
		this.isRunning = function(){
			return isMonitoring;
		}
		
		this.isCSSEnabled = function(){
			return isCSSEnabled;
		}
		
		this.start = function(){
			
			if(isMonitoring == false){
				monitorStyleChange();
				isMonitoring = true;
			}
			
		};
		
		function monitorStyleChange(){
			$(document).on(STYLES_DISABLED, onStylesDisabled); // debug binding
			$(document).on(STYLES_ENABLED, onStylesEnabled); // debug binding
			setInterval(function(){ checkForStyleChange() }, INTERVAL);
		}
		
		function checkForStyleChange() {
			
			// computed style features 
			var bodyBoxSizing = $("body").css("box-sizing"); // border-box
			var bodyOverflowX = $("body").css("overflow-x"); // hidden
			var languageNavCursor = $("#languageDrop").css("cursor"); // pointer
			var languageNavDisplay = $("#languageDrop").css("display"); // inline-block
			
			var documentHasEstaCssFeatures = (bodyBoxSizing == "border-box") && (bodyOverflowX == "hidden") && (languageNavCursor == "pointer") && (languageNavDisplay == "inline-block");
			
			if(documentHasEstaCssFeatures == true && isCSSEnabled == false){ 
				$.event.trigger(STYLES_ENABLED); // trigger once
			} else if(documentHasEstaCssFeatures == false && isCSSEnabled == true) {
				$.event.trigger(STYLES_DISABLED); // trigger once
			} 
			
			isCSSEnabled = documentHasEstaCssFeatures;
			
		}
		
		function onStylesEnabled(event){
			esta.log.warning("onStylesEnabled", instance);
		}
		
		function onStylesDisabled(event){
			esta.log.warning("onStylesDisabled", instance);
		}
		
		return this;
		
	};
	
})(esta, jQuery);

/**
 * CSS Disabled Header
 * Global fixes when stylesheets/css are disabled/enabled
 * 
 */
(function(esta, $){

	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.Header = function(){
		
		var $navbar;
		var $cbpLogoLg;
		var $estaLogoLgWhite;
		var instance = this;
		
		this.setup = function(){
			setupStyleChangEventListener();
		};
		
		function setupStyleChangEventListener(){
			$(document).on(esta.events.css.STYLES_DISABLED, function(){
				instance.renderDisabled();
			});
			$(document).on(esta.events.css.STYLES_ENABLED, function(){
				instance.renderEnabled();
			});
		}
	
		this.renderDisabled = function(){
			$navbar = $("#navigationBar .language-header").detach();
			$cbpLogo = $("#CBPLogoLg").detach();
			$estaLogoLgWhite = $("#ESTALogoLgWhite").detach();
		};
		
		this.renderEnabled = function(){
			$navbar.appendTo("#navigationBar");
			$cbpLogo.appendTo("#logoGroup");
			$estaLogoLgWhite.appendTo("#logoGroup");
		};
		
	}
	
})(esta, jQuery);

/**
 * CSS Disabled Tooltips
 * Global fixes when stylesheets/css are disabled/enabled
 * 
 */
(function(esta, $){

	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.Tooltips = function(){

		var instance = this;
		
		this.setup = function(){
			setupStyleChangEventListener();
		};
		
		function setupStyleChangEventListener(){
			$(document).on(esta.events.css.STYLES_DISABLED, function(){
				instance.renderDisabled();
			});
			$(document).on(esta.events.css.STYLES_ENABLED, function(){
				instance.renderEnabled();
			});
		}
	
		this.renderDisabled = function(){
			$("[data-original-title]").each(function(index, element){
				$(element).on("show.bs.tooltip", instance.onPreventTooltip);
				var tooltip = $(element).attr("data-original-title");
				var tooltipHTML = "<p class=\"exposed-tool-tip\">"+tooltip+"</p>";
				$(element).prepend(tooltipHTML);
			});
		};
		
		this.renderEnabled = function(){
			$("[data-original-title]").each(function(index, element){
				$(element).off("show.bs.tooltip", instance.onPreventTooltip);
				$(element).find(".exposed-tool-tip").remove();
			});
		};
		
		this.onPreventTooltip = function(event){
			event.preventDefault();
		};
		
	}
	
})(esta, jQuery);

/**
 * CSS Disabled Accordions
 * Global fixes when stylesheets/css are disabled/enabled
 * 
 */
(function(esta, $){

	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.Accordions = function(){
		
		var styledElementsArray = [];
		var instance = this;
		
		this.setup = function(){
			setupStyleChangEventListener();
		};
		
		function setupStyleChangEventListener(){
			$(document).on(esta.events.css.STYLES_DISABLED, function(){
				instance.renderDisabled();
			});
			$(document).on(esta.events.css.STYLES_ENABLED, function(){
				instance.renderEnabled();
			});
		}
	
		this.renderDisabled = function(){
		
			styledElementsArray = [];
			
			// remove any accordion elements that have set style="height:0"
			// but record it for restoration later
			$(".accordion").find("[style]").each(function(index, element){
				var el = {element: element, style: $(element).attr("style")};
				styledElementsArray.push(el);
				$(element).removeAttr("style");
			});
			
			// lock them from being triggered directly
			$(".accordion-toggle").each(function(index, element){
				$(element).attr("data-toggle", "");
				$(element).on("click", instance.onPreventAccordion);
				$(element).on("show.bs.tooltip", instance.onPreventAccordion);
				$(element).on("hide.bs.tooltip", instance.onPreventAccordion);
			});
			
		};
		
		this.renderEnabled = function(){
			
			// restore the style
			styledElementsArray.forEach(function(item, index, array){
				$(item.element).attr("style", item.style);
			});
			
			// lock them from being triggered directly
			$(".accordion-toggle").each(function(index, element){
				$(element).attr("data-toggle", "collapse");
				$(element).off("click", instance.onPreventAccordion);
				$(element).off("show.bs.tooltip", instance.onPreventAccordion);
				$(element).off("hide.bs.tooltip", instance.onPreventAccordion);
			});
			
		};
		
		this.onPreventAccordion = function(event){
			event.preventDefault();
			$(event.currentTarget).removeAttr("style");
		};
		
	}
	
})(esta, jQuery);

/**
 * Focus history singleton
 * (always on in case users switch to and from css disabled)
 * 
 */
(function(global, esta, $){

	esta.accessibility = esta.accessibility || {};
	esta.accessibility.FocusHistory = esta.accessibility.FocusHistory || new function(){
		
		var HISTORY_THRESHOLD = 100;
		var defaultFocusElement;
		var historyArray = [];
		var lastFocusedElement;
		var lastReachableFocusedElement;
		var instance = this;

		$(global.document).ready(function(event){
		
			defaultFocusElement = $("#skippy").get(0) || $("body").get(0);
			
			$("a").on("focus", instance.onFocus);
			$("button").on("focus", instance.onFocus);
			
			$("input").on("focus", instance.onFocus);
			$("option").on("focus", instance.onFocus);
			$("select").on("focus", instance.onFocus);
			$("textarea").on("focus", instance.onFocus);
			
			$("div[tabindex='0']").on("focus", instance.onFocus);
			$("span[tabindex='0']").on("focus", instance.onFocus);
			
		});
		
		this.onFocus = function(event){
			//esta.log.comment("on focus");
			//esta.log.comment(event.currentTarget);
			lastFocusedElement = event.currentTarget;
			recordFocus(lastFocusedElement);
		};
		
		function recordFocus(element){
			historyArray.push(lastFocusedElement);
			if(historyArray.length > HISTORY_THRESHOLD){
				historyArray.shift();
			}
		}
		
		/**
		* If tab index is not -1
		*/
		this.getLastReachableElement = function(){
		
			if(defaultFocusElement === "undefined"){ throw "defaultFocusElement is undefined"; }
			lastReachableFocusedElement = defaultFocusElement; 
			
			for(var i = historyArray.length - 1; i >= 0; i--){
				var item = historyArray[i];
				if(typeof item !== "undefined"){
					if($(item).length > 0){
						var tabindexValue = $(item).attr("tabindex");
						if(tabindexValue != "-1"){
							lastReachableFocusedElement = item;
							break;
						}
					}
				}
			}
			
			return lastReachableFocusedElement;
			
		};
		
		this.getLastElement = function(){
			if(typeof lastFocusedElement === "undefined"){
				if(defaultFocusElement === "undefined"){ throw "defaultFocusElement is undefined"; }
				lastFocusedElement = defaultFocusElement; 
			} 
			return lastFocusedElement;
		};
		
		this.getHistoryArray = function(){
			return historyArray.slice();
		}
		
		return instance;
		
	};
	
})(typeof window === 'undefined' ? this : window, esta, jQuery);

/**
 * CSS Disabled Modals
 * Global fixes when stylesheets/css are disabled/enabled
 * 
 */
(function(esta, $){

	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.Modals = function(){
		
		var instance = this;
		var $lastFocusBeforeModalFocus;
		var $lastModal;
		
		this.setup = function(){
			setupStyleChangEventListener();
			setupListenersForModals();
		};
		
		function setupStyleChangEventListener(){
			$(document).on(esta.events.css.STYLES_DISABLED, function(){
				instance.renderDisabled();
			});
			$(document).on(esta.events.css.STYLES_ENABLED, function(){
				instance.renderEnabled();
			});
		}
	
		this.renderDisabled = function(){
		
			$(".modal").each(function(index, element){
				$(element).on("show.bs.modal", instance.onPreventModal);
				$(element).on("shown.bs.modal", instance.onPreventModal);
				$(element).on("hide.bs.modal", instance.onPreventModal);
				$(element).on("hidden.bs.modal", instance.onPreventModal);
				$(element).on("loaded.bs.modal", instance.onPreventModal);
			});
			
			$("[data-dismiss='modal']").each(function(index, element){
				$(element).on("click", instance.onDismissModal);
			});
			
			$(".modal").each(function(index, element){
				enableTabIndexesForModal(element, false);
			});
			
		};
		
		/**
		* remove tab traps
		* now that display:none is no longer valid as a way to prevent keyboard focus, 
		* we need to remove child tabindexes=0 to -1 in parent -1 containers
		* and then set them back later
		*/
		function enableTabIndexesForModal(modal, enable){
			
			var tabindexValue = enable ? "0" : "-1";
			
			// <a> has a default implicit tabindex of 0
			$(modal).find("a").each(function(index, focusableElement){
				$(focusableElement).attr("tabindex", tabindexValue); // remove child from focus
			});
			// <button> has a default implicit tabindex of 0
			$(modal).find("button").each(function(index, focusableElement){
				$(focusableElement).attr("tabindex", tabindexValue); // remove child from focus
			});
			$(modal).find("[tabindex='0']").each(function(index, focusableElement){
				$(focusableElement).attr("tabindex", tabindexValue); // remove child from focus
			});
			
		}
		
		this.renderEnabled = function(){
		
			$(".modal").each(function(index, element){
				$(element).off("show.bs.modal", instance.onPreventModal);
				$(element).off("shown.bs.modal", instance.onPreventModal);
				$(element).off("hide.bs.modal", instance.onPreventModal);
				$(element).off("hidden.bs.modal", instance.onPreventModal);
				$(element).off("loaded.bs.modal", instance.onPreventModal);
			});
			
			$("[data-dismiss='modal']").each(function(index, element){
				$(element).off("click", instance.onDismissModal);
			});
			
			$(".modal").each(function(index, element){
				enableTabIndexesForModal(element, true);
			});
			
		};
		
		// get out of modal traps
		this.onDismissModal = function(event){
		
			// remove tab trap
			enableTabIndexesForModal($lastModal, false);
			
			var lastFocusable = esta.accessibility.FocusHistory.getLastReachableElement();
			//esta.log.comment(lastFocusable);
			$(lastFocusable).focus();
			
		};
		
		this.onPreventModal = function(event){
			event.preventDefault();
			var modalElement = event.currentTarget;
			$lastModal = $(modalElement);
			$lastModal.focus(); 
			$lastModal.attr("style", "");
			enableTabIndexesForModal(modalElement, true);
		};
		
		
		function setupListenersForModals(){
			// Modal focus tab function call	
			$('#passportModal').keydown(function(event) {
				trapTabKey($(this), event);
			});
			$('#visaModal').keydown(function(event) {
				trapTabKey($(this), event);
			});
			$('#securityModal').keydown(function(event) {
				trapTabKey($(this), event);
			});
			$('#restartModal').keydown(function(event) {
				trapTabKey($(this), event);
			});
			
			$('#faqModal').keydown(function(event) {
				trapTabKey($(this), event);
			});
			$('#eligibilityModal').keydown(function(event) {
				trapTabKey($(this), event);
			});    
			$('#warningModal').keydown(function(event) {
				trapTabKey($(this), event);
			}); 
			
			//ignores modals when CSS is disabled
			$('.modal').on('hidden.bs.modal', function() {
				var modalWrap = $(this).attr('id');
				$('#' + modalWrap).addClass('disabled');
				$('#' + modalWrap + ' .close-btn').attr('tabindex', -1);
			});
			//enables modals when modal is actived
			$('.modal').on('show.bs.modal', function() {
				var modalWrap = $(this).attr('id');
				$('#' + modalWrap).removeClass('disabled');
				$('#' + modalWrap + ' .close-btn').attr('tabindex', 0);
			});
			//sets initial tabindex of buttons/resets "key trap"
			$('.modal').each(function() {
				var modalWrap = $(this).attr('id');
				$('#' + modalWrap + '.disabled .close-btn').attr('tabindex', -1);
				$('#' + modalWrap + ' .close-btn').on('click', function() {
					$('#' + modalWrap).attr('style', 'display:none');
				});
			});
			
		}
		
		function trapTabKey(obj, evt) {
		
			// jQuery formatted selector to search for focusable items
			var focusableElementsString = "a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, *[tabindex], *[contenteditable]";


			// if tab or shift-tab pressed
			if (evt.which == 9) {
				// get list of all children elements in given object
				var o = obj.find('*');

				// get list of focusable items
				var focusableItems;
				focusableItems = o.filter(focusableElementsString).filter(':visible');

				// get currently focused item
				var focusedItem;
				focusedItem = $(':focus');

				// get the number of focusable items
				var numberOfFocusableItems;
				numberOfFocusableItems = focusableItems.length

				// get the index of the currently focused item
				var focusedItemIndex;
				focusedItemIndex = focusableItems.index(focusedItem);

				if (evt.shiftKey) {
					//back tab
					// if focused on first item and user preses back-tab, go to the last focusable item
					if (focusedItemIndex == 0) {
						focusableItems.get(numberOfFocusableItems - 1).focus();
						evt.preventDefault();
					}

				} else {
					//forward tab
					// if focused on the last item and user preses tab, go to the first focusable item
					if (focusedItemIndex == numberOfFocusableItems - 1) {
						focusableItems.get(0).focus();
						evt.preventDefault();
					}
				}
			}
		}
		
		
		
	}
	
})(esta, jQuery);

/**
 * CSS Disabled Review Page
 * Global fixes when stylesheets/css are disabled/enabled
 * 
 */
(function(esta, $){
	
	esta.accessibility = esta.accessibility || {};
	esta.accessibility.styles = esta.accessibility.styles || {};
	esta.accessibility.styles.ReviewPage = function(){
		
		var hiddenItemsArray = [];
		var instance = this;
		
		this.setup = function(){
			setupStyleChangEventListener();
		};
		
		function setupStyleChangEventListener(){
			$(document).on(esta.events.css.STYLES_DISABLED, function(){
				if(esta.pageId == "reviewApplication"){
					instance.renderDisabled();
				}
			});
			$(document).on(esta.events.css.STYLES_ENABLED, function(){
				if(esta.pageId == "reviewApplication"){
					instance.renderEnabled();
				}
			});
		}
	
		this.renderDisabled = function(){
		
			
		
			$("#reviewAccordion").find(".hidden-xs").each(function(index, item){
				var record = {element: item, contents: $(item).clone(true).html()};
				 $(item).html(''); // clear it out so it doesn't appear
				hiddenItemsArray.push(record);
			});
			$("#reviewAccordion").find("button[tabindex='-1'][readonly='readonly']").each(function(index, item){
				var record = {element: item, contents: $(item).clone(true).html()};
				 $(item).html(''); // clear it out so it doesn't appear
				 $(item).attr("style", "display:none"); // try to hide remnants 
				hiddenItemsArray.push(record);
			});
			
			if(typeof updateReviewedState !== "undefined"){
				updateReviewedState();
			}
			
		};

		this.renderEnabled = function(){
		
			hiddenItemsArray.forEach(function(item){
				$(item.element).html(item.contents); // stuff it back in
				// remove display none from button readonly types
				var styleValue = $(item.element).attr("style");
				if(styleValue == "display:none"){
					$(item.element).removeAttr("style");
				}
			});
			
			hiddenItemsArray = [];
			
			if(typeof updateReviewedState !== "undefined"){
				updateReviewedState();
			}
			
		};
		
	};
	
})(esta, jQuery);

$(document).ready(function(event){
	// 
	var keyboard = new esta.accessibility.Keyboard();
	keyboard.setup();
	//
	var stylesMonitor = new esta.accessibility.styles.CSSMonitor();
	stylesMonitor.start();
	//
	var stylesChangedHeader = new esta.accessibility.styles.Header();
	stylesChangedHeader.setup();
	//
	var stylesChangedTooltips = new esta.accessibility.styles.Tooltips();
	stylesChangedTooltips.setup();
	//
	var stylesChangedAccordions = new esta.accessibility.styles.Accordions();
	stylesChangedAccordions.setup();
	//
	var stylesModals = new esta.accessibility.styles.Modals();
	stylesModals.setup();
	//
	var stylesReviewPage = new esta.accessibility.styles.ReviewPage();
	stylesReviewPage.setup();
	//
	/**
	* From skip-link.js
	*/
	var userAgent = navigator.userAgent.toLowerCase(),
        is_webkit = userAgent.indexOf( 'webkit' ) > -1,
        is_opera = userAgent.indexOf( 'opera' ) > -1,
        is_ie = userAgent.indexOf( 'msie' ) > -1 || userAgent.indexOf( 'trident' ) > -1;

    if (document.getElementById && window.addEventListener ) {
        window.addEventListener( 'hashchange', function() {
		
			esta.log.comment("skip-link.js hashchange");
            var element = document.getElementById( location.hash.substring( 1 ) );

            function cleanup() {
                element.removeAttribute('tabindex');
                element.removeEventListener( 'blur', cleanup, false );
            }

            if (element) {
                if (!( /^(?:a|select|input|button|textarea)$/i.test(element.tagName) || element.hasAttribute( 'tabindex' ))) {
                    element.tabIndex = -1;
                    element.addEventListener( 'blur', cleanup, false );
                }

                element.focus();
            }
        }, false );
    }
	
	// force modals to end
	//if(esta.pageId == "siteFAQ"){
		var $securityModal = $("#securityModal").detach();
		var $restartModal = $("#restartModal").detach();
		$("body").append($securityModal);
		if($restartModal.length > 0){ $("body").append($restartModal); }
	//}
	
	// prevent paste on group app
	$('*[name="groupContact.confirmEmailAddress"]').bind("paste", function(event) {
		event.preventDefault();
	});
	
	
});
	