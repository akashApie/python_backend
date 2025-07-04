# API Documentation - Madras Crocodile Bank Trust

## Overview
This API provides comprehensive access to all sections of the Madras Crocodile Bank Trust website with detailed subsections and rich content including images.

## Base URL
```
http://127.0.0.1:5000/api/v1
```

## Available Endpoints

### 1. About Us Section
**Endpoint:** `/about`
**Methods:** GET, POST
**Description:** Manage About Us content with multiple subsections

**Features:**
- Mission, History, and Vision subsections
- Timeline data for historical information
- Key statistics and achievements
- Inspirational quotes
- Detailed subsections with images
- Featured content highlighting

**Example GET Response:**
```json
{
  "id": 1,
  "title": "Our Mission",
  "subtitle": "Protecting and Preserving Reptilian Heritage",
  "section_type": "mission",
  "text": "The Madras Crocodile Bank Trust is dedicated to...",
  "image": "https://images.unsplash.com/photo-1562690868...",
  "subsections": [
    {
      "title": "Conservation",
      "content": "Protecting endangered species through breeding programs...",
      "image": "https://images.unsplash.com/photo-1551601651..."
    }
  ],
  "key_points": [
    "First crocodile conservation facility in India",
    "Over 2,500 crocodiles bred and released"
  ],
  "statistics": {
    "years_operating": 47,
    "species_conserved": 100,
    "animals_bred": 2500,
    "visitors_annually": 150000
  }
}
```

### 2. Species Collection
**Endpoint:** `/species`
**Methods:** GET, POST
**Individual:** `/species/<id>`
**Methods:** GET, PUT, DELETE

**Features:**
- Comprehensive species information
- Conservation status tracking
- Habitat and distribution details
- Diet and behavior information
- Gallery images for each species
- Interesting facts and breeding information
- Venomous species identification

**Query Parameters:**
- `category`: Filter by reptile/amphibian
- `featured`: Get only featured species

**Example Species:**
- Saltwater Crocodile (Crocodylus porosus)
- Indian Rock Python (Python molurus)
- King Cobra (Ophiophagus hannah)

### 3. Conservation Projects
**Endpoint:** `/conservation`
**Methods:** GET, POST
**Individual:** `/conservation/<id>`
**Methods:** GET, PUT, DELETE

**Features:**
- Detailed project descriptions
- Research objectives and methodology
- Results and impact assessments
- Species involved in each project
- Partner organizations
- Publication tracking
- Image galleries

**Query Parameters:**
- `category`: research, breeding, field_work, education
- `status`: ongoing, completed, upcoming
- `featured`: Get only featured projects

**Example Projects:**
- Gharial Conservation Program
- Venom Research Initiative

### 4. Events & Programs
**Endpoint:** `/events`
**Methods:** GET, POST
**Individual:** `/events/<id>`
**Methods:** GET, PUT, DELETE

**Features:**
- Educational workshops and tours
- Special conservation events
- Registration management
- Contact information
- Detailed agendas
- Target audience specification
- Guest speaker information

**Query Parameters:**
- `category`: workshop, guided_tour, special_event, educational_program
- `event_type`: public, private, school_group, research
- `featured`: Get only featured events
- `upcoming`: Get future events only

**Example Events:**
- World Wildlife Day Celebration
- Snake Identification Workshop
- School Field Trip Program

### 5. Team Members
**Endpoint:** `/team`
**Methods:** GET, POST
**Individual:** `/team/<id>`
**Methods:** GET, PUT, DELETE

**Features:**
- Detailed professional profiles
- Research interests and specializations
- Publication lists
- Awards and recognitions
- Contact information
- Current project involvement
- Educational background

**Query Parameters:**
- `department`: research, conservation, education, administration
- `featured`: Get only featured team members
- `public_only`: Filter public profiles only

**Example Team Members:**
- Dr. Rajesh Kumar (Director of Conservation)
- Dr. Priya Sharma (Head of Venom Research)
- Mr. Venkat Rao (Senior Education Officer)

### 6. Homepage Slides
**Endpoint:** `/slides`
**Methods:** GET, POST
**Individual:** `/slides/<id>`
**Methods:** GET, PUT, DELETE

**Features:**
- Hero carousel content
- Call-to-action buttons
- Image overlays and animations
- Scheduled display periods
- Multiple categories

**Query Parameters:**
- `category`: hero, featured, announcement
- `active_only`: Get only active slides

### 7. Additional Pages
**Endpoint:** `/pages`
**Methods:** GET, POST
**Individual:** `/pages/<id>` or `/pages/slug/<slug>`
**Methods:** GET, PUT, DELETE

**Features:**
- Static and dynamic page content
- SEO metadata
- Hierarchical page structure
- View count tracking
- Rich content sections

**Query Parameters:**
- `page_type`: static, dynamic, landing
- `published_only`: Get only published pages
- `featured`: Get only featured pages

## Data Features

### Rich Content Structure
- All sections include detailed subsections
- Multiple image galleries with high-quality stock photos
- Comprehensive metadata and SEO optimization
- Hierarchical content organization

### Image Integration
- Main images for all content types
- Additional gallery images
- Unsplash integration for high-quality stock photos
- Responsive image URLs

### Advanced Filtering
- Category-based filtering
- Status-based queries
- Featured content highlighting
- Date-based filtering for events

### Content Management
- Full CRUD operations on all endpoints
- Soft delete capabilities
- Version tracking with timestamps
- Author attribution

## Sample Data Included

The database is pre-populated with realistic dummy data including:

- **3 About Us sections** with detailed subsections
- **3 Species profiles** with comprehensive information
- **2 Conservation projects** with research details
- **3 Upcoming events** with registration information
- **3 Team member profiles** with professional details
- **4 Homepage slides** for the carousel
- **2 Additional pages** with rich content

All content includes high-quality images from Unsplash and realistic, engaging descriptions that showcase the conservation work of the Madras Crocodile Bank Trust.

## Error Handling

The API includes comprehensive error handling:
- 404 for not found resources
- 400 for bad requests
- 500 for server errors
- Detailed error messages in JSON format

## Testing the API

You can test the API using:
1. Web browser for GET requests
2. Postman or similar tools for full CRUD testing
3. curl commands for command-line testing

Example curl command:
```bash
curl -X GET "http://127.0.0.1:5000/api/v1/species?featured=true"
```
