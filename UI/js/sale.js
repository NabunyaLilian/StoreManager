//method for getting sales
function getSale(event){
    var search = document.getElementById('my_cart')
    alert(search)
    event.preventDefault();
    fetch('http://127.0.0.1:5000/api/v2/sale/1', {
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
                               ' </tr>'  ;   
                for(i=0; i < result['Sale'].length; i++){                       
                    sales +=  '<tr><td>'+result['Sale'][i]["sale_id"]+'</td><td>'+result['Sale'][i]["name"]+'<td>'+result['Sale'][i]["quantity"]+'</td><td>'+result['Sale'][i]["price"]+'</td><td>'+result['Sale'][i]["date"]+'</td></tr>';
                }
                document.getElementById("sales_table").innerHTML = sales+"</table>";
         
        })

}    

