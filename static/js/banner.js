
function random_integer(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}

function fetch(){
	var jqxhr = $.getJSON( "/api/django-random/", function() {
		console.log( "success" );
	})
	.done(async function(json) {
		$("#classpath").html(json.classpath);
		$('#nowplaying').prop('title', json.size + ' bytes');

		for (char of json.data){
			if (char == ' '){
				var duration = random_integer(40, 120);
			}
			await new Promise(resolve => setTimeout(resolve, duration));
		    $('#code_runner').append(char);
		    if (char == '\n' || true){
		      var code_so_far = $('#code_runner').text();
		      code_so_far = hljs.fixMarkup(code_so_far);
		      code_so_far = hljs.highlight('python', code_so_far).value
		      $('#code_runner').html(code_so_far);
		    }
		}
		
	})
}

async function enable_cookie_banner(){
	await new Promise(resolve => setTimeout(resolve, 5000));
	$('#cookie-policy-bar').fadeIn();
}

$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
    fetch();
    enable_cookie_banner();
});
