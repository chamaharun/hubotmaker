var ApiEndPoint = "http://133.242.53.17/";

$(".create-new").on("click", function() {
    $('#CreateModal').modal("show")
});
$(".edit").on("click", function() {
    $('#EditModal').modal("show")
});
$(".delete").on("click", function() {
    $('#DeleteConfirm').modal("show")
});
$(".UserRegistSubmit").on("click", UserRegistSubmit);



function UserRegistSubmit() {

    $.ajax({
        type: "POST",
        url: ApiEndPoint + "user",
        cache: false,
        data: {
            username: $("#Username").val(),
            password: $("#Password").val()
        },
        success: function(data) {
		console.log(data);
    		if (data.status == true) {
                alert("submitted")
                UserActivate();
            } else {
                $("#Username").addClass("has-error");
                $("#Password").addClass("has-error");
            }
	}
    });
}

function UserActivate() {

    $.ajax({
        type: "PUT",
        url: ApiEndPoint + "user/activate",
        cache: false,
        data: {
            username: $("#Username").val(),
            password: $("#Password").val()
        },
    }).done(function(data) {
        if (data.status == "ture") {
            RegisterCompleted();
        }
    });
}

function RegisterCompleted() {
    $("RegisterCompleted").removeClass("hidden");
}

//$(".UserRegistSubmit").on("click",UserRegistSubmit());
