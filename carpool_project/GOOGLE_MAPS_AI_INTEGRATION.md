# Google Maps & AI Integration Guide

This guide explains how to use the enhanced CSS styling, Google Maps integration, and AI features in your CarPool project.

## 🎨 Enhanced CSS Features

### Cartoon Car Background
The CSS includes a beautiful cartoon-style car background pattern that automatically applies to all pages. The background uses:
- Gradient overlays
- Animated patterns
- Responsive design

### Visual Enhancements
- Modern gradient buttons with hover effects
- Smooth animations and transitions
- Card hover effects
- Custom scrollbar styling
- Responsive design for all devices

## 🗺️ Google Maps Integration

### Step 1: Get Your Google Maps API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Maps JavaScript API
   - Places API
   - Directions API
   - Geocoding API
4. Create credentials (API Key)
5. Restrict your API key for security (recommended)

### Step 2: Update the API Key

In `carpool/templates/carpool/base.html`, replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual API key:

```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_ACTUAL_API_KEY&libraries=places,geometry"></script>
```

### Step 3: Using Google Maps in Your Templates

#### Basic Map Display

```html
<div class="map-wrapper">
    <div id="my-map" class="map-container" style="height: 500px;"></div>
</div>

<script>
function initMap() {
    const map = new google.maps.Map(document.getElementById('my-map'), {
        center: { lat: 40.7589, lng: -73.9851 },
        zoom: 13
    });
    
    new google.maps.Marker({
        position: { lat: 40.7589, lng: -73.9851 },
        map: map,
        title: "Location"
    });
}
initMap();
</script>
```

#### Embedded Map (iframe)

```html
<div class="map-wrapper">
    <div class="map-container">
        <iframe 
            src="https://www.google.com/maps/embed?pb=YOUR_EMBED_URL"
            width="100%" 
            height="450" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy">
        </iframe>
    </div>
</div>
```

#### Map with Route

```html
<div class="map-wrapper">
    <div id="route-map" class="map-container" style="height: 500px;"></div>
</div>

<script>
function showRoute(origin, destination) {
    const map = new google.maps.Map(document.getElementById('route-map'), {
        zoom: 12,
        center: { lat: 40.7589, lng: -73.9851 }
    });
    
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
    
    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING
    }, (response, status) => {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
        }
    });
}
</script>
```

#### Using in Django Templates

```django
{% extends "carpool/base.html" %}

{% block content %}
<div class="map-wrapper">
    <div id="ride-map" class="map-container" 
         data-lat="{{ ride.latitude }}" 
         data-lng="{{ ride.longitude }}"
         style="height: 500px;">
    </div>
</div>
{% endblock %}
```

The base template automatically initializes maps with `data-lat` and `data-lng` attributes.

## 🤖 AI Integration Styling

### AI Chat Interface

```html
<div class="ai-container">
    <div class="ai-chat">
        <div class="d-flex align-items-center mb-3">
            <div class="ai-icon">
                <i class="fas fa-robot"></i>
            </div>
            <h4 class="mb-0">AI Assistant</h4>
        </div>
        <div class="ai-message">
            <strong>AI:</strong> Your message here
        </div>
    </div>
</div>
```

### AI Recommendations

```html
<div class="ai-recommendation">
    <h5><i class="fas fa-lightbulb"></i> Smart Recommendation</h5>
    <p>Your recommendation text here</p>
    <button class="btn btn-primary">Action Button</button>
</div>
```

### AI Loading Indicator

```html
<div class="ai-container">
    <div class="d-flex align-items-center">
        <div class="ai-loading me-3"></div>
        <span>AI is processing...</span>
    </div>
</div>
```

## 📝 Example: Complete Ride Detail Page with Map and AI

