function AddSales(event){
    event.preventDefault();
    var Name = document.getElementById('name').value;
    var Quantity = document.getElementById('qty').value;
    var date = document.getElementById('date').value;
    const data = {"Name":Name, "Quantity":Quantity, "Date":date};
    // alert(JSON.stringify(data))
    // alert(localStorage.getItem("access-token"))
    fetch('http://127.0.0.1:5000/api/v2/sales',
    {
        method:'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": localStorage.getItem("access-token")
        },
        cache:'no-cache'
    })
    .then((res) => res.json())
    .then(result => {
        if(result['Message'] ==  "Sale record created"){
            alert('Product added to cart')
        }
        else{
            alert('Something went wrong')
        }
        
    })
    
    }



fetch('http://127.0.0.1:5000/api/v2/sales', {
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
                       var sales = '<table>'+
                                   '<tr>'+
                                   '<th>Sale_Id</th>'+
                                   '<th>Name</th>'+
                                   '<th>Quantity</th>'+
                                   '<th>Price</th>'+
                                   '<th>Date</th>'+
                                   '<th>StoreAttendant_Id</th>'+
                                  ' </tr>'  ;               
                       for(i=0; i < result['Sales'].length; i++){
                        sales +=  '<tr><td>'+result['Sales'][i]["sale_id"]+'</td><td>'+result['Sales'][i]["name"]+'<td>'+result['Sales'][i]["quantity"]+'</td><td>'+result['Sales'][i]["price"]+'</td><td>'+result['Sales'][i]["date"]+'</td><td>'+result['Sales'][i]["user_id"]+'</td></tr>';
                       }
                       document.getElementById("sales_table").innerHTML = sales+"</table>";
            
           })
   