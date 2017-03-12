"use strict";
if(typeof Placeholdem === 'function') {
	if (document.querySelectorAll( '[placeholder]' ).length) {
		Placeholdem( document.querySelectorAll( '[placeholder]' ) );
	};
}

function pieChart() {
	//circle progress bar
	if ((jQuery().easyPieChart) && (jQuery.support.leadingWhitespace)) {
		var count = 0 ;
		var colors = ['#DD4861'];
		jQuery('.chart').each(function(){
				
			var imagePos = jQuery(this).offset().top;
			var topOfWindow = jQuery(window).scrollTop();
			if (imagePos < topOfWindow+600) {

				jQuery(this).easyPieChart({
			        barColor: colors[count],
					trackColor: '#e5e5e5',
					scaleColor: false,
					scaleLength: false,
					lineCap: 'butt',
					lineWidth: 13,
					size: 100,
					rotate: 0,
					animate: 2000,
					onStep: function(from, to, percent) {
							jQuery(this.el).find('.percent').text(Math.round(percent));
						}
			    });
			}
			count++;
			if (count >= colors.length) { count = 0};
		});
	}
}

jQuery(document).ready(function() {

	//animation to elements on scroll
	if (jQuery().appear) {
		jQuery('.to_animate').appear().css({opacity: 0});
		jQuery('.to_animate').filter(':appeared').each(function(index){
			var self = jQuery(this);
			var animationClass = !self.data('animation') ? 'fadeInUp' : self.data('animation');
			var animationDelay = !self.data('delay') ? 200 : self.data('delay');
			setTimeout(function(){
				self.addClass("animated " + animationClass);
			}, index * animationDelay);
		});

		jQuery('body').on('appear', '.to_animate', function(e, $affected ) {
			jQuery($affected).each(function(index){
				var self = jQuery(this);
				var animationClass = !self.data('animation') ? 'fadeInUp' : self.data('animation');
				var animationDelay = !self.data('delay') ? 200 : self.data('delay');
				setTimeout(function(){
					self.addClass("animated " + animationClass);
				}, index * animationDelay);
			});
		});
	}

	//counters init on scroll
	if (jQuery().appear) {
		jQuery('.counter').appear();
		jQuery('body').on('appear', '.counter', function(e, $affected ) {
			jQuery($affected).each(function(index){
				if (jQuery(this).hasClass('counted')) {
					return;
				} else {
					jQuery(this).countTo().addClass('counted');
				}
				
			});
		});
	}

	//menu
	if (jQuery().superfish) {
		jQuery('ul.sf-menu').superfish({
			delay:       700,
			animation:   {opacity:'show',height:'show'},
			animationOut: {opacity: 'hide'},
			speed:       'fast',
			disableHI:   false,
			cssArrows:   false,
			autoArrows:  false
		});
	}

	//toTop
	if (jQuery().UItoTop) {
        jQuery().UItoTop({ easingType: 'easeOutQuart' });
    }

	//parallax
	if (jQuery().parallax) {
		jQuery('#testimonials').parallax("50%", 0.4);
	}

	//prettyPhoto
    if (jQuery().prettyPhoto) {
	   	jQuery("a[data-gal^='prettyPhoto']").prettyPhoto({
	   		hook: 'data-gal',
			theme: 'facebook' /* light_rounded / dark_rounded / light_square / dark_square / facebook / pp_default*/
	  	});
	}

   	//carousel
   	if (jQuery().carousel) {
		jQuery('.carousel').carousel();
	}

	//owl carousel
	if (jQuery().owlCarousel) {
		//upcomming events carousel
	    jQuery(".owl-carousel.owl-items-5").owlCarousel({
	    	navigation : true,
	    	navigationText : false,
	    	pagination : false,
	    	items: 5
	    });

	    //partners
	    jQuery(".partners").owlCarousel({
	    	navigation : true,
	    	navigationText : false,
	    	pagination : false,
	    	items: 5,
	    	autoPlay: 5000
	    });
	}
    
	//bx slider
	if (jQuery().bxSlider) {
		jQuery('.bxslider').bxSlider({
			auto: true,
			controls: false,
			pager: false,
		  	mode: 'fade'
		});

		jQuery('.vertical-slider').bxSlider({
			mode: 'vertical',
			//slideWidth: 300,
			minSlides: 2,
			slideMargin: 30,
			pager: false
		});
	}

	//single page localscroll and scrollspy
	var navHeight = jQuery('#header').outerHeight(true) + 40;
	jQuery('body').scrollspy({
		target: '.mainmenu_wrap',
		offset: navHeight
	});
	if (jQuery().localScroll) {
		jQuery('#mainmenu, #land').localScroll({
			duration:1400,
			easing:'easeInOutQuint',
			offset: 0
		});
		
	}

	//twitter
	//slide tweets
	jQuery('#tweets .twitter').bind('loaded', function(){
		jQuery(this).addClass('flexslider').find('ul').addClass('slides');
	});
	if (jQuery().tweet) {
		jQuery('.twitter').tweet({
			modpath: "./twitter/",
		    count: 3,
		    avatar_size: 48,
		    loading_text: 'loading twitter feed...',
		    join_text: 'auto',
		    username: 'ThemeForest', 
		    template: "{avatar}{time}{join}<span class=\"tweet_text\">{tweet_text}</span>"
		});
	}

});

