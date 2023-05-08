const ENTER_KEY_CODE = 13;

function ModifyEnterKeyPressAsTab(event) {
    var caller;
    var key;
    if (window.event) {
        caller = window.event.srcElement; //Get the event caller in IE.
        key = window.event.keyCode; //Get the keycode in IE.
    } else {
        caller = event.target; //Get the event caller in Firefox.
        key = event.which; //Get the keycode in Firefox.
    } if (key == ENTER_KEY_CODE) { //Enter key was pressed.
        event.preventDefault();
        cTab = caller.tabIndex; //caller tabIndex.
        maxTab = 0; //highest tabIndex (start at 0 to change)
        minTab = cTab; //lowest tabIndex (this may change, but start at caller)
        allById = document.getElementsByTagName("input"); //Get input elements.
        allByIndex = []; //Storage for elements by index.
        c = 0; //index of the caller in allByIndex (start at 0 to change)
        i = 0; //generic indexer for allByIndex;
        for (id in allById) { //Loop through all the input elements by id.
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
        for (tab = cTab; tab <= maxTab; tab++) {
            //Look for this tabIndex from the caller to the end of page.
            for (i = c + 1; i < allByIndex.length; i++) {
                if (allByIndex[i].tabIndex == tab) {
                    allByIndex[i].focus(); //Move to that element and stop.
                    return;
                }
            }
            //Look for the next tabIndex from the start of page to the caller.
            for (i = 0; i < c; i++) {
                if (allByIndex[i].tabIndex == tab + 1) {
                    allByIndex[i].focus(); //Move to that element and stop.
                    return;
                }
            }
            //Continue searching from the caller for the next tabIndex.
        }

        //The caller was the last element with the highest tabIndex,
        //so find the first element with the lowest tabIndex.
        for (i = 0; i < allByIndex.length; i++) {
            if (allByIndex[i].tabIndex == minTab) {
                allByIndex[i].focus(); //Move to that element and stop.
                return;
            }
        }
    }
}
