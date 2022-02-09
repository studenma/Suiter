var characteristic = {}; 


function generateTestSuite() {
	var form = document.forms['char'];
	var data = form['message'].value;
	var data_suiter;

	// send the request to Combine
	var xhr_combine = new XMLHttpRequest();
	xhr_combine.addEventListener("readystatechange", function() {
	  if(xhr_combine.readyState === 4 && xhr_combine.status === 200) {
	  	console.log(xhr_combine.responseText);
	  	// send the request to Suiter
	  	if(xhr_combine.readyState === XMLHttpRequest.DONE) {
            data = JSON.stringify(xhr_combine.responseText);
			var xhr_suiter = new XMLHttpRequest();
			xhr_suiter.open("POST", "/generate" , true);
			xhr_suiter.setRequestHeader("Content-Type", "application/json");
			xhr_suiter.send(data);
        }
	  }
	});
	xhr_combine.open("POST", "http://127.0.0.1:3000/generate" , true);
	xhr_combine.setRequestHeader("Content-Type", "application/json");
	xhr_combine.send(data);

	
	// var xhr_suiter = new XMLHttpRequest();
	// xhr_suiter.addEventListener("readystatechange", function() {
	//   if(xhr_suiter.readyState === 4 && xhr_suiter.status === 200) {
	//   	console.log(xhr_suiter.responseText);
	//   }
	// });
	// xhr_suiter.open("POST", "/generate" , true);
	// xhr_suiter.setRequestHeader("Content-Type", "application/json");
	// data_suiter = JSON.stringify(data_suiter);
	// console.log(data_suiter);
	// xhr_suiter.send(data_suiter);
}