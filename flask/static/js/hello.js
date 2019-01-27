var interval_calls;
function hello(){
alert("hello");
$("#messfunc").html("hello");
 //document.getElementById("messfunc").innerHTML = "hello";
 }

function goodbye(){
 alert("goodbye");
 $("#messfunc").html("goodbye");
 //document.getElementById("messfunc").innerHTML = "goodbye";
 } 
 var ind=0;

 function init_server(period)
 {//interval_calls=setInterval(ajax_calls,period);
  }

function login()
{}


function ajax_calls(){
board_status();
update_data();
}

function stopajaxcalls()
{clearInterval(interval_calls);}

function getconfigdata()
 {$.ajax({url: "/getconfigdata", success: function(result){
       $("#config").html(result);}});}
	   
function setconfigdata()
 {$.post("/setconfigdata",{user:$("#username").val(),pass:$("#password").val(),ip:$("#ip").val(),port:$("#port").val()}, success: function(result){
       alert("Config changed");}});}

 function board_status()
 {$.ajax({url: "/board_status", success: function(result){
       $("#board_status").html(result+" "+ind);
	   ind++;}});	 }

function update_data(){
  $.ajax({url:"/data_retr",success : function(result)
     {$("#data_status").html(result+" "+ind);}});  }

 function loginstatus(){
 $.ajax({url: "/loginstatus.py", success: function(result){
       alert(result);
    }}); } 
