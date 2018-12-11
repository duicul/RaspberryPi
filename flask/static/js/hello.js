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
 {setInterval(board_status,period);}
 
 function board_status()
 {$.ajax({url: "/board_status", success: function(result){
       $("#board_status").html(result+" "+ind);
	   ind++;
    }});
	 
	 
 }
 
 function loginstatus(){
 $.ajax({url: "/loginstatus.py", success: function(result){
       alert(result);
    }});
	/*$.ajax({url: "demo_test.txt", success: function(result){
        $("#div1").html(result);
    }});*/
 } 
