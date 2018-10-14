 // get the form
  const form = document.querySelector("form");
  // get username by selecting input id
  const username = document.querySelector("#username");
  // get password by selecting input id
  const password = document.querySelector("#password"); 

  // prevent form behaviour which is submitting somewhere
  form.addEventListener("submit", function(e){
      e.preventDefault() // do nothing
    // check if username is admin and password is 123
    if(username.value ==="admin" && password.value ==="123"){
      //send user to admin dashboard
      location = "admin_index.html";
    }
    else if(username.value ==="Lia" && password.value !=="password"){
       // wrong password so inform user
      alert("Invalid password") // can be replaced by a span tag
    }
    else{
     // user is not admin so send them to attendant
     location = "store_attendant_index.html";
    }
  
});
