function open_nutrition(){
    document.getElementById("nutrition_parameters").style.width = "75em";
}

function close_nutrition(){
    document.getElementById("nutrition_parameters").style.width = "0px";
}

function sort_table_alphabetically_by_name(){
    col = 1
    var table, rows, i, x, y;

    table = document.getElementById("item_selection_table")
    rows = table.rows

    switching = true;

    while(switching) {

        switching = false;

        for (i = 1; i < (rows.length) - 1; i++) {


            x = rows[i].getElementsByTagName("td")[col];
            y = rows[i + 1].getElementsByTagName("td")[col];

            if(x.innerText.toLowerCase() > y.innerText.toLowerCase()) {
                switching = true;
                break
            }
        }
        if(switching){
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        }
    }
}

function sort_numerically_by_column(col){
    var table, rows, i, x, y, switching;

    table = document.getElementById("item_selection_table")
    rows = table.rows

    switching = true;

    while(switching) {

        switching = false;

        for (i = 1; i < (rows.length) - 1; i++) {


            x = rows[i].getElementsByTagName("td")[col].innerText;
            y = rows[i + 1].getElementsByTagName("td")[col].innerText;

            if(x.substring(0, 1).localeCompare("$") === 0){
                x = x.substring(1)
                y = y.substring(1)
            }

            if(parseFloat(x) > parseFloat(y)) {
                switching = true;
                break
            }
        }
        if(switching){
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        }
    }
}
