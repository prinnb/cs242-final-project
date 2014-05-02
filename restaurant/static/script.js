$(document).ready(function(){
	$(".iframe_popup").colorbox({iframe:true, width:"80%", 
    height:"80%", onCleanup:function(){ location.reload(); }});
});

function click_like_btn(num_other_like, food_menu_id) {
	var id = $(this).attr("id");
  var div_selector = $("#like_status_" +food_menu_id);

	var jqxhr = $.ajax( {
      type: "POST",
      url: "/restaurant/like/" + food_menu_id +"/",
      data: {num_other_like : num_other_like, 
      		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value }
    } );
    jqxhr.done(function(data) {
   	  div_selector.html(data);
	  })
    jqxhr.fail(function(jqXHR) {
		  alert( jqXHR.statusText );
    })

}