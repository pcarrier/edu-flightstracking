var onglets = new Array('xml','geoxml','kml','map');

function switchto(onglet) {
    for (var i = 0; i < onglets.length; i++) {
    $(onglets[i] + 'title').removeClassName('active');
    $(onglets[i] + 'content').removeClassName('active');
    }
    $(onglet + 'title').addClassName('active');
    $(onglet + 'content').addClassName('active');
    appendLog('Switched to ' + onglet);
}

function loadMap() {
    if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(46.316, 3.1640), 5);
    }
}

function appendLog(text) {
    var today = new Date();
    var dateString = today.toLocaleString();
    $('log').insert({'top': dateString + ": " + text + '\n'});
}

function reloadFlights() {
    new Ajax.Request('/flights.xml', {
	    method: 'get',
		onSuccess: function(transport) {
		$('flights').update(transport.responseText);
		appendLog('Reloaded textarea.');
	    },
		onFailure: function(transport) {
		appendLog('Reloading textarea failed!');
	    }
    });
}

function loaded() {
    switchto(onglets[0]);
    reloadFlights();
    appendLog('Interface loaded!');
}