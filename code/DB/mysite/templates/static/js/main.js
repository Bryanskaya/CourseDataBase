function HiddenFields(){
    var elem = document.getElementById("role").value;
    if (elem === 'hunter' || elem === 'охотник')
    {
        document.getElementById("add-info").style.display = "flex";
        document.getElementById("label-info").style.display = "block";
        document.getElementById("ticket_num").style.display = "block";
        document.getElementById("address").style.display = "block";

        document.getElementById("ticket_num").required = true;
        document.getElementById("address").required = true;
    }
    else
    {
        document.getElementById("add-info").style.display = "none";

        document.getElementById("ticket_num").required = false;
        document.getElementById("address").required = false;
    }

    if (elem === 'huntsman' || elem === 'егерь')
    {
        document.getElementById("add-work").style.display = "flex";
        document.getElementById("label-work").style.display = "block";
        document.getElementById("hunting_grounds").style.display = "block";
        document.getElementById("sectors").style.display = "block";

        document.getElementById("hunting_grounds").required = true;
        document.getElementById("sectors").required = true;
    }
    else
    {
        document.getElementById("add-work").style.display = "none";

        document.getElementById("hunting_grounds").required = false;
        document.getElementById("sectors").required = false;
    }
}

function RecoverPassword() {
    var elem = document.getElementById("login").value;

    if (elem === '') {
        document.getElementById("btn-in").click();
    }
    else {
        window.location.href = '/recover_password/' + elem;
    }
}

function Jump(pos) {
    var child = document.getElementById('input-code').childNodes;
    console.log(child);
    if (pos === 7)
        return;
    else
        child[pos + 2].focus();
}


function FindNeed() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("find-voucher-ground");
    filter = input.value;
    table = document.getElementById("list-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.indexOf(filter) > -1) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }       
    }
}

function FindNeedInput() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("find-voucher-ground");
    filter = input.value;
    table = document.getElementById("list-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.indexOf(filter) > -1) {
            tr[i].style.display = "";
            console.log(td.text)
        } 
        else {
            tr[i].style.display = "none";
        }
    }       
    }
}

function RequestVoucher(id) {
    let num = document.getElementById(id).value;

    if (!(0 < num && num < 100 )) {
        num = 0;
    }
    
    window.location.href = '/buy/' + id + '&' + num;
}

function DelRequest(id) {
    window.location.href = '/show/' + id;
}