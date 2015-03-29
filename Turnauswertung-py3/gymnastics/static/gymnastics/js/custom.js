/* Initiate LightTable filter */
$(document).ready(LightTableFilter.init());

/* Handle the data arguments of the delete modal */
$('#delete-modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var id = button.data('id') // Extract info from data-* attributes
  var name = button.data('name')
  var url = button.data('url')

  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.delete-modal-question').text('Are you sure you want to delete \"' + name + '\"?')
  modal.find('.delete-modal-confirm').attr('href', url);
})

/* Delete confirm popup and ajax post delete handling */
$(".confirm").confirm({
    confirm: function(button) {
        var buttonText = button.attr('href');

        console.log('Button function with ' + buttonText);

        ajaxDelete(buttonText);
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

// $(document).ready(function() {
//     var csrftoken = getCookie('csrftoken');

//     function csrfSafeMethod(method) {
//         // these HTTP methods do not require CSRF protection
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//     }

//     $.ajaxSetup({
//         crossDomain: false, // obviates need for sameOrigin test
//         beforeSend: function(xhr, settings) {
//             if (!csrfSafeMethod(settings.type)) {
//                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
//             }
//         }
//     });
// });

function ajaxDelete(href) {
    console.log("AjaxDelete with " + href);

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var posting = $.ajax({
        type:"POST",
        url:href,
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    posting.fail(function() {
        // find out what the actual problem is!

        // handle unexpected error here
        // TODO: ...
        alert("posting.fail");
    });

    posting.done(function(data) {
        if (data.result == "ok"){
            alert("posted with result ok");
        } else {
            // handle error processed by server here
            alert("posting with result NOT ok");
        }
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