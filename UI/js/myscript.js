//Modal for the add Products
// Get the modal
var modal = document.getElementById('simpleModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("modalBtn");

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName("closeBtn")[0];

//listen for click
modalBtn.addEventListener('click', openModal);

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


//Modal for edit Products
var modal2 = document.getElementById('EditModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("editBtn");

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

function mydeleteFunction() {
      confirm("Are you sure you want to delete this product!");
  }



//  method to add products 
function AddProduct(){
    var Name = document.getElementById('name').value;
    var Quantity = document.getElementById('qty').value;
    var Price = document.getElementById('price').value;
    var Min_quantity = document.getElementById('min_qty').value;
    var Category = document.getElementById('category').value;

    const data = {"Name":Name, "Quantity":Quantity, "Price":Price, "Min_quantity":Min_quantity, "Category":Category};
    alert(JSON.stringify(data))
    console.log(localStorage.getItem("access-token"))
    fetch('http://127.0.0.1:5000/api/v2/products',
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
        alert(result);
    if(result['Message'] ==  "Product added to stock"){
    alert(result['Message'])
    }
    else{
    alert(result['Message'])
    }
    
    })
    
    }  