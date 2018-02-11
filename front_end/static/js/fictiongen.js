/*------------------------------------------------------------------------------------------*/
// Calculations
/*------------------------------------------------------------------------------------------*/

/* Total words of all active books */
function get_total_words() {
    total_words = 0;
    $('.booktile[data-text-active]').each(function() {
        total_words = total_words +  ( $(this).attr('data-text-words') * 1); // * 1 to convert to int.
    })
    return total_words;
}

/* Calculates a user readable value for how much a book will come into play in the process */
function calculate_weight_ratio(total,single_book_words, book_weight) {
    // Picking a format which makes sense to a user.
    // Might be good to do this to a nearest fraction.
    power =  ( single_book_words / total ) * 100 
    power = power * book_weight
    console.log(power);
    ui_power = power.toFixed(2);
    return ui_power;
}


/*------------------------------------------------------------------------------------------*/
// UI Functions
/*------------------------------------------------------------------------------------------*/
// ADD: I'd like to move these to a separate file, and perhaps handle them as an object.
// These are very much template functions just to get basic functionality running


function ui_pulse(clickedItem) {
    // Pulse slightly combined with other actions

    /* 
        Note: incase I forget what I was thinking here. Some kind of general responsiveness in the interface 
        for clicks would be good.

    */
    $('body').addClass('tactile-click');
    $(clickedItem).addClass('clk-out');
    setTimeout(function() { 
        $('body').removeClass('tactile-click');
        $(clickedItem).removeClass('clk-out');
    },600);
}

/* Activate the "Results will appear shortly" notice */
function ui_activate_loading_notice() {
    $('.loading-notice').animate({ top:'70px' },'slow');
    $('.response-field-wrap').css('display','block');
    // setTimeout(ui_deactivate_loading_notice,5000); // removed on ajax completion
}

function ui_deactivate_loading_notice() {
    $('.loading-notice').animate({ top:'-600px' },200); // Quick unload
    $('.response-field-wrap').css('display','none');
}

/* Activate the results pane */
function ui_activate_results_pane() {
    $('.response-text').css('display','block');
}

/* Deactivate the text result pane */
function ui_deactivate_results_pane() {
    $('.response-field-wrap').css('display','none');
    $('.response-text').css('display','none');
}

/* Set the user visible indicator of how heavily a book will feature in the chain */
function ui_set_relative_weights() {
    total = get_total_words();
    $('.booktile[data-text-active]').each(function() {
        single_books_words = $(this).attr('data-text-words');
        book_weight = $(this).children('.book-weight').val();
        weight = calculate_weight_ratio(total,single_books_words,book_weight);
        $(this).children('.book-power').html(weight);
    })
}

/* Set active book weights to the most even value */
function ui_set_even_weights() {
    $('.booktile[data-text-active]').each(function() {
        total_words = get_total_words();
        book_words = $(this).attr('data-text-words');
        power = total_words / book_words;
        $(this).children('.book-weight').val(power);
    });
    ui_set_relative_weights(); // Update the visible numbers
}




/*------------------------------------------------------------------------------------------*/
// Getting data from the page/user
/*------------------------------------------------------------------------------------------*/

function get_lines() { return $('#line-num').val()  }
function get_paragraph_size() { return $('#paragraph-size').val()  }
function get_statesize() { return $('#state-size').val()  }
function get_url() { return $('#url-entry').val()  }
function get_grammar_kit() {
    if ($('#grammar-entry').is(":checked"))
    {return 1; } else { return 0;}
}

function get_active_books() { 
    /* Retrieves active books and weights to be passed to the request */
    bookIDs = {};
    $('.booktile[data-text-active]').each(function() {
        var bookObj = {}
        id = $(this).attr("data-book-id");
        weight = $(this).attr("data-text-weight");
        bookIDs[id] = weight;
    })
    return bookIDs;
}
function get_name_replacements() {
    if ($('#name-replacement').is(":checked")){
        var male_name = $('#male-name').val();
        var female_name = $('#female-name').val();
        return {male_name, female_name}; 
    } else {
     return 0;
    }
}


function get_book_request_json() {
    /* Retrieves the JSON data to be passed to the request. This is an amalgamation of the above */
    bookIDs = get_active_books();
    data = JSON.stringify({
        book_ids : bookIDs,
        stateSize: get_statesize() ,
        lines: get_lines(),
        paragraphs: get_paragraph_size(),
        posEnabled : get_grammar_kit(),
        names: get_name_replacements(),
        csrfmiddlewaretoken: "{{ csrf_token }}"
    })
    return data;
}

/*------------------------------------------------------------------------------------------*/
// Ajax Requests
/*------------------------------------------------------------------------------------------*/
function send_log() {
    ui_activate_loading_notice();
    $.ajax({
        url: '/mk/process/',
        type: 'POST',
        dataType: 'json',
        data: get_book_request_json(),
        success : function(data) {
            $( ".response-field p" ).html(data);
            ui_activate_results_pane();
        },
        complete : function() {
            ui_deactivate_loading_notice();
            console.log("Complete")
        },
        error : function() {
            console.log("Server error");

            $('.loading-notice').html("I'm sorry there was an error and the text couldn't be loaded.")
        }
    });
 }


/*------------------------------------------------------------------------------------------*/
// Events
/*------------------------------------------------------------------------------------------*/
$(document).ready(function() {
    $(".close-text").on('click', ui_deactivate_results_pane );
    $(".book-weight").on('change', ui_set_relative_weights );
    $("#books-equaliser").on('click', ui_set_even_weights );
    $(".booktile .booktile-clickable").click(function(){
        ui_pulse(this);
          var booktile = $(this).parent();
          if (booktile.attr('data-text-active')) {
            booktile.removeAttr('data-text-active'); // Toggle attribute
            booktile.appendTo('.booktile-details-inner');
        } else {
            booktile.attr('data-text-active',"on");
            booktile.appendTo('#active-books');
        }
    });

    //async load images
    $('img[data-async-src]').each(function() {
        $(this).attr('src',$(this).attr('data-async-src'));
    });

});



/*------------------------------------------------------------------------------------------*/
// Copy to clipboard
/*------------------------------------------------------------------------------------------*/

function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}


