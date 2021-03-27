//var serverhost = 'http://127.0.0.1:8000';
var serverhost = 'http://ec2-3-101-66-156.us-west-1.compute.amazonaws.com';

	chrome.runtime.onMessage.addListener(
		function(request, sender, sendResponse) {
		  	if (request.message === "tw_submit") {
			  
				var url = serverhost + '/get_tw_article_summary/?article='+ encodeURIComponent(request.article) ;
			
				console.log(url);
			
				fetch(url)
				.then(response => response.json())
				.then(response => sendResponse({farewell: response}))
				.catch(error => console.log(error))
				
				return true;  // Will respond asynchronously.
		  
	}});

	chrome.runtime.onMessage.addListener(
		function(request, sender, sendResponse) {
		  	if (request.message === "li_submit") {
			  
				var url = serverhost + '/get_li_article_summary/?article='+ encodeURIComponent(request.article) ;
			
				console.log(url);
			
				fetch(url)
				.then(response => response.json())
				.then(response => sendResponse({farewell: response}))
				.catch(error => console.log(error))
				
				return true;  // Will respond asynchronously.
		  
	}});

	chrome.runtime.onMessage.addListener(
  		function(request, sender, sendResponse) {
    		if( request.message === "open_tw_tab" ) {
      			chrome.tabs.create({"url": request.url});
    }
  	}
	);

	chrome.runtime.onMessage.addListener(
  		function(request, sender, sendResponse) {
    		if( request.message === "open_li_tab" ) {
      			chrome.tabs.create({"url": request.url});
    }
  	}
	);

	chrome.runtime.onMessage.addListener(
  		function(request, sender, sendResponse) {
    		if( request.message === "get_clipboard" ) {
      			chrome.tabs.create({"url": request.url});
    }
  	}
	);