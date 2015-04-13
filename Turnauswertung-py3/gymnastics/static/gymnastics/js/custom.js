/* Initiate LightTable filter */
$(document).ready(LightTableFilter.init());

/* Initiate jQuery table sorter */
$(document).ready(function() { 
    /* Add jQuery table sorter parser */
    $.tablesorter.addParser({ 
        // set a unique id 
        id: 'ranks', 
        is: function(s) { 
            // return false so this parser is not auto detected 
            return false; 
        }, 
        format: function(s) {
            var s_trimmed = s.trim()

            if (s_trimmed) {
                return s_trimmed;
            }
            return Number.MAX_VALUE.toString();
        }, 
        // set type, either numeric or text 
        type: 'numeric' 
    }); 

    // intialize the table sorter of table-results-athletes
    var column_count = $("#table-results-athletes").find("tr:first th").length;
    var last_column_index = column_count - 1;
    var headers = {} 
    for (i = 2; i < column_count; i += 2) {
        headers[i] = { sorter: 'ranks' }
    }

    $("#table-results-athletes").tablesorter({
        // sort on the first column and third column, order asc 
        sortList: [[last_column_index,0],[0,0]],
        headers: headers 
    }); 

    // intialize the table sorter of table-results-teams
    var column_count = $("#table-results-teams").find("tr:first th").length;
    var last_column_index = column_count - 1;
    var headers = {} 
    for (i = 2; i < column_count; i += 2) {
        headers[i] = { sorter: 'ranks' }
    }

    $("#table-results-teams").tablesorter({
        // sort on the first column and third column, order asc 
        sortList: [[last_column_index,0],[0,0]],
        headers: headers 
    }); 
}); 

/* Delete confirm popup and ajax post delete handling */
$(".confirm").confirm({
    confirm: function(button) {
        var href = button.attr('href');
        var id = button.data('id');

        ajaxDelete(href, id);
    },
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

function ajaxDelete(href, id) {
    var posting = $.ajax({
        type: 'post',
        url: href,
        crossDomain: false
    });

    posting.done(function(data) {
        if (data.result == "ok"){
            $("#athletes_row_" + id).addClass("hidden")
        } else {
            // handle error processed by server here
            alert("posting with result NOT ok");
        }
    });

    posting.fail(function() {
        // handle unexpected error here
        alert("posting.fail");
    });

    return false;
}