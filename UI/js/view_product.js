//  method to fetch products 
    
fetch('https://lilianstoremanager-api.herokuapp.com/api/v2/products', {
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
                var edit = 'editBtn'
                var products = '<table border="1" >'+
                            '<tr>'+
                            '<th>Product_Id</th>'+
                            '<th>Name</th>'+
                            '<th>Quantity</th>'+
                            '<th>Price</th>'+
                            '<th>Minimum Quantity</th>'+
                            '<th>Category</th>'+
                           ' </tr>'  ;               
                for(i=0; i < result['Products'].length; i++){
                    products +=  '<tr><td id = "pdt_id">'+result['Products'][i]["product_id"]+'</td><td>'+result['Products'][i]["name"]+'<td>'+result['Products'][i]["quantity"]+'</td><td>'+result['Products'][i]["price"]+'</td><td>'+result['Products'][i]["min_quantity"]+'</td><td>'+result['Products'][i]["category"]+'</td></tr>';
                }
                document.getElementById("product_tab").innerHTML = products+"</table>";
         
    })    

