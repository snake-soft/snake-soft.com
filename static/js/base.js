
function split_text_into_lines(text){
	return text.split('\n');
}

function split_line_into_words(line){
	return line.split(' ');
}
/**
$(document).ready(function() {
	var lines = split_text_into_lines(text);
	for (var i = 0; i < lines.length; i++){
		var words = split_line_into_words(lines[i])

		for (var j = 0; j < words.length; j++){
			$('#code_runner').append(words[j] + ' ');
		}
		$('#code_runner').append('\n');
	}
});**/

function stripHTML(dirtyString) {
	  var container = document.createElement('div');
	  var text = document.createTextNode(dirtyString);
	  container.appendChild(text);
	  return container.innerHTML; // innerHTML will be a xss safe string
	}

function clean_text(text){
	var clean_text = '';
	for (var i = 0; i < text.length; i++){
		switch (text.charAt(i)){
		case '\n':
			clean_text += '<br>';
			break;
		case ' ':
			clean_text += ' ';//'&nbsp;';
			break;
		default:
			clean_text += text.charAt(i);
		}
	}
	text = hljs.highlight('python', text).value;
	return hljs.fixMarkup(text);
}

//text = clean_text(text);
//var text = hljs.highlight('python', text1).value;
//text = hljs.fixMarkup(text1);

//alert(text);

function sleep(ms) {
	  return new Promise(resolve => setTimeout(resolve, ms));
	}

function initialize_code(){
	//alert($('#code_runner').html());
	//var code = $('#new').html();
	//alert(hljs.highlight('python', code).value);
	//hljs.highlight('python', code).value;
	////$('#code_runner').html(hljs.highlight('python', code).value);
	//	hljs.initHighlighting();
	//alert($('#code_runner').html());
//    alert(hljs.highlightBlock($('#code_runner').html()));
}



async function float(){
	for (var i = 0; i<text.length; i++){
		$('#code_runner').append(text[i]);
		if (text[i] == '\n'){
			var code = $('#code_runner').text();
			code = hljs.fixMarkup(code);
			code = hljs.highlight('python', code).value
			$('#code_runner').html(code);
		}
		await new Promise(resolve => setTimeout(resolve, 50));
	}
}


// split into lines
// split lines into words
// add div/span(?) per word
// add class to div/span after word has finished
// add classes for iterals
$(document).ready(function() {
	//var obj = $('#code_runner')
	//var code = hljs.highlight('python', obj.html()).value;
	//obj.html(hljs.fixMarkup(code)); 
	//$('#code_runner').append(text);//hljs.highlight('python', text).value);
	$(function () {
		$('[data-toggle="tooltip"]').tooltip()
	})
	//float();
});
