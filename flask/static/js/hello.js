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
 
 function loginstatus(){
 $.ajax({url: "/loginstatus.py", success: function(result){
       alert(result);
    }});
	/*$.ajax({url: "demo_test.txt", success: function(result){
        $("#div1").html(result);
    }});*/
 } 
