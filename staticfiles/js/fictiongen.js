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

/* Activate the "Results will appear shortly" notice */
function ui_activate_loading_notice() {
    $('.loading-notice').animate({ top:'100px' },'slow');
    $('.response-field-wrap').css('display','block');
    setTimeout(ui_deactivate_loading_notice,5000);
}

function ui_deactivate_loading_notice() {
    $('.loading-notice').animate({ top:'-600px' },'slow');
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
// UI Functions; Jquery Resizable
/*------------------------------------------------------------------------------------------*/

function ui_set_resizable_handles() {
    console.log("Resizable Handles Started");
    var options = {
        handleSelector: null,
        resizeWidth : true,
        resizeWidthFrom: 'right'
    }
    $('.booktile').resizable(options);
}

/*------------------------------------------------------------------------------------------*/
// Getting data from the page/user
/*------------------------------------------------------------------------------------------*/

function get_lines() { return $('#line-num').val()  }
function get_statesize() { return $('#state-size').val()  }
function get_url() { return $('#url-entry').val()  }
function get_grammar_kit() {
    if ($('#grammar-entry').is(":checked"))
    {return 1; } else { return 0;}
}
/* Retrieves active books and weights to be passed to the request */
function get_active_books() { 
        bookIDs = {};
        $('.booktile[data-text-active]').each(function() {
            bookObj = {}
            id = $(this).attr("data-book-id");
            weight = $(this).attr("data-text-weight");
            bookIDs[id] = weight;
        })
        return bookIDs;
}

/* Retrieves the JSON data to be passed to the request */
function get_book_request_json() {
    bookIDs = get_active_books();
    data = JSON.stringify({
        book_ids : bookIDs,
        stateSize: get_statesize() ,
        lines: get_lines(),
        posEnabled : get_grammar_kit(),
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
            ui_activate_loading_notice();
        },
        error : function() {
            console.log("Server error");
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
    $(".booktile").click(function(){
          if ($(this).attr('data-text-active')) {
            $(this).removeAttr('data-text-active'); // Toggle attribute
        } else {
            $(this).attr('data-text-active',"on");
        }
    ui_set_resizable_handles();
    ui_set_relative_weights(); // Set the relative weights of texts
    
    console.log("Page Events Successfully Registered");
    });
});

