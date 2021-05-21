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
}


