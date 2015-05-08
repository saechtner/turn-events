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
    for (i = 1; i < column_count; i += 1) {
        headers[i] = (i % 2 == 0) ? { sorter: 'ranks' } : { sorter: false }
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
    for (i = 1; i < column_count; i += 1) {
        headers[i] = (i % 2 == 0) ? { sorter: 'ranks' } : { sorter: false }
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
