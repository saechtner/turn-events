/* Initiate LightTable filter */
$(document).ready(LightTableFilter.init());


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


/* Table Sorter Functions*/
function reversedSorter(a, b) {
    var a_trimmed = a.trim();
    var b_trimmed = b.trim();
    
    if (a_trimmed && b_trimmed) {
        if (a_trimmed < b_trimmed) return 1;
        if (a_trimmed > b_trimmed) return -1;
    } else {
        if (a_trimmed) return 1;
        if (b_trimmed) return -1;
    }
    
    return 0;
}

function regularStringSorter(a, b) {
    var a_trimmed = a.trim().toLowerCase();
    var b_trimmed = b.trim().toLowerCase();

    return b_trimmed.localeCompare(a_trimmed);
}