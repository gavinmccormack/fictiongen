
function log_format(text) {
            time =  new Date().toJSON().slice(11,19)
            return ("<br /><span class='console-time'>" + time + "</span>" + text)
        }

function get_lines() { return $('#line-num').val()  }
function get_statesize() { return $('#state-size').val()  }
function get_url() { return $('#url-entry').val()  }
function get_grammar_kit() {
    if ($('#grammar-entry').is(":checked"))
    {return 1; } else { return 0;}}




function testJSON() {
  // Testing the JSON object as a method of sending the post request. this will change the data to be in the request body
     $.ajax({
        url: '/mk/processjson/',
        type: 'POST',
        data: { json: JSON.stringify({
            name:"Bob"
        })},
        dataType: 'json'
    }, function (data) {alert(data)});
}


function send_log() {
                    bookIDs = []
                    $('.booktile[data-book-active]').each(function() {
                        bookIDs.push($(this).attr("bookid"));
                    })
                    console.log(bookIDs);
                    $.post('/mk/process/', {
                        book_ids: bookIDs,
                        stateSize: get_statesize() ,
                        lines: get_lines(),
                        posEnabled : get_grammar_kit(),
                        csrfmiddlewaretoken: "{{ csrf_token }}"}, function (data) {
                    $( ".response-field p" ).html(log_format(data));
                    });
                 }

function retrieve_text_from_url(query) {
                    $.post('/steal-text/', { url : get_url() ,  csrfmiddlewaretoken: "{{ csrf_token }}"}, function (data) {
                     $( "#markov-entry" ).append(log_format(data));
                    });
                 }

$(document).ready(function() {
                $("#add-url").keypress(function(event){
                    if(event.which == 13){
                        $("#add-url").click();
                        return false;
                    }
                });

                // Default Tab
                document.getElementById("tab-plaintext").click();

                $(".booktile").click(function(){
                    
                      if ($(this).attr('data-book-active')) {
                        $(this).removeAttr('data-book-active'); // Toggle attribute
                    } else {
                        $(this).attr('data-book-active',"on");
                    }
                });

        });

    // Check if range sliders change and update percentage blend
    function setPercentages () {
                var ulSlide = parseInt(get_ulysses_slider());  // Turn these into integers. So some poor unnamed soul doesn't spend an hour wondering why basic maths doesn't work. It was me.
                var erSlide = parseInt(get_ero_slider());
                var total = ulSlide +  erSlide;
                var percentageUly = ( ulSlide  / total * 100 ).toFixed(2);
                var percentageEro = ( erSlide / total * 100  ).toFixed(2);
                var percentage = percentageUly + "% / " + percentageEro + "%" ;
                $('#percentage-counter').html(percentage);
    };