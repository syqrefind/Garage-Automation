//crsf
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

//post to removeVehicle
function removeVehicle(accountId,pk,licensePlate){
    var answer = confirm("Remove " + licensePlate + "?");
    if (answer){
        $.ajax({
            'url': "/garageAutomation/home/",
            'type': 'POST',
            'data':{
                'csrfmiddlewaretoken':getCookie('csrftoken'),
                'removeVehicle': 'true',
                'account_id':accountId, 
                'license_plate':licensePlate,
                'vehicle_pk':pk
            },
            'success': function(result){
            location.reload();
        }});
    }
}