//function to fetch product
function getProduct(event){ 
    var cart = document.getElementById('cart_value').value
    alert(cart)
    event.preventDefault();
    fetch('http://127.0.0.1:5000/api/v2/product/'+cart, {
    method: 'GET',
    headers: {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    "Authorization": localStorage.getItem("access-token")
    },
    cache: 'no-cache'

    })
    .then((res) => {
        console.log(res)
        return res.json()
    }
    )
    .then(result => {
        var i = 0;
        var products = '<table border="1" >'+
                    '<tr>'+
                    '<th>Product_Id</th>'+
                    '<th>Name</th>'+
                    '<th>Quantity</th>'+
                    '<th>Price</th>'+
                    '<th>Action</th>'+
                    ' </tr>'  ;                     
        products +=  '<tr><td>'+result['Product'][i]["product_id"]+'</td><td>'+result['Product'][i]["name"]+'<td>'+result['Product'][i]["quantity"]+'</td><td>'+result['Product'][i]["price"]+'</td><td>'+'<button id="modalBtn" class="button" onclick = "openModal()" >Make Sale</button>'+'</td></tr>';
        document.getElementById("product_table").innerHTML = products+"</table>";

    })
}    

//Modal for the add Products

// Get the modal
var modal = document.getElementById('simpleModal');

// Get the button that opens the modal
// var modalBtn  = document.getElementById("modalBtn");

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName("closeBtn")[0];

//listen for click
// modalBtn.addEventListener('click', openModal);

//listen for close click
closeBtn.addEventListener('click', closeModal);

//listen for outside click
window.addEventListener('click', clickOutside);

// When the user clicks the button, open the modal
function openModal(){
	modal.style.display = "block";
} 

//function to close modal
function closeModal(){

	modal.style.display = 'none';
}

//function to close modal if outside click

function clickOutside(e){
   if(e.target == modal){
   	modal.style.display = 'none';
   }
	
}
