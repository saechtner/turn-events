/* Initiate LightTable filter */
$(document).ready(LightTableFilter.init());

/* Handle the data arguments of the delete modal */
$('#delete-modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var id = button.data('id') // Extract info from data-* attributes
  var name = button.data('name')

  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.delete-modal-question').text('Are you sure you want to delete \"' + name + '\"?')
})


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

    // This function must be customized
    var onDelete = function(){
        $.post(this.href, function(data) {
            if (data.result == "ok"){
                alert("data deleted successfully");
            } else {
                // handle error processed by server here
                alert("smth goes wrong");
            }
        }).fail(function() {
            // handle unexpected error here
            // TODO: ...
            alert("error");
        });
        return false;
    }

    // $(".delete-modal-confirm").click(onDelete);
    $(".athlete-detail-delete").click(onDelete);
});