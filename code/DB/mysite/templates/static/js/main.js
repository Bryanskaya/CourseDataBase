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

//function GetSectors() {
//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//
//    var elem = document.getElementById("hunting_grounds").value;
//    console.log(elem);
//
//    const request = new XMLHttpRequest();
//    const url = "get_sectors/";
//    const params = "id=" + elem;
//
//    request.responseType =	"json";
//    request.open("POST", url, true);
//    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//    request.setRequestHeader("X-CSRFToken", csrftoken);
//
//    request.addEventListener("readystatechange", () => {
//
//    if (request.readyState === 4 && request.status === 200) {
//        let obj = request.response;
//
//        console.log(obj.id);
//
//        var docfrag = document.createDocumentFragment();
//
//        for (var i = 0; i < obj.id.length; i++)
//        {
//             docfrag.appendChild(new Option(obj.id[i], obj.id[i]));
//        }
//
//        var select = document.getElementById("sectors");
//        select.innerHTML = "";
//
//        if (obj.id.length === 0) {
//            select.appendChild(new Option("Нет доступных", null));
//        }
//        else {
//            select.appendChild(docfrag);
//        }
//	}
//});
//    console.log(document.getElementById("sectors"));
//    request.send(params);
//}

