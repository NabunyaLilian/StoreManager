//  method to fetch products 
    
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
        // alert(result['Products'].length)
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
                            '<th>Options</th>'+
                           ' </tr>'  ;               
                for(i=0; i < result['Products'].length; i++){
                    id = result["Products"][i]["product_id"]
                    name = result['Products'][i]["name"]
                    quantity = result['Products'][i]["quantity"]
                    price = result['Products'][i]["price"]
                    min_quantity = result['Products'][i]["min_quantity"]
                    category = result['Products'][i]["category"]

                    products +=  '<tr><td id = "pdt_id">'+id+'</td><td>'+name+'<td>'+quantity+'</td><td>'+price+'</td><td>'+min_quantity+'</td><td>'+category+ '</td><td>'+'<button id="'+id+'" class="button"  onclick='+'openEdit('+id+',"'+name+'",'+quantity+','+price+','+min_quantity+')>Edit</button>&nbsp &nbsp  <button id = "delete-button"  onclick = "mydeleteFunction(), DeleteProduct('+id+')">Delete</button>'+'</td></tr>';
                }
                document.getElementById("products_table").innerHTML = products+"</table>";
         
    })


//function to fetch product
function getProduct(event){ 
    event.preventDefault();
    fetch('http://127.0.0.1:5000/api/v2/product/7', {
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
    alert(JSON.stringify(result))
        var i = 0;
        var products = '<table border="1" >'+
                    '<tr>'+
                    '<th>Product_Id</th>'+
                    '<th>Name</th>'+
                    '<th>Quantity</th>'+
                    '<th>Price</th>'+
                    '<th>Action</th>'
                    +
                    ' </tr>'  ;               
            products +=  '<tr><td>'+result['Products'][i]["product_id"]+'</td><td>'+result['Products'][i]["name"]+'<td>'+result['Products'][i]["quantity"]+'</td><td>'+result['Products'][i]["price"]+'</td><td>'+ '</td><td>'+'<button id="modalBtn" class="button"  onclick="openModal()">Make Sale</button>'+'</td></tr>';
        document.getElementById("product_table").innerHTML = products+"</table>";

    })
}

//  function to add products     
function AddProduct(event){
    event.preventDefault();
    var Name = document.getElementById('name').value;
    var Quantity = document.getElementById('qty').value;
    var Price = document.getElementById('price').value;
    var Min_quantity = document.getElementById('min_qty').value;
    var Category = document.getElementById('category').value;

    const data = {"Name":Name, "Quantity":Quantity, "Price":Price, "Min_quantity":Min_quantity, "Category":Category};
    // alert(JSON.stringify(data))
    fetch('http://127.0.0.1:5000/api/v2/products',
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
    .then((res) => {
        // if(res.status!=201){
        //   alert(res.status) 
        // }
        console.log(res)
        // alert(res.status)
        return res.json()
    })
    .then(result => { 
     
    if(result['Message'] ==  "Product added to stock"){
    alert(result['Message'])
    }
    else{
    alert(result['Error'])
    }
    
    })
    
    }

//  function to edit products 

function EditProduct(event){
        event.preventDefault();
        // var id = document.getElementById('pdt_id').value;
        var product_id = document.getElementById('pdt_id').value
        var Name = document.getElementById('pdt_name').value;
        var Quantity = document.getElementById('quantity').value;
        var Price = document.getElementById('px').value;
        var Min_quantity = document.getElementById('min_quantity').value;
        var Category = document.getElementById('cat').value;
        const data = {"Name":Name, "Quantity":Quantity, "Price":Price, "Min_quantity":Min_quantity, "Category":Category};
        // alert(JSON.stringify(data))
        // alert(id)
        // alert(localStorage.getItem("access-token"))
        fetch('http://127.0.0.1:5000/api/v2/product/'+product_id,
        {
            method:'PUT',
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
            if(result['Message'] ==  "Product updated"){
                alert(result['Message'])
            }
            else{
                alert(result['Error'])
            }
            
        })
        
        }

 
//  function to delete products   

function DeleteProduct(id){
        alert(id)
        fetch('http://127.0.0.1:5000/api/v2/product/'+id,
        {
            method:'DELETE',
            
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            cache:'no-cache'
        })
        .then((res) => res.json())
        .then(result => {
        if(result['Message'] ===  "Product deleted"){
            alert(result['Message'])
        }
        else{
            alert('Something went wrong')
        }
        
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

function openEdit(product_id, name, quantity, price, min_quantity){

        document.getElementById('pdt_id').value = product_id;
        document.getElementById('pdt_name').value = name;
        document.getElementById('quantity').value = quantity;
        document.getElementById('px').value = price;
        document.getElementById('min_quantity').value = min_quantity;


        // alert(product_id)  
        //Modal for edit Products
        var modal2 = document.getElementById('EditModal');
        // Get the button that opens the modal
        var modalBtn  = document.getElementById(product_id);
        // Get the <span> element that closes the modal
        var closeEditBtn = document.getElementsByClassName("closeEditBtn")[0];
         //listen for click
         modalBtn.addEventListener('click', openEditModal);
        //listen for close click
        closeEditBtn.addEventListener('click', closeEditModal);
        //listen for outside click
        window.addEventListener('click', clickOutside);
        // When the user clicks the button, open the modal
        function openEditModal(){

            modal2.style.display = "block";
        } 
        //function to close modal
        function closeEditModal(){

            modal2.style.display = 'none';
        }

        //function to close modal if outside click

        function clickOutside(e){
            if(e.target == modal){
                modal2.style.display = 'none';
            }    
        }
}

//function to confirm delete

function mydeleteFunction() {
      confirm("Are you sure you want to delete this product!");
  }

//function to confirm offer of admin rights

function myRightsFunction() {
      confirm("Are you sure you want to give admin rights");
  }          
    