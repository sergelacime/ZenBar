(function($) {
    "use strict"

    var table = $('#example-advance-1').DataTable();
     
    $('#example-advance-1 tbody').on('click', 'tr', function () {
        var data = table.row( this ).data();
        alert( 'Vous avez cliquer sur '+data[0]+'\'s ligne' );
    });


    var eventFired = function ( type ) {
        var n = $('#demo_info')[0];
        n.innerHTML += '<div>'+type+' event - '+new Date().getTime()+'</div>';
        n.scrollTop = n.scrollHeight;      
    }
 
    $('#example-advance-2')
        .on( 'order.dt',  function () { eventFired( 'Order' ); } )
        .on( 'search.dt', function () { eventFired( 'Recherche' ); } )
        .on( 'page.dt',   function () { eventFired( 'Page' ); } )
        .DataTable();


    $('#example-advance-3').DataTable( {
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/German.json"
        }
    });

})(jQuery);