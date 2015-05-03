var json;
$.getJson("data.js", function(data){
    json = data;
});

<script>
(function() {
  var SbuxLocations = "put in the url with the data from my website after it's uploaded here";
  $.getJSON( SbuxLocations, {
    format: "json"
  })
    .done(function( data ) {
      $.each( data.items, function( i, item ) {
        $( "not sure what does here" ).attr( "src", item.media.m ).appendTo( "not sure what goes here either" );
        if ( i === 3 ) {
          return false;
        }
      });
    });
})();
</script>
