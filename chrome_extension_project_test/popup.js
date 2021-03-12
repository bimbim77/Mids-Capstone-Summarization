$(function(){

	
    
    $('#urlsubmit').click(function(){

    	var queryInfo = {
    		active: true,
    		currentWindow: true
  			};

  		chrome.tabs.query(queryInfo, (tabs) => {
    		var tab = tabs[0];
    		var url = tab.url;
		

		if (url){
                chrome.runtime.sendMessage(
					{article: url},
					function(response) {
						result = response.farewell;
						$('#article').val(result.summary);
					});
		}
			
			
		
		
    });
});

});