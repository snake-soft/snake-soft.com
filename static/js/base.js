function set_menu_height(){
	var menu_height = $('.cms-toolbar').height();
	$('#home').css('margin-top', menu_height);
}

$(document).ready(function() {
	set_menu_height();
	alert('fdas');
});
