const toggleMenu = document.querySelector('.toggle-menu');
const menuList = document.querySelector('.menu ul');
const toggleCloseMenu = document.querySelector('.close-menu');

toggleMenu.addEventListener('click', () => {
  menuList.classList.toggle('show');
  toggleCloseMenu.classList.toggle('show');
  toggleMenu.classList.add('hidden');
});

toggleCloseMenu.addEventListener('click', () => {
  menuList.classList.remove('show');
  toggleCloseMenu.classList.remove('show');
  toggleMenu.classList.remove('hidden');
});



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

