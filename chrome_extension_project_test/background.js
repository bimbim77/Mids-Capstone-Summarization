var serverhost = 'http://127.0.0.1:8000';

	chrome.runtime.onMessage.addListener(
		function(request, sender, sendResponse) {
		  
			  
			var url = serverhost + '/get_article_title/?article='+ encodeURIComponent(request.article) ;
			
			console.log(url);
			
			fetch(url)
			.then(response => response.json())
			.then(response => sendResponse({farewell: response}))
			.catch(error => console.log(error))
				
			return true;  // Will respond asynchronously.
		  
	});

	chrome.runtime.onMessage.addListener(
  		function(request, sender, sendResponse) {
    		if( request.message === "open_new_tab" ) {
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