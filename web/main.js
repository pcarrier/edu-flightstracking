//alert("Version beta !");

function loadMap() {
    if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(46.316, 3.1640), 5);
    }
}