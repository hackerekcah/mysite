function unsavedWorkModalClick() {
    // remove  data-target from menu item so it does not trigger the disclaimer modal
	$(this).removeAttr("data-target");
	var flowExec = $(this).attr('flowExecKey');
	if (null == flowExec) {
		flowExec = $("[name=_flowExecutionKey]").val();
	}
	var newFlow = false;
	$("#restartModal .modal-footer .esta-button-primary").empty();
	$("#restartModal .modal-footer .esta-button-primary").html('');	
	var myEventId = "home";
	if ($(this).hasClass("individual-app") || $(this).hasClass("individual-app2")) {
		myEventId = "apply";
		newFlow = true;
	} else if ($(this).hasClass("group-app")) {
		myEventId = "applyGrp";
		newFlow = true;
	} else if ($(this).hasClass("check-individual-app")|| $(this).hasClass("check-individual-app2")) {
		myEventId = "retrieveSingleApplication";
		newFlow = true;
	} else if ($(this).hasClass("check-group-app")) {
		myEventId = "retrieveGroupApplication";
		newFlow = true;
	} else if (this.id == "_eventId_previous") {
		myEventId = "previous";
	} else if (this.id == "_eventId_manageGroup") {
		myEventId = "manageGroup";
	} else if (this.id == "_eventId_disclaimer-addToGroup") {
		myEventId = "disclaimer-addToGroup";
	}
	
	// If user clicked on a menu item we let webflow create a new flow otherwise
	// we post in the same flow ID
	var formHTML;
	formHTML = '<form id="ETAApplication" action="application.html';
	if (newFlow) {
		formHTML = formHTML + '" method="post">';
	} else {
		formHTML = formHTML + '?execution=' + flowExec + '" method="post">' +
		'<input type="hidden" name="_flowExecutionKey" value="'+flowExec+'" />';
	}
	formHTML = formHTML + 
	'<input type="hidden" name="' + myEventId + '" value="please"/>' +
	'<input type="submit" id="_eventId_' + myEventId + '" name="_eventId_' + myEventId + '" value="' +
	yesLabel +
	'" tabindex="0" ' +
	'class="btn btn-default btn-md button esta-button-primary esta-modal-button-primary" />' +
	'</form>';
			
	// remove <a> tag
	$("#restartModal .modal-footer  .esta-button-primary").remove();
	// Add <form> code after <a> tag				
	$("#restartModal .modal-footer .pull-right").append($(formHTML));

    
    $("#restartModal").modal('show');
    $(window).off("beforeunload");

    // Setup handler to reset the Yes button and the Security Notification button on close
    $("#restartModal").on("hidden.bs.modal", function (e) {
    	$("#restartModal .modal-footer .pull-right").html('');
    	$("#submitButton").html('');
    });
	return false;
}

function addOnClickEvent(obj, func) {
 	var oldEvent = obj.onclick;
	if (typeof obj.onclick != 'function') {
		 obj.onclick = func;
	} else {
		 obj.onclick = function() {
			if (oldEvent) {
				oldEvent();
			}
			func(obj);
		};
	}
}

addOnClickEvent(document.getElementById("homeMenu"), unsavedWorkModalClick );
addOnClickEvent(document.getElementById("individualApplicationMenu"), unsavedWorkModalClick );
addOnClickEvent(document.getElementById("groupApplicationMenu"), unsavedWorkModalClick );
addOnClickEvent(document.getElementById("checkApplicationMenu"), unsavedWorkModalClick );
addOnClickEvent(document.getElementById("checkGroupMenu"), unsavedWorkModalClick );
