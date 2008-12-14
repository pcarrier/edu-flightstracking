//alert("Version beta !");

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

function loaded() {
    appendLog('Interface loaded!');
    switchto(onglets[0]);
}