L.mapbox.accessToken = 'pk.eyJ1Ijoid3NhbmtleSIsImEiOiJaZjViQU5FIn0.r9sJQsvsl2Zz2_fp_nfemQ';
L.mapbox.map('map', 'examples.map-i875kd35')
    .addControl(L.mapbox.geocoderControl('mapbox.places'));

