/**
* Original Code adapted from:
* 	http://codepen.io/chriscoyier/pen/tIuBL
*
* Light Table Filter using "fuzzy" search
* 
* - Need JQuery!
* - Adds functionality to all input field -- table pairs on page
* 
* Goal: Insert values in field and filter rows of table by: yes, contains value and: no, doesn't
* 		Hide all rows that don't contain that values.
* 
* Setup: 	1) Add an input for each table like this and edit the data-table attribute: 
*			<input type="search" class="light-table-filter" data-table="HTML CLASS OF TABLE TO BE FILTERED">
*			2) Add a table with <thead> and <tbody> to your html
*			3) Add the above value "HTML CLASS OF TABLE TO BE FILTERED" as class to this table.
*			4) call LightTableFilter.init() on $(document).ready
*			5) use it!
*

EXAMPLE

	<input type="search" class="light-table-filter" data-table="arm_results" name="arm_table_filter">

    <table class="arm_results">
        <thead>
            <tr>
                <th>Drugs</th>
                <th>Side Effects</th>
                <th>Support</th>
                <th>Confidence</th>
                <th>Lift</th>
            </tr>
        </thead>
        <tbody>
            <!--
            <tr>
                <td>drug1</td>
                <td>se1</td>
                <td>supp1</td>
                <td>conf1</td>
                <td>lift1</td>
            </tr>
            <tr>
                ........
            </tr>
            -->
        </tbody>
    </table>
*
*
*
**/

var LightTableFilter = function(Arr) {

	var _input;

	function _onInputEvent(e) {
		_input = e.target;
		var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
		Arr.forEach.call(tables, function(table) {
			Arr.forEach.call(table.tBodies, function(tbody) {
				Arr.forEach.call(tbody.rows, _filter);
			});
		});
	}

	function _filter(row) {
		var text = row.textContent.toLowerCase()
        var val = _input.value.toLowerCase();
		row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
	}

	function init_light_table_filter() {
		var inputs = document.getElementsByClassName('light-table-filter');
		Arr.forEach.call(inputs, function(input) {
			input.oninput = _onInputEvent;
		});
	}

	return {
		'init': init_light_table_filter 
	};

}(Array.prototype);

