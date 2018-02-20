function awesome() {
    $('#but').toggleClass("btn-success").toggleClass("btn-danger");
    /*$('span').toggleClass("glyphicon-ok").fadeToggle("slow", 2000);
    $('span').toggleClass("glyphicon-ok").fadeToggle("slow").toggleClass("glyphicon-remove").fadeToggle("slow");*/
    /*$('span').fadeToggle("slow").toggleClass("glyphicon-remove").setTime(2000);*/
    $('span').fadeToggle(1000, function(){
        $(this).toggleClass("glyphicon-ok").toggleClass("glyphicon-remove");
    }).fadeToggle()

}