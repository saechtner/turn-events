jQuery(document).ready(function($) {

    /* Try activating tab based on url hash */
    $(function(){
        var hash = window.location.hash;
        if (hash && $(hash)) {
            $('a[href="' + hash + '"]').tab('show');
        }
    });

    /* Initiate Light filters */
    LightFilter.init()

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

    // Intialize the table sorter of table-results-athletes
    var column_count = $("#table-results-athletes").find("tr:first th").length;
    var last_column_index = column_count - 1;
    var headers = {} 
    for (i = 2; i < column_count; i += 1) {
        headers[i] = (i % 2 == 1) ? { sorter: 'ranks' } : { sorter: false }
    }

    $("#table-results-athletes").tablesorter({
        // sort on the first column and third column, order asc 
        sortList: [[last_column_index, 0], [0, 0]],
        headers: headers 
    }); 

    // intialize the table sorter of table-results-teams
    var column_count = $("#table-results-teams").find("tr:first th").length;
    var last_column_index = column_count - 1;
    var headers = {} 
    for (i = 2; i < column_count; i += 1) {
        headers[i] = (i % 2 == 1) ? { sorter: 'ranks' } : { sorter: false }
    }

    $("#table-results-teams").tablesorter({
        // sort on the first column and third column, order asc 
        sortList: [[last_column_index,0],[0,0]],
        headers: headers 
    });  

    /* Initiate jquery.dragsort */
    function saveOrder() {
        var data = $("#chosen-list li").map(function() { 
            return $(this).data('itemidx'); 
        }).get();
        $("input[name=chosen_list_order]").val(data.join(" "));
    };

    $("#chosen-list, #available-list").dragsort({ 
        dragSelector: "li", 
        dragBetween: true, 
        dragEnd: saveOrder, 
        placeHolderTemplate: "<li class='list-group-item'></li>"
    });

    /* Add jquery.dragsort extending click handlers */
    $('#available-list').on('click', 'li', function() {
        $('#chosen-list').append($(this));
        saveOrder();
    });

    $('#chosen-list').on('click', 'li', function() {
        $('#available-list').append($(this));
        saveOrder();
    });

    // Initial saving of the saveOrder.
    saveOrder();

    /* Vertical scroll handling */

    $(window).scroll(function() {
        var scroll_limit = 150;
        var scroll_top = $(this).scrollTop();

        scrollResponseHorizontalFormButtons(scroll_top, scroll_limit);
    });

    function scrollResponseHorizontalFormButtons(scroll_top, scroll_limit) {
        var default_margin_top = 100
        var button_group = $('.btn-group-vertical.vertical-align-center')
        var is_locked = button_group.hasClass("fixed");

        if (button_group) {
            if (!is_locked && scroll_top > scroll_limit) {
                button_group.addClass("fixed");
            } else if (is_locked && scroll_top <= scroll_limit) {
                button_group.removeClass("fixed");
            }
        }
    }

    // media query handling with enquire.js

    var vertically_centered_buttons = $("#btn-group-vertical-align")

    enquire.register("screen and (min-width: 992px)", {

        // OPTIONAL
        // If supplied, triggered when a media query matches.
        match : function() {
            vertically_centered_buttons.removeClass('btn-group btn-group-justified')
            vertically_centered_buttons.addClass('btn-group-vertical')
        },      
                                    
        // OPTIONAL
        // If supplied, triggered when the media query transitions 
        // *from a matched state to an unmatched state*.
        unmatch : function() {
            vertically_centered_buttons.removeClass('btn-group-vertical')
            vertically_centered_buttons.addClass('btn-group btn-group-justified')
        },    
        
        // OPTIONAL
        // If supplied, triggered once, when the handler is registered.
        setup : function() {},    
                                    
        // OPTIONAL, defaults to false
        // If set to true, defers execution of the setup function 
        // until the first time the media query is matched
        deferSetup : true,
                                    
        // OPTIONAL
        // If supplied, triggered when handler is unregistered. 
        // Place cleanup code here
        destroy : function() {}
          
    });
});