jQuery(window).load(function(){
	
	//init gallery
	Grid.init();

	//chart
	pieChart();

	
	setTimeout(function(){
		jQuery('.progress-bar').addClass('stretchRight');
	}, 600);

	//stick header to top
	if (jQuery().sticky) {
	    jQuery("#header").sticky({ 
	    		topSpacing: 0,
	    		scrollBeforeStick: 80
	    	},
	    	function(){ 
	    		jQuery("#header").stop().animate({opacity:0}, 0).delay(500).stop().animate({opacity:1}, 800);
	    	},
	       	function(){ 
	    		jQuery("#header").stop().animate({opacity:0}, 0).delay(800).stop().animate({opacity:1}, 1000);
	    	}
	    );
	}
	

	if (jQuery().flexslider) {
		jQuery("#mainslider .flexslider").flexslider({
			animation: "fade",
			useCSS: true,
			controlNav: true,   
			directionNav: false,
		    prevText: "",
		    nextText: "",
			smoothHeight: false,
			slideshowSpeed:5000,
			animationSpeed:800,
			start: function( slider ) {
				slider.find('.slide_description').children().attr('style', 'opacity:0;');
				slider.find('.flex-active-slide .slide_description').children().each(function(index){
				var self = jQuery(this);
				var animationClass = !self.data('animation') ? 'fadeInRight' : self.data('animation');
				setTimeout(function(){
						self.addClass("animated "+animationClass);
					}, index*200);
				});
			},
			after :function( slider ){
				slider.find('.flex-active-slide .slide_description').children().each(function(index){
				var self = jQuery(this);
				var animationClass = !self.data('animation') ? 'fadeInRight' : self.data('animation');
				setTimeout(function(){
						self.addClass("animated "+animationClass);
					}, index*200);
				});
			},
			end :function( slider ){
				slider.find('.slide_description').children().each(function() {
					jQuery(this).attr('class', '');
				});
			}
		});

		jQuery(".flexslider").flexslider({
			animation: "fade",
			useCSS: true,
			controlNav: true,   
			directionNav: false,
		    prevText: "",
		    nextText: "",
			smoothHeight: true,
			slideshowSpeed:5000,
			animationSpeed:800,
			after :function( slider ){
			}
		});
	}

	jQuery('body').delay(1000).scrollspy('refresh');


	//preloader
	jQuery(".preloaderimg").fadeOut();
	jQuery(".preloader").delay(200).fadeOut("slow").delay(200, function(){
		jQuery(this).remove();
	});

	//flickr
	// use http://idgettr.com/ to find your ID
	if (jQuery().jflickrfeed) {
		jQuery("#flickr").jflickrfeed({
			flickrbase: "http://api.flickr.com/services/feeds/",
			limit: 6,
			qstrings: {
				id: "63512867@N07"
			},
			itemTemplate: '<a href="{{image_b}}" rel="prettyPhoto[pp_gal]"><li><img alt="{{title}}" src="{{image_s}}" /></li></a>'
		}, function(data) {
			jQuery("#flickr a").prettyPhoto({
				theme: 'facebook'
	   		});
	   		jQuery("#flickr li").hover(function () {						 
			   jQuery(this).find("img").stop().animate({ opacity: 0.5 }, 200);
		    }, function() {
			   jQuery(this).find("img").stop().animate({ opacity: 1.0 }, 400);
		    });
		});
	}


});

jQuery(window).resize(function(){
	if (jQuery().sticky) {
		jQuery("#header").sticky('update');
	}
	jQuery('body').scrollspy('refresh');

});

jQuery(window).scroll(function() {

	//circle progress bar
	pieChart();


});