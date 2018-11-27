// function to log in a user

function loginUser(){
var Username = document.getElementById('username').value;
var Password = document.getElementById('password').value;
const data = {"Username":Username, "Password":Password};

fetch('http://127.0.0.1:5000/api/v2/auth/login', {
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
        localStorage.setItem("access-token",'Bearer '+result['Access_token']);
        window.location.href = 'admin_index.html';
    }
    else{
        localStorage.setItem("access-token",'Bearer '+result['Access_token']);
        window.location.href = 'store_attendant_index.html';
}
}

})

}

// function to fetch users

fetch('http://127.0.0.1:5000/api/v2/products', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        "Authorization": localStorage.getItem("access-token")
    },
    cache: 'no-cache'
    
})
    .then((res) => res.json())
    .then(result => {
        if(result.status === 200){
                var i = 0;
                var table = '<table>'+
                            '<tr>'+
                            '<th>Product_Id</th>'+
                            '<th>Name</th>'+
                            '<th>Quantity</th>'+
                            '<th>Price</th>'+
                            '<th>Minimum Quantity</th>'+
                            '<th>Category</th>'+
                            '<th>Options</th>'+
                           ' </tr>'  ;               
                for(i=0; i < result[Products].length; i++){
                    products +=  '<tr><td>'+result[Products][i]["product_id"]+'</td><td>'+result[Products][i]["name"]+'<td>'+result[Products][i]["quantity"]+'</td><td>'+result[Products][i]["price"]+'</td><td>'+result[Products][i]["min_quantity"]+'</td><td>'+result[Products][i]["category"]+ '<button id="editBtn" class="button" >Edit</button>&nbsp &nbsp  <button id = "delete-button"  onclick = "mydeleteFunction(), DeleteProduct()">Delete</button>';
                }
                document.getElementById("products_table").innerHTML = products+"</table>";
        }
        else{
            // alert(result.status);
        }
        
    })



//function to register a user

function RegisterUser(event){
event.preventDefault();    
var Username = document.getElementById('username').value;
var FirstName = document.getElementById('firstname').value;
var Password = document.getElementById('password').value;
var isAdmin = document.getElementById('isadmin').value;
const data = {"Username":Username, "FirstName":FirstName, "Password":Password, "isAdmin":isAdmin};
// alert(JSON.stringify(data))
// alert(localStorage.getItem("access-token"))
fetch('http://127.0.0.1:5000/api/v2/auth/signup',
{
    method:'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        "Authorization":  localStorage.getItem("access-token")
    },
    body: JSON.stringify(data),
    cache:'no-cache'
})
.then(function(res){
    return res.json()
})
.then(function(result){
    
    if(result['User']['Username'] === Username){
        alert(result['Message'])
    }
    else{
        alert('something went wrong try again')
    }

})

}

// method to give admin rights
function GiveRights(user_id){
    fetch('http://127.0.0.1:5000/api/v2/admin/'+user_id,
    {
        method:'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization":  localStorage.getItem("access-token")
        },
        cache:'no-cache'
    })
    .then((res) => res.json())
    .then(result => {
        if(result['Message'] == "New admin created"){
            alert(JSON.stringify(result['Message']))
        }
        else{
            alert("Something went wrong try again")
        }
    
    })
    
    }
    
function myRightsFunction() {
    confirm("Are you sure you want to give admin rights");
}      


//  method to fetch products 
    
fetch('http://127.0.0.1:5000/api/v2/users', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        "Authorization": localStorage.getItem("access-token")
    },
    cache: 'no-cache'
    
})
    .then((res) => res.json())
    .then(result => {
                var i = 0;
                var users = '<table border="1" id = "store_attendants">'+
                            '<tr>'+
                            '<th>User_Id</th>'+
                            '<th>Name</th>'+
                            '<th>Username</th>'+
                            '<th>Options</th>'
                              ;               
                for(i=0; i < result['Users'].length; i++){
                   var  user_id = result['Users'][i]["user_id"]
                //    alert(user_id)
                    users +=  '<tr><td><span id ="att_id">'+result['Users'][i]["user_id"]+'</span></td><td>'+result['Users'][i]["name"]+'<td>'+result['Users'][i]["username"]+'</td><td>'+'<button onclick = "myRightsFunction(), GiveRights('+user_id+')">Give Admin Rights</button>'+'</td></tr>';
                }
                document.getElementById("users_table").innerHTML = users+"</table>";
         
    })
    