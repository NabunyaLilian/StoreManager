

function loginUser(){
var username = document.getElementById('email').value;
var password = document.getElementById('password').value;
alert(username);
alert(password);
const data = {"username":username, "password":password};


fetch('https://lilianstoremanager-api.herokuapp.com/api/v2/auth/login', {
method: 'POST',
headers: {
'Accept': 'application/json',
'Content-Type': 'application/json'
},
cache: 'no-cache',
body: JSON.stringify(data)
})
.then((res) => res.json())
.then(result => {
// if(result.status_code === 200){
// if(result['User']['username'] == "lianda"){
//     localStorage.setItem("access-token",result.Access_token);
//     window.location.href = 'admin_index.html';
// }
// else{
//     localStorage.setItem("access-token",result.Access_token);
//     window.location.href = 'store_attendant_index.html';
// }
// }
alert(result);

})

}

function RegisterUser(){
var username = document.getElementById('username').value;
var firstname = document.getElementById('firstname').value;
var password = document.getElementById('password').value;
var isadmin = document.getElementById('isadmin').value;
const data = {"username":username, "firstname":firstname, "password":password, "isadmin":isadmin};

fetch('https://lilianstoremanager-api.herokuapp.com/api/v2/auth/signup', {
method: 'POST',
headers: {
'Accept': 'application/json',
'Content-Type': 'application/json'
},

cache: 'no-cache',
body: JSON.stringify(data)
})
.then((res) => res.json())
.then(result => {
if(result.status_code === 201){
alert(result.Message)
}
else{
alert(result.Message)
}

})

}
