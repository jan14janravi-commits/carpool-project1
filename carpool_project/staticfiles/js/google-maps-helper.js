/**
 * Google Maps Helper Functions
 * Reusable functions for Google Maps integration in CarPool project
 */

// Initialize a basic map
function initBasicMap(mapElementId, lat, lng, zoom = 13) {
    const mapElement = document.getElementById(mapElementId);
    if (!mapElement) {
        console.error(`Map element with ID "${mapElementId}" not found`);
        return null;
    }

    const map = new google.maps.Map(mapElement, {
        center: { lat: lat, lng: lng },
        zoom: zoom,
        styles: [
            {
                featureType: "poi",
                elementType: "labels",
                stylers: [{ visibility: "off" }]
            }
        ]
    });

    return map;
}

// Add a marker to the map
function addMarker(map, lat, lng, title, iconColor = "#4A90E2") {
    if (!map) {
        console.error("Map instance is required");
        return null;
    }

    return new google.maps.Marker({
        position: { lat: lat, lng: lng },
        map: map,
        title: title,
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10,
            fillColor: iconColor,
            fillOpacity: 1,
            strokeWeight: 2,
            strokeColor: "#FFFFFF"
        }
    });
}

// Show route between two points
function showRoute(mapElementId, origin, destination, travelMode = 'DRIVING') {
    const mapElement = document.getElementById(mapElementId);
    if (!mapElement) {
        console.error(`Map element with ID "${mapElementId}" not found`);
        return;
    }

    const map = new google.maps.Map(mapElement, {
        zoom: 12,
        center: { lat: 40.7589, lng: -73.9851 } // Default center
    });

    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode[travelMode]
    }, (response, status) => {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
            // Center map on route
            const bounds = new google.maps.LatLngBounds();
            response.routes[0].legs.forEach(leg => {
                bounds.extend(leg.start_location);
                bounds.extend(leg.end_location);
            });
            map.fitBounds(bounds);
        } else {
            console.error('Directions request failed: ' + status);
            alert('Unable to display route. Please check the addresses.');
        }
    });
}

// Get current location and center map
function getCurrentLocation(map, callback) {
    if (!navigator.geolocation) {
        alert('Geolocation is not supported by your browser');
        return;
    }

    navigator.geolocation.getCurrentPosition(
        (position) => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            if (map) {
                map.setCenter(pos);
                addMarker(map, pos.lat, pos.lng, "Your Location", "#51CF66");
            }

            if (callback) {
                callback(pos);
            }
        },
        (error) => {
            console.error('Error getting location:', error);
            alert('Unable to get your location. Please enable location services.');
        }
    );
}

// Initialize map from data attributes
function initMapFromDataAttributes() {
    const mapElements = document.querySelectorAll('.map-container[data-lat][data-lng]');
    
    mapElements.forEach((mapElement) => {
        const lat = parseFloat(mapElement.dataset.lat);
        const lng = parseFloat(mapElement.dataset.lng);
        const zoom = mapElement.dataset.zoom ? parseInt(mapElement.dataset.zoom) : 13;
        
        if (!isNaN(lat) && !isNaN(lng)) {
            const map = initBasicMap(mapElement.id || `map-${Date.now()}`, lat, lng, zoom);
            if (map) {
                addMarker(map, lat, lng, mapElement.dataset.title || "Location");
            }
        }
    });
}

// Search for places using Google Places API
function searchPlaces(query, callback) {
    if (!window.placesService) {
        console.error('Places service not initialized. Make sure Places library is loaded.');
        return;
    }

    const request = {
        query: query,
        fields: ['name', 'geometry', 'formatted_address']
    };

    window.placesService.findPlaceFromQuery(request, (results, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK && results) {
            if (callback) {
                callback(results);
            }
        } else {
            console.error('Places search failed:', status);
        }
    });
}

// Initialize Places Autocomplete
function initAutocomplete(inputElementId, callback) {
    const input = document.getElementById(inputElementId);
    if (!input) {
        console.error(`Input element with ID "${inputElementId}" not found`);
        return null;
    }

    const autocomplete = new google.maps.places.Autocomplete(input, {
        types: ['geocode']
    });

    autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace();
        if (callback) {
            callback(place);
        }
    });

    return autocomplete;
}

// Calculate distance between two points
function calculateDistance(lat1, lng1, lat2, lng2) {
    const R = 6371; // Radius of the Earth in km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLng = (lng2 - lng1) * Math.PI / 180;
    const a = 
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLng / 2) * Math.sin(dLng / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c; // Distance in km
    return distance;
}

// Initialize maps when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize maps from data attributes
    if (typeof google !== 'undefined' && google.maps) {
        initMapFromDataAttributes();
        
        // Initialize Places service if needed
        if (google.maps.places) {
            const map = new google.maps.Map(document.createElement('div'));
            window.placesService = new google.maps.places.PlacesService(map);
        }
    }
});

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initBasicMap,
        addMarker,
        showRoute,
        getCurrentLocation,
        initMapFromDataAttributes,
        searchPlaces,
        initAutocomplete,
        calculateDistance
    };
}

