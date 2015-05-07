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


/* Initiate jQuery drag sorter */
$(document).ready(function() { 
    // $("#available-list").dragsort();   

    function saveOrder() {
        var data = $("#chosen-list li").map(function() { 
            return $(this).data('itemidx'); 
        }).get();
        $("input[name=chosen_list_order]").val(data.join(" "));
    };

    $("#chosen-list, #available-list").dragsort({ 
        dragSelector: "div", 
        dragBetween: true, 
        dragEnd: saveOrder, 
        placeHolderTemplate: "<li class='placeHolder'><div></div></li>"
    });
});

/* Delete confirm popup and ajax post delete handling */
$(document).ready(function() { 
    $(".confirm").confirm({
        confirm: function(button) {
            var href = button.attr('href');
            var id = button.data('id');

            ajaxDelete(href, id);
        },
    });
});

$(document).ready(function() {
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
    };

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
};

function ModifyEnterKeyPressAsTab(event)
{
    var caller;
    var key;
    if (window.event)
    {
        caller = window.event.srcElement; //Get the event caller in IE.
        key = window.event.keyCode; //Get the keycode in IE.
    }
    else
    {
        caller = event.target; //Get the event caller in Firefox.
        key = event.which; //Get the keycode in Firefox.
    }
    if (key == 13) //Enter key was pressed.
    {
        event.preventDefault();
        cTab = caller.tabIndex; //caller tabIndex.
        maxTab = 0; //highest tabIndex (start at 0 to change)
        minTab = cTab; //lowest tabIndex (this may change, but start at caller)
        allById = document.getElementsByTagName("input"); //Get input elements.
        allByIndex = []; //Storage for elements by index.
        c = 0; //index of the caller in allByIndex (start at 0 to change)
        i = 0; //generic indexer for allByIndex;
        for (id in allById) //Loop through all the input elements by id.
        {
            allByIndex[i] = allById[id]; //Set allByIndex.
            tab = allByIndex[i].tabIndex;
            if (caller == allByIndex[i])
                c = i; //Get the index of the caller.
            if (tab > maxTab)
                maxTab = tab; //Get the highest tabIndex on the page.
            if (tab < minTab && tab >= 0)
                minTab = tab; //Get the lowest positive tabIndex on the page.
            i++;
        }
        //Loop through tab indexes from caller to highest.
        for (tab = cTab; tab <= maxTab; tab++)
        {
            //Look for this tabIndex from the caller to the end of page.
            for (i = c + 1; i < allByIndex.length; i++)
            {
                if (allByIndex[i].tabIndex == tab)
                {
                    allByIndex[i].focus(); //Move to that element and stop.
                    return;
                }
            }
            //Look for the next tabIndex from the start of page to the caller.
            for (i = 0; i < c; i++)
            {
                if (allByIndex[i].tabIndex == tab + 1)
                {
                    allByIndex[i].focus(); //Move to that element and stop.
                    return;
                }
            }
            //Continue searching from the caller for the next tabIndex.
        }

        //The caller was the last element with the highest tabIndex,
        //so find the first element with the lowest tabIndex.
        for (i = 0; i < allByIndex.length; i++)
        {
            if (allByIndex[i].tabIndex == minTab)
            {
                allByIndex[i].focus(); //Move to that element and stop.
                return;
            }
        }
    }
}

$(document).ready(function() {
    function scrollResponse(element, transform_value) {
        if (transform_value) {
            element.css("transform", "translate3d(0px, " + transform_value + "px, 0px)");
        } else {
            element.css("transform", "none");
        }
    }

    $(window).scroll(function() {
        var scroll_limit = 160;

        var scroll_top = $(window).scrollTop();

        var page_header_div = $(".page-header:first");
        var is_locked = page_header_div.hasClass("is-locked");
        var page_header_bg_img = page_header_div.find(".page-header-bg-img:first");

        if (scroll_top == 0) {
            scrollResponse(page_header_bg_img, null);
        } else if (scroll_top < scroll_limit) {
            if (is_locked) {
                page_header_div.removeClass("is-locked");
            }
            scrollResponse(page_header_bg_img, scroll_top/5);
        } else if (scroll_top >= scroll_limit && !is_locked) {
            page_header_div.addClass("is-locked");
            scrollResponse(page_header_bg_img, scroll_limit/5);
        }
    });
});
