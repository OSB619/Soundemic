function verifyPassword() {  
  var pw = document.getElementById("password").value;  
  var pwc = document.getElementById("confirm-password").value;
  var verified="Good"
  alert(pw);

  //check empty password field  
  if(pw == "") {  
     document.getElementById("message").innerHTML = "**Fill the password please!"; 
     document.getElementById("submit").value="bad";
     return false;  
  }  
   
 //minimum password length validation  
  if(pw.length < 8) {  
     document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters"; 
     document.getElementById("submit").value="bad";
     return false;  
  }  
  
//maximum length of password validation  
  if(pw.length > 15) {  
     document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";
     document.getElementById("submit").value="bad";  
     return false;  
  }

  if(pw!=pwc){
    document.getElementById("message").innerHTML="!!!!Password does not match... try again...";
    document.getElementById("submit").value="bad";
    return false;

  }

}  

function myFunction(){
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}