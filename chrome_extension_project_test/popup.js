$(function(){

	
    
    $('#tw_submit').click(function(){

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

						var tw_button = document.getElementById("tw_submit");
						var li_button = document.getElementById("li_submit");
						tw_button.remove();
						li_button.remove();

						var tbox = document.createElement("textarea");
  						tbox.setAttribute("id", "article");
  						tbox.setAttribute("rows", "5");
  						tbox.setAttribute("cols", "55");
  						$( ".textBox" ).append(tbox);
  						document.getElementById("article").value = result.summary;

  						var socialPost = document.createElement("INPUT");
  						socialPost.setAttribute("type", "submit");
  						socialPost.setAttribute("value","Post To Twitter");
  						socialPost.setAttribute("id", "tw_post");
  						socialPost.setAttribute("width","200px");
  						$( ".inline" ).append(socialPost);

  						$('#tw_post').click(function(){
  							chrome.runtime.sendMessage({"message": "open_new_tab", "url": 'https://twitter.com/intent/tweet?text=' + result.summary + '&url=' + url});


  							});
  						
					});
		}
			
			
		
		
    });
});

    $('#li_submit').click(function(){

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

						var tw_button = document.getElementById("tw_submit");
						var li_button = document.getElementById("li_submit");
						tw_button.remove();
						li_button.remove();

						var tbox = document.createElement("textarea");
  						tbox.setAttribute("id", "article");
  						tbox.setAttribute("rows", "5");
  						tbox.setAttribute("cols", "55");
  						$( ".textBox" ).append(tbox);
  						document.getElementById("article").value = result.summary;

  						var socialPost = document.createElement("INPUT");
  						socialPost.setAttribute("type", "submit");
  						socialPost.setAttribute("value","Post To LinkedIn");
  						socialPost.setAttribute("id", "li_post");
  						socialPost.setAttribute("width","200px");
  						$( ".inline" ).append(socialPost);

  						$('#li_post').click(function(){
  							var copyText = document.getElementById("article");
  							copyText.select();
  							copyText.setSelectionRange(0, 99999);
  							document.execCommand("copy");

  							chrome.runtime.sendMessage({"message": "open_li_tab", "url": 'https://www.linkedin.com/sharing/share-offsite/?url=' + url});
  							

  							});
  							
  						});
					
		}
			
			
		
		
    });
});







});