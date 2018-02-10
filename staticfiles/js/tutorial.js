// An interactive tutorial button to highlight options and explain them.
// The naming/classes here are a bit fecked, but can refactor later.

function set_trigger(selector){ // This is a weird name.
    // sets an element to serve as the tutorial trigger.
    $(selector).on('click', init_tutorial);
}

function show_tutorial_overlay(){
    $('#tutorial-pane').attr('data-tutorial-active', 1)
}

function hide_tutorial_overlay(){
    $('#tutorial-pane').attr('data-tutorial-active', 0)
}

function show_description(selector) {
   $(selector).addClass('tutorial-show');
}

function show_item_tutorial(item_selector,item_description_selector) {
  //Highlight the relevant items, and show the help text
  highlight_item(item_selector);
  show_description(item_description_selector)
}

function init_tutorial() {
  console.log("Tutorial On");
  show_tutorial_overlay();

  //Books
  show_item_tutorial('.booktile','#booktile-tutorial');
}

function highlight_item(selector) {
  var item = $(selector)
  item.css('z-index','5000');
  item.addClass('active-tutorial-item');
}


$(document).ready(function() {
  set_trigger('#tutorial-activate');
  

});