jQuery().ready(function(){
  var tabMarque=[];
  $.getJSON('test.json', function(data) {
    $.each(data, function(index, val) {
      tabMarque[index]=val;
    });
  });
console.log(tabMarque);
  $('#Marque').change(function(event) {
    $marque=$(this).val();
    $htmlOption='<option value="0">State</option>';
    if($marque!=0)
      {
        $.each(tabMarque[$marque], function(key, value) {
          $('#Serie').append($('<option></option>').val(val[1]).html(text));
        });
      }
      $('#Serie').html($htmlOption);
  });
});
