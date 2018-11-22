

function loginUser(){
var Username = document.getElementById('username').value;
var Password = document.getElementById('password').value;

const data = {"Username":Username, "Password":Password};


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
if(result['Message'] === "Login successful"){
    if(result['User']['username'] == 'lianda'){
        localStorage.setItem("access-token",result['Access_token']);
        window.location.href = 'admin_index.html';
    }
    else{
        localStorage.setItem("access-token",result['Access_token']);
        window.location.href = 'store_attendant_index.html';
}
}

})

}

function RegisterUser(){
var Username = document.getElementById('username').value;
var FirstName = document.getElementById('firstname').value;
var Password = document.getElementById('password').value;
var isAdmin = document.getElementById('isadmin').value;
const data = {"Username":Username, "FirstName":FirstName, "Password":Password, "isAdmin":isAdmin};
alert(JSON.stringify(data))
fetch('https://lilianstoremanager-api.herokuapp.com/api/v2/auth/signup',
{
    method:'POST',
    body: JSON.stringify(data),
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        "Authorization":  localStorage.getItem("access-token")
    },
    cache:'no-cache'
})
.then((res) => res.json())
alert(res)
.then(result => {
    if(result['User']['Username'] === Username){
        alert(result['Message'])
    }
    else{
        alert(result['Message'])
    }

})

}
