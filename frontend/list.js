var ApiEndPoint = "http://133.242.53.17";

function generateTbody(hubotId){
var listHTML = "\n";
listHTML += "<tr>\n" ;
listHTML += "<td>" + hubotId + "</td>\n";
listHTML += "<td id='st_" + hubotId + "'>OFF</td>\n";
listHTML += "<td>\n";
listHTML += "<button class=\"btn btn-default edit\">Edit</button>\n";
listHTML += "<button class=\"btn btn-info\" hidden id='start_" + hubotId + "'>Start</button>\n";
listHTML += "<button class=\"btn btn-warning hidden\" id='stop_" + hubotId + "'>Stop</button>\n";
listHTML += "</td>\n";
listHTML += "</tr>\n";
    return(listHTML);
}

function getStatus(APIKey,hubotId){
    var status = "OPPAI";
    	$.ajax({
        type: "GET",
	url: ApiEndPoint + "/hubot/" + hubotId + "/status",
	data:{
	    apikey: APIKey
	    },
	dataType: "json",
	success: function(data){
	    if(data.status){
		var status = data.message;
		var st_id = "#st_" + hubotId;
		var start_id = "#start_" + hubotId;
		var stop_id = "#stop_" + hubotId;
		if(status){
	            $(st_id).text("Running");
		    $(start_id).addClass("hidden");
		    $(stop_id).removeClass("hidden");
		}else{
	            $(st_id).text("Exited");
		    $(start_id).removeClass("hidden");
		    $(stop_id).addClass("hidden");
		}
	    }
	}
    });
}



$(document).ready(function(){
    var SESSID = $.cookie("SESSID");
    if(SESSID !== undefined){
        $.ajax({
            type: "GET",
	        url: ApiEndPoint + "/user/hubot/list",
	        data:{
	            apikey: SESSID
	        },
	        dataType: "json",
	        success: function(data){
	            console.log(data.status);
		    var hubotIds = data.message;
		    for (var i=0; i < hubotIds.length; i++){
                        $(".hubot-list-tbody").append(generateTbody(hubotIds[i]));
                        getStatus(SESSID,hubotIds[i]);
     			console.log(hubotIds[i]);
		    } 
	        }
        });
    }else{
        location.href = "../login/";
    }
});

$(".logout").on("click",function(){
    $.cookie("SESSID",'',{expires: -1 ,path: "/"});
    location.href = "../login/";
});
