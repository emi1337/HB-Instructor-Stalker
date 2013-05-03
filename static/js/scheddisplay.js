jQuery(document).ready(function(){
	startFresh();
})

function startFresh() {
	$("#checkins").hide();
	$("#fullsched").show();

	$("#christian-checkin-options").hide();
	$("#christian-checkout").hide();
	$("#christian-full-checkout").hide();

	$("#liz-checkin-options").hide();
	$("#liz-checkout").hide();
	$("#liz-full-checkout").hide();

	$("#cynthia-checkin-options").hide();
	$("#cynthia-checkout").hide();
	$("#cynthia-full-checkout").hide();

	$("#nick-checkin-options").hide();
	$("#nick-checkout").hide();
	$("#nick-full-checkout").hide();
}

// event listeners
$("#view-checkins").on('click', function(e){
	e.preventDefault();
	$("#checkins").show();
	$("#fullsched").hide();
})

$("#view-fullsched").on('click', function(e){
	e.preventDefault();
	$("#checkins").hide();
	$("#fullsched").show();
})

//christian buttons
$("#christian-checkin").on('click', function(e){
	e.preventDefault();
	$("#christian-checkin").hide();
	$("#christian-checkin-options").show();
})

$("#christian-in-office").on('click', function(e){
	e.preventDefault();
	$("#christian-checkin-options").hide();
	$("#christian-checkout").show();
	$("#christian-status").text("Christian is in the office!");
})

$("#christian-can-contact").on('click', function(e){
	e.preventDefault();
	$("#christian-checkin-options").hide();
	$("#christian-checkout").show();
	$("#christian-status").text("Christian is not in the office, but you can contact him online.");
})

$("#christian-checkout").on('click', function(e){
	e.preventDefault();
	$("#christian-checkout").hide();
	$("#christian-checkin-options").show();
	$("#christian-full-checkout").show();

})

$("#christian-full-checkout").on('click', function(e){
	e.preventDefault();
	$("#christian-checkin-options").hide();
	$("#christian-full-checkout").hide();
	$("#christian-checkout").hide();
	$("#christian-checkin").show();
	$("#christian-status").text("Christian is doing his own thang right now.");
	var christian = document.getElementById("")


})


//liz buttons


//cynthia buttons


//nick buttons

function changeBW() {

}

function changeColor() {

}