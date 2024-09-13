function fetchOptions(endpoint,dropdowId){
    fetch(endpoint)
    .then(response => response.json())
    .then(data => {
        const dropdown = document.getElementById(dropdowId);
        dropdown.innerHTML = '<option value="" disbled selected> Selected an option</option>';
        data.forEach(option =>{
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent=option;
            dropdown.appendChild(optionElement);
        });
    });
}

// fetching ooptions for each dropdown on page load
window.onload = function(){
    fetchOptions('/squareMeters','squareMeters');
    fetchOptions('/numberOfRooms','numberOfRooms');
    fetchOptions('/hasYard','hasYard');
    fetchOptions('/hasPool','hasPool');
    fetchOptions('/floors','floors');
    fetchOptions('/cityPartRange','cityPartRange');
    fetchOptions('/made','made');
    fetchOptions('/isNewBuilt','isNewBuilt');
    fetchOptions('/hasStormProtector','hasStormProtector');
    fetchOptions('/basement','basement');
    fetchOptions('/attic','attic');
    fetchOptions('garage','garage');
    fetchOptions('/hasGuestRoom','hasGuestRoom');
}

//function to ssend data and receive prediced price
function sendData(){
    const form = document.getElementById('predictionForm');
    const formData = new FormData(form);

    fetch('/predict',{
        method:  'POST',
        body: formData

    })

    .then(response => response.text())
    .then(price => {
        document.getElementById("predictedPrice").innerHTML="Price : INR" + price;
    });
}

