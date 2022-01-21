// [START maps_map_simple]
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}
// [END maps_map_simple]
//AIzaSyDeap_e-I8mfKUQlIW2PmBnnlzHfptLlGI