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
    .then(result => {
        alert('heryyy');
    if(result['User']['username'] ==  Username){
    alert(result['Message'])
    }
    else{
    alert(result['Message'])
    }
    
    })
    
    }