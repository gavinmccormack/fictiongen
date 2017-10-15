(function($){

equalheight = function(container){

var currentTallest = 0,
     currentRowStart = 0,
     rowDivs = new Array(),
     $el,
     topPosition = 0;
 $(container).each(function() {

   $el = $(this);
   $($el).height('auto')
   topPostion = $el.position().top;

   if (currentRowStart != topPostion) {
     for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
       rowDivs[currentDiv].height(currentTallest);
     }
     rowDivs.length = 0; // empty the array
     currentRowStart = topPostion;
     currentTallest = $el.height();
     rowDivs.push($el);
   } else {
     rowDivs.push($el);
     currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
  }
   for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
     rowDivs[currentDiv].height(currentTallest);
   }
 });
}

$(window).load(function() {
  equalheight('.col-md-6');
});
$(window).resize(function(){
  equalheight('.col-md-6');
});




// Slide animations on page change
// This is very rough and a few obvious flaws come to mind already.

function slide_out(selector) {
  $( selector ).animate({
    opacity: 0.25,
    left: "-5000"
  }, 2000, function() {
    $( selector ).addClass('inactive')
  });
}

function slide_in(selector) {
  $( selector ).animate({
    opacity: 1,
    left: "0",
  }, 2000, function() {
  });

  $( selector ).removeClass('inactive')
}

function register_slide_left(trigger, slideFrom, slideTo) {
// prototype
  $( trigger ).click(function() {
      slide_out(slideFrom);
      slide_in(slideTo);
  });
}

$(window).load(function() {
  register_slide_left('.intro-button','.introduction-page','.generator-page');
  register_slide_left('#talk-button','.generator-page','.results-page');
});

})(jQuery);

