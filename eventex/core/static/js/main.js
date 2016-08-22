jQuery(document).ready(function($) {

   'use strict';

	//SMOOTH SCROLL
    smoothScroll.init({
		speed: 500, // How fast to complete the scroll in milliseconds
		easing: 'easeInOutCubic', // Easing pattern to use
		updateURL: false, // Boolean. Whether or not to update the URL with the anchor hash on scroll
		callbackBefore: function ( toggle, anchor ) {}, // Function to run before scrolling
		callbackAfter: function ( toggle, anchor ) {} // Function to run after scrolling
	 });

	//FIX HOVER EFFECT ON IOS DEVICES
	document.addEventListener("touchstart", function(){}, true);


});

$(window).load(function(){

    //HEADER ANIMATION
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        var offset = $(".header-frame").height() / 3;

        if (scroll > offset) {
            $( ".header-frame" ).addClass( "header-frame-fixed" );
        } else {
            $( ".header-frame" ).removeClass( "header-frame-fixed" );
        }

    });

});

//GOOGLE MAP
function init_map() {
    var myOptions = {
        zoom: 14,
        center: new google.maps.LatLng(-22.902488, -43.175939), //change the coordinates
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        styles: [{featureType:'all',stylers:[{saturation:-100},{gamma:0.90}]}]
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(-22.902488, -43.175939) //change the coordinates
    });

}
google.maps.event.addDomListener(window, 'load', init_map);



