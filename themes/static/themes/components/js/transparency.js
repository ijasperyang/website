jQuery(document).ready(function() {

    updateHeaderTransparency();

    $(window).scroll(function(){
	    updateHeaderTransparency();
	});

    $(window).resize(function(){
        updateHeaderTransparency();
    });

    function updateHeaderTransparency() {
        var offset = ($('header').height() + parseInt($('main').css('padding-top')) ) * -1;
        $('.main-feature').css("margin-top", offset);

    	if ($('header').hasClass('scrolled') || $('#search-box').hasClass("open")) {
	        transparencyOff();
	    } else if ($('.main-feature').length && !$("body").hasClass("template-home-page")) {
	         transparencyOn();
	    }
    }

    function transparencyOn() {
        $('header').addClass("transparency");
        $('#toggle-mobile').hide();
        $('#search-box-toggle').hide();
        $('#main-menu').hide();
    }

    function transparencyOff() {
        $('header').removeClass("transparency");
        $('#toggle-mobile').show();
        $('#search-box-toggle').show();
        $('#main-menu').show();

        if ($('#search-box').hasClass("open") && $(window).width() >= breakpoint) {

            if ($('header').hasClass('collapsed')) {
                $('#toggle-mobile').show();
            } else {
               $('#toggle-mobile').hide();
            }
        }
    }
});
