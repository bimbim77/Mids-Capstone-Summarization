/**
 * Gets the desired element on the client page and clicks on it
 */
function goToActivityTab() {
    var activityTab = document.getElementsByClassName("artdeco-button__text")[0];

    activityTab.click();
    
    window.addEventListener("load", function(){
    	navigator.clipboard.readText()
  		.then(text => {
    	document.querySelector('.ql-editor').innerText = text;
  	})
  		.catch(err => {
    	console.log('Something went wrong', err);
  });
});

    

}

goToActivityTab();