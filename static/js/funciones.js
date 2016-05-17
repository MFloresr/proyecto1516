$(document).ready(function() {
    var time = setTimeout(eliminarAlertes, 5000);
    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }
    $(".navbar-nav").children().on("click", function(){
        $(this).addClass("active");
    })
});   