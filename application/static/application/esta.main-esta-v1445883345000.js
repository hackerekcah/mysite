/**
 * ESTA initializer and universal global objects
 * This should be called before anything else
 * NOTE: LINK THIS FILE INSIDE <head></head>
 * @param global (window)
 */
(function(global) {
	
	global.esta = global.esta || {};
	
	if(typeof global.contextPath === 'undefined'){
		throw "window.contextPath is required for esta";
	} else if(typeof global.pageId === 'undefined'){
		throw "undefined", "window.pageId is required for esta";
	}
	
	global.esta.contextPath = global.contextPath;
	global.esta.pageId = global.pageId;
	
})(typeof window === 'undefined' ? this : window);

/**
* ESTA events
* @param esta
* @param $
*/
(function(esta, $) {
	
	esta.events = esta.events || {};
	esta.events.css = esta.events.css || {};
	esta.events.css.STYLES_DISABLED = "esta.styles.disabled";
	esta.events.css.STYLES_ENABLED = "esta.styles.enabled";
	
})(esta, jQuery);

/**
 * Safe logger and threshold output
 * @param esta
 */
(function(esta) {
	
	if(typeof esta === 'undefined'){
		throw "esta must be defined to use esta.log";
	}
	
	esta.log = esta.log || new function(){
		
		this.MSG = 0;
		this.WARN = 1;
		this.ERR = 2;
		this.LOG_THRESHOLD = 0;
		
		this.lastContext = "";
		
		var instance = this;
		
		this.comment = function(obj, context){
			if(	typeof console !== 'undefined' && instance.LOG_THRESHOLD <= instance.MSG){
				console.log(obj);
				instance.lastContext = typeof context === 'undefined' ? "none" : context;
			}
		};
		
		this.warning = function(obj, context){
			if(	typeof console !== 'undefined' && instance.LOG_THRESHOLD <= instance.WARN){
				console.warn(obj);
				instance.lastContext = typeof context === 'undefined' ? "none" : context;
			}
		};
		
		this.error = function(obj, context){
			if(	typeof console !== 'undefined' && instance.LOG_THRESHOLD <= instance.ERR){
				console.error(obj);
				instance.lastContext = typeof context === 'undefined' ? "none" : context;
			}
		};
		
		return this;
		
	};
	
})(esta);