```django
{% extends "carpool/base.html" %}
{% load static %}

{% block content %}
<div class="container mt-5">
    <div class="row">
        <div class="col-md-8">
            <div class="card mb-4">
                <div class="card-body">
                    <h2>{{ ride.title }}</h2>
                    <p><i class="fas fa-map-marker-alt"></i> {{ ride.origin }} → {{ ride.destination }}</p>
                    
                    <!-- Google Map -->
                    <div class="map-wrapper mt-4">
                        <div id="ride-map" class="map-container" style="height: 400px;"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="col-md-4">
            <!-- AI Recommendations -->
            <div class="ai-recommendation mb-4">
                <h5><i class="fas fa-lightbulb"></i> AI Recommendation</h5>
                <p>Based on your preferences, this ride matches 95% of your criteria!</p>
                <ul>
                    <li>Driver rating: 4.9★</li>
                    <li>Route efficiency: Excellent</li>
                    <li>Price: Competitive</li>
                </ul>
                <button class="btn btn-primary w-100">Book Now</button>
            </div>
            
            <!-- AI Chat -->
            <div class="ai-container">
                <div class="ai-chat">
                    <div class="d-flex align-items-center mb-3">
                        <div class="ai-icon">
                            <i class="fas fa-robot"></i>
                        </div>
                        <h5 class="mb-0">Ask AI</h5>
                    </div>
                    <div class="ai-message">
                        <strong>AI:</strong> Need help? Ask me anything about this ride!
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function initRideMap() {
    const map = new google.maps.Map(document.getElementById('ride-map'), {
        center: { lat: {{ ride.latitude }}, lng: {{ ride.longitude }} },
        zoom: 13
    });
    
    // Add origin marker
    new google.maps.Marker({
        position: { lat: {{ origin_lat }}, lng: {{ origin_lng }} },
        map: map,
        title: "Origin",
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10,
            fillColor: "#51CF66",
            fillOpacity: 1
        }
    });
    
    // Add destination marker
    new google.maps.Marker({
        position: { lat: {{ dest_lat }}, lng: {{ dest_lng }} },
        map: map,
        title: "Destination",
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10,
            fillColor: "#FF6B6B",
            fillOpacity: 1
        }
    });
    
    // Draw route
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
    
    directionsService.route({
        origin: "{{ ride.origin }}",
        destination: "{{ ride.destination }}",
        travelMode: google.maps.TravelMode.DRIVING
    }, (response, status) => {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
        }
    });
}

window.addEventListener('load', initRideMap);
</script>
{% endblock %}
```

## 🎯 CSS Classes Reference

### Map Classes
- `.map-container` - Main map container
- `.map-wrapper` - Wrapper with padding and styling
- `.map-controls` - Container for map control buttons
- `.map-control-btn` - Styled map control button

### AI Classes
- `.ai-container` - Main AI feature container with gradient background
- `.ai-chat` - AI chat interface container
- `.ai-message` - Individual AI message bubble
- `.ai-icon` - Animated AI icon
- `.ai-recommendation` - AI recommendation box
- `.ai-loading` - Loading spinner for AI processing

### Utility Classes
- `.text-gradient` - Gradient text effect
- `.shadow-lg` - Large shadow effect
- `.rounded-lg` - Large border radius

## 🔧 Customization

### Changing Colors

Edit the CSS variables in `modern-styles.css`:

```css
:root {
    --primary-color: #4A90E2;      /* Main brand color */
    --secondary-color: #357ABD;    /* Secondary color */
    --accent-color: #FF6B6B;       /* Accent color */
    --ai-gradient-start: #00C9FF;  /* AI gradient start */
    --ai-gradient-end: #92FE9D;    /* AI gradient end */
}
```

### Changing Background Image

Replace the background image URL in the CSS:

```css
body::before {
    background: url('YOUR_CARTOON_CAR_IMAGE_URL') center/cover;
}
```

## 📱 Responsive Design

All components are fully responsive and work on:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🚀 Performance Tips

1. **Lazy Load Maps**: Only load maps when needed
2. **API Key Restrictions**: Restrict your Google Maps API key to your domain
3. **Image Optimization**: Use optimized images for backgrounds
4. **CSS Minification**: Minify CSS for production

## 📚 Additional Resources

- [Google Maps JavaScript API Documentation](https://developers.google.com/maps/documentation/javascript)
- [Google Maps Embed API](https://developers.google.com/maps/documentation/embed)
- [Font Awesome Icons](https://fontawesome.com/icons)

## ⚠️ Important Notes

1. **API Key Security**: Never commit your API key to version control. Use environment variables.
2. **API Quotas**: Be aware of Google Maps API usage limits and pricing.
3. **Browser Compatibility**: Test in multiple browsers for best results.
4. **Mobile Performance**: Test map performance on mobile devices.

## 🐛 Troubleshooting

### Maps not showing?
- Check if API key is correct
- Verify APIs are enabled in Google Cloud Console
- Check browser console for errors

### AI styling not working?
- Ensure `modern-styles.css` is loaded
- Check if CSS classes are correctly applied
- Verify Font Awesome is loaded for icons

### Background not visible?
- Check image URL is accessible
- Verify CSS is loaded correctly
- Check z-index values

