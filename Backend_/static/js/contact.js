//VALIDACIÓN FORMULARIO

const form = document.getElementById('formId');

const inputs =  document.querySelectorAll('#formId input');


const expressions = {
	
	name: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	
	mail: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	phone: /^[0-9]{7,14}$/ // 7 a 14 numeros.
}

const fields = {
    name:false,
    mail:false,
    phone:false
}

const validateForm = (e) =>{
    
    switch(e.target.name){
        case 'name':
            campValidate(expressions.name, e.target,'name');
           break
        case 'mail':
            campValidate(expressions.mail, e.target,'mail')
            break
        case 'phone':
            campValidate(expressions.phone, e.target,'phone')
            break
       
    }
}

const campValidate = (expression,input, camp) => {
    if(expression.test(input.value)){
        document.getElementById(`group_${camp}`).classList.remove('form_incorrect');
        document.getElementById(`group_${camp}`).classList.add('form_correct');
        document.querySelector('#group_name .form_input_error').classList.remove('form_input_error_active');
        fields[camp] = true;
    }else{
        document.getElementById(`group_${camp}`).classList.add('form_incorrect');
        document.getElementById(`group_${camp}`).classList.remove('form_correct');
        document.querySelector(`#group_${camp} .form_input_error`).classList.add('form_input_error_active');
        fields[camp] = false;
    }
}

inputs.forEach((input)=>{
    input.addEventListener('keyup',validateForm);
    input.addEventListener('blur',validateForm);
})

form.addEventListener('submit', (e)=>{
   
    if(fields.name && fields.mail && fields.phone){
        form.reset();

        document.getElementById('form_mess_exit').classList.add('form_mess_exit_active');
        setTimeout(()=>{
            document.getElementById('form_mess_exit').classList.remove('form_mess_exit_active'); 
        }, 7000 );

        document.querySelectorAll('.form_correct').forEach((icon)=>{
            icon.classList.remove('form_correct');
        });
    }else{
        document.getElementById('form_mess').classList.add('form_mess_active');
        setTimeout(()=>{
            document.getElementById('form_mess').classList.remove('form_mess_active'); 
        }, 5000 );
    }
})

//API MAPS

let map = L.map('map').setView([19.21619, -99.194467],12)
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

let circle = L.circle([19.21619, -99.194467], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: 500
}).addTo(map);

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Bv. La Felicidad N°362 - " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);