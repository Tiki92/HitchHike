(function () {

    function loadmap() {
        var djoptions = {"srid": null, "extent": [[-90, -180], [90, 180]], "fitextent": true, "center": [50.9, 25.31], "zoom": 4, "minzoom": 3, "maxzoom": 18, "layers": [["OSM", "//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", "\u00a9 <a href=\"http://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors"]], "overlays": [], "attributionprefix": null, "scale": "both", "minimap": false, "resetview": true, "tilesextent": []},
            options = {djoptions: djoptions, initfunc: loadmap,
                       globals: false, callback: window.map_init_basic}
            //map = L.Map.djangoMap('map', options);
        
    }
    var loadevents = ["load"];
    if (loadevents.length === 0) loadmap();
    else if (window.addEventListener) for (var i=0; i<loadevents.length; i++) window.addEventListener(loadevents[i], loadmap, false);
    else if (window.jQuery) jQuery(window).on(loadevents.join(' '), loadmap);
    
})();

var map = L.map('map', { scrollWheelZoom: false }).setView([52.219019,-1.552358], 7);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}{r}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var control = L.Routing.control({
		waypoints: [],
    routeWhileDragging: false,
		serviceUrl: 'http://localhost:5000/route/v1',
		geocoder: L.Control.Geocoder.nominatim(),
		autoRoute: true,
		routeWhileDragging: false,
		routeDragTimeout: 250,
		showAlternatives: false,
		altLineOptions: {
			styles: [
				{color: 'black', opacity: 0.15, weight: 9},
				{color: 'white', opacity: 0.8, weight: 6},
				{color: 'blue', opacity: 0.5, weight: 2}
			]
		}
	}).addTo(map);

	function createButton(label, container) {
	    var btn = L.DomUtil.create('button', '', container);
	    btn.setAttribute('type', 'button');
	    btn.innerHTML = label;
	    return btn;
	}

	map.on('click', function(e) {
	    var container = L.DomUtil.create('div'),
	        startBtn = createButton('Start from this location', container),
	        destBtn = createButton('Go to this location', container);

	    L.popup()
	        .setContent(container)
	        .setLatLng(e.latlng)
	        .openOn(map);

					L.DomEvent.on(startBtn, 'click', function() {
							control.spliceWaypoints(0, 1, e.latlng);
							map.closePopup();
					});

					L.DomEvent.on(destBtn, 'click', function() {
						control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
						map.closePopup();
				});
	});



L.easyButton('<span id="do1" class="fa fa-floppy-o"></span>', function () {


		//alert('Save routing coordinates ...');
}).addTo(map);

//L.Control.geocoder().addTo(map);

L.Routing.errorControl(control).addTo(map);

//var user = "{{ user }}";
    
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
		beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
						xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
		}
});


$("#do1").click(function(){
    
    var date = document.getElementById("datetime").value;
    var phone = document.getElementById("phoneNumber").value.toString();
	var price = document.getElementById("price").value;
	var description = document.getElementById("description").value.toString();
	var seats = document.getElementById("seats").value.toString();
	
    console.log(date);
    console.log(typeof phone);
	console.log(typeof price);
	console.log(seats);
	console.log("description: " + description);
    
    var len = control.getWaypoints().length;
    console.log(len);
	//JSON.stringify(control.getWaypoints()[0]["latLng"]["lat"]);
	var loc_lat = control.getWaypoints()[0]["latLng"]["lat"];
	var loc_lng = control.getWaypoints()[0]["latLng"]["lng"];
	var point = new GeoPoint(loc_lng, loc_lat);
	var loc =  "SRID=4326;POINT(" + [point.getLonDec() + " " + point.getLatDec()] + ")";
	console.log(loc);


	var dest_lat = control.getWaypoints()[len - 1]["latLng"]["lat"];
	var dest_lng = control.getWaypoints()[len - 1]["latLng"]["lng"];
	var point1 = new GeoPoint(dest_lng, dest_lat);
	var dest = "SRID=4326;POINT(" + [dest_lng + " " + dest_lat] + ")";
	console.log(dest);

	var loc_name = control.getWaypoints()[0]["name"].split(",", 1)[0];
	var dest_name = control.getWaypoints()[len - 1]["name"].split(",", 1)[0];
	console.log(loc_name);
	console.log(dest_name);


	$.ajax({
    url:"/add_ride",
		//datatype: "application/json",
    type: "POST",
    data: {
					 user: user,
					 location: loc,
					 destination: dest,
					 location_name: loc_name,
					 destination_name: dest_name,
                     ride_date: date,
                     phone: phone,
					 price: price,
					 description: description,
					 //seats: seats,
					 csrf_token: csrftoken
				 },

    success:function(json){
			console.log(json);
			//alert("It Worked" + json)
		},
//    complete:function(){
//			alert("fin")
//		},
    error:function (xhr, textStatus, thrownError){
        alert("error doing something: " + thrownError);
    }
});

});