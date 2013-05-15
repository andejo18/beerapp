

lightbeers = ["pilsner","lager","paleale"]

darkbeers = ["stout","brownale","porter"]

$(document).ready(function()
{
    $(this)
    // $('#button1').click(function() 
    // {
    //     console.log("shit, mane")
    //     $.getJSON('/beerme/main/dbquery', function(data)  
    //     {
    //         console.log(data)
    //     })
    // });

    $('div .tierone').one("click", function() {
        // corrlistst = $(this).attr('id') + beers

        buttonid = $(this).attr('id')

        // console.log($(this).id + " was clicked")

        console.log(buttonid)

        $(this).siblings("div").hide()

        if (buttonid == "light") {
            selbeers = lightbeers
        }
        else 
        {
            selbeers = darkbeers
        }
        for (anitem in selbeers) {
            $(this).append("<div style='display: none;' class='tiertwo' id='" + selbeers[anitem] + "'><h3>" + selbeers[anitem] + "</h3></div>")
            $(this).find(".tiertwo:last").fadeIn("slow");
            
        }
        tiertwoinit()

    });



});
function tiertwoinit()
{
    $('div .tiertwo').click(function() {
        console.log("two clicked")
        console.log($(this).attr('id'))
        
    })
}
