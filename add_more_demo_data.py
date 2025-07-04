"""
Enhanced seed script to add more comprehensive demo data to the database
"""
from app import create_app
from app.models.aboutus import AboutUs
from app.models.species import Species
from app.models.conservation_project import ConservationProject
from app.models.event import Event
from app.models.team_member import TeamMember
from app.models.slide import Slide
from app.models.page import Page
from datetime import datetime, date

app = create_app()

def add_more_species():
    """Add more species to the database"""
    additional_species = [
        {
            'name': 'Mugger Crocodile',
            'scientific_name': 'Crocodylus palustris',
            'category': 'reptile',
            'conservation_status': 'Vulnerable',
            'habitat': 'Freshwater lakes, rivers, and marshes',
            'description': 'Also known as the marsh crocodile, this species is found throughout the Indian subcontinent.',
            'diet': 'Fish, frogs, birds, small mammals, and aquatic invertebrates',
            'size': '2-4 meters',
            'lifespan': '40-60 years',
            'main_image': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1566402685096-bf4b4e4c0053?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Can survive in both fresh and slightly saline water',
                'Build hole nests in sandy banks',
                'Excellent parents that protect their young',
                'Can go without food for several months'
            ],
            'breeding_info': 'Females dig nests in sandy or muddy banks during winter months.',
            'threats': 'Habitat destruction, pollution, and human encroachment',
            'distribution': 'Indian subcontinent, Iran, and Nepal',
            'is_venomous': False,
            'is_featured': True
        },
        {
            'name': 'Indian Cobra',
            'scientific_name': 'Naja naja',
            'category': 'reptile',
            'conservation_status': 'Near Threatened',
            'habitat': 'Dense forests, plains, agricultural lands, and rocky terrain',
            'description': 'One of the most iconic snakes of India, known for its distinctive hood and cultural significance.',
            'diet': 'Rodents, frogs, birds, and other snakes',
            'size': '1.2-1.8 meters',
            'lifespan': '20-25 years',
            'main_image': 'https://images.unsplash.com/photo-1507146426996-ef05306b995a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1509927083803-4bd519298ac4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Can spread its hood when threatened',
                'Highly venomous but generally avoids humans',
                'Revered in Hindu mythology',
                'Excellent swimmer and climber'
            ],
            'breeding_info': 'Females lay 12-30 eggs in termite mounds or hollow trees.',
            'threats': 'Habitat loss, persecution by humans, and illegal trade',
            'distribution': 'Indian subcontinent and Southeast Asia',
            'is_venomous': True,
            'is_featured': True
        },
        {
            'name': 'Russell\'s Viper',
            'scientific_name': 'Daboia russelii',
            'category': 'reptile',
            'conservation_status': 'Least Concern',
            'habitat': 'Grasslands, scrublands, rocky areas, and agricultural fields',
            'description': 'A highly venomous viper species known for its potent bite and aggressive nature when threatened.',
            'diet': 'Rodents, birds, lizards, and frogs',
            'size': '1.0-1.5 meters',
            'lifespan': '15-20 years',
            'main_image': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Responsible for many snakebite cases in India',
                'Has heat-sensing pits for detecting prey',
                'Gives birth to live young',
                'Can remain motionless for hours'
            ],
            'breeding_info': 'Ovoviviparous species that gives birth to 12-40 live young.',
            'threats': 'Human persecution and habitat modification',
            'distribution': 'Indian subcontinent and Southeast Asia',
            'is_venomous': True,
            'is_featured': False
        },
        {
            'name': 'Indian Star Tortoise',
            'scientific_name': 'Geochelone elegans',
            'category': 'reptile',
            'conservation_status': 'Vulnerable',
            'habitat': 'Dry grasslands, scrub forests, and semi-arid regions',
            'description': 'Beautiful tortoise species with distinctive star-shaped patterns on its shell.',
            'diet': 'Grasses, fruits, flowers, and occasionally carrion',
            'size': '15-25 cm shell length',
            'lifespan': '80-100 years',
            'main_image': 'https://images.unsplash.com/photo-1580407196238-dac33f57c410?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Shell patterns are unique to each individual',
                'Can survive without water for extended periods',
                'Hibernates during extreme weather',
                'Popular in illegal pet trade'
            ],
            'breeding_info': 'Females bury 1-10 eggs in sandy soil during monsoon season.',
            'threats': 'Illegal collection for pet trade and habitat loss',
            'distribution': 'Indian subcontinent and Sri Lanka',
            'is_venomous': False,
            'is_featured': True
        },
        {
            'name': 'Common Indian Monitor',
            'scientific_name': 'Varanus bengalensis',
            'category': 'reptile',
            'conservation_status': 'Least Concern',
            'habitat': 'Forests, grasslands, agricultural areas, and urban environments',
            'description': 'Large lizard species known for its intelligence and adaptability to various environments.',
            'diet': 'Insects, small mammals, birds, eggs, fish, and carrion',
            'size': '1.0-1.5 meters',
            'lifespan': '15-20 years',
            'main_image': 'https://images.unsplash.com/photo-1502780402662-acc01917910e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1618824834469-7ad3f1c0a57c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Excellent swimmers and climbers',
                'Has forked tongue like snakes',
                'Can stand on hind legs when threatened',
                'Highly intelligent with good memory'
            ],
            'breeding_info': 'Females lay 10-30 eggs in termite mounds or burrows.',
            'threats': 'Persecution by humans and habitat fragmentation',
            'distribution': 'Indian subcontinent and Southeast Asia',
            'is_venomous': False,
            'is_featured': False
        }
    ]

    for species_data in additional_species:
        existing = Species.query.filter_by(scientific_name=species_data['scientific_name']).first()
        if not existing:
            Species.create(**species_data)
            print(f"Added species: {species_data['name']}")
        else:
            print(f"Species already exists: {species_data['name']}")

def add_more_conservation_projects():
    """Add more conservation projects"""
    additional_projects = [
        {
            'title': 'Sea Turtle Conservation Program',
            'subtitle': 'Protecting Marine Reptiles Along Indian Coasts',
            'category': 'field_work',
            'status': 'ongoing',
            'start_date': date(2018, 3, 1),
            'location': 'Gahirmatha Beach, Odisha',
            'description': 'Comprehensive program to protect sea turtle nesting sites and reduce mortality rates.',
            'objectives': [
                'Monitor nesting beaches',
                'Reduce fishery bycatch',
                'Community awareness programs',
                'Nest protection initiatives'
            ],
            'methodology': 'Beach patrols, satellite tracking, community engagement, and policy advocacy.',
            'results': 'Protected over 10,000 turtle nests and reduced mortality by 40%.',
            'impact': 'Significant recovery in Olive Ridley turtle populations.',
            'main_image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1582719471137-c3967ffaaf8e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'species_involved': ['Olive Ridley Turtle', 'Green Turtle', 'Hawksbill Turtle'],
            'partners': ['Odisha Forest Department', 'WWF India'],
            'funding_sources': ['Ministry of Environment', 'International donors'],
            'budget': '$200,000 annually',
            'lead_researcher': 'Dr. Meera Patel',
            'publications': [
                'Sea Turtle Conservation Success Stories (2023)',
                'Community-Based Marine Conservation (2022)'
            ],
            'is_featured': True
        },
        {
            'title': 'Amphibian Diversity Assessment',
            'subtitle': 'Documenting Frog and Toad Species of Western Ghats',
            'category': 'research',
            'status': 'ongoing',
            'start_date': date(2020, 1, 1),
            'end_date': date(2025, 12, 31),
            'location': 'Western Ghats, India',
            'description': 'Comprehensive survey and documentation of amphibian species in biodiversity hotspot.',
            'objectives': [
                'Species identification and cataloging',
                'Population assessments',
                'Habitat requirement studies',
                'Conservation recommendations'
            ],
            'methodology': 'Field surveys, acoustic monitoring, DNA barcoding, and ecological modeling.',
            'results': 'Documented 45 species including 8 new species discoveries.',
            'impact': 'Enhanced understanding of amphibian diversity and conservation needs.',
            'main_image': 'https://images.unsplash.com/photo-1454391304352-2bf4678b1a7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'species_involved': ['Malabar Tree Frog', 'Purple Frog', 'Dancing Frog'],
            'partners': ['Kerala Forest Department', 'Bombay Natural History Society'],
            'funding_sources': ['DST India', 'Critical Ecosystem Partnership Fund'],
            'budget': '$150,000 annually',
            'lead_researcher': 'Dr. Arun Krishnan',
            'publications': [
                'New Amphibian Species from Western Ghats (2023)',
                'Amphibian Conservation Priorities (2022)'
            ],
            'is_featured': False
        }
    ]

    for project_data in additional_projects:
        existing = ConservationProject.query.filter_by(title=project_data['title']).first()
        if not existing:
            ConservationProject.create(**project_data)
            print(f"Added conservation project: {project_data['title']}")
        else:
            print(f"Project already exists: {project_data['title']}")

def add_more_events():
    """Add more educational events"""
    additional_events = [
        {
            'title': 'Reptile Photography Workshop',
            'subtitle': 'Capturing Wildlife Through Your Lens',
            'category': 'workshop',
            'event_type': 'public',
            'start_datetime': datetime(2025, 8, 15, 9, 0),
            'end_datetime': datetime(2025, 8, 15, 17, 0),
            'location': 'Photography Studio & Field',
            'venue_details': 'Indoor studio and outdoor reptile enclosures',
            'description': 'Learn professional wildlife photography techniques focusing on reptiles and amphibians.',
            'detailed_agenda': 'Camera basics, lighting techniques, field photography, editing workshop',
            'target_audience': 'Photography enthusiasts and nature lovers',
            'max_participants': 20,
            'registration_fee': 1500.0,
            'prerequisites': 'Basic camera knowledge helpful but not required',
            'what_to_bring': ['DSLR or mirrorless camera', 'Extra batteries', 'Memory cards'],
            'main_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'organizers': ['Photography Club', 'Education Department'],
            'guest_speakers': ['Mr. Rajesh Kumar - Wildlife Photographer'],
            'contact_person': 'Ms. Kavitha',
            'contact_email': 'photography@crocodilebank.org',
            'contact_phone': '+91-9876543220',
            'is_featured': True
        },
        {
            'title': 'Venom & Antivenom Awareness Seminar',
            'subtitle': 'Understanding Snake Bites and First Aid',
            'category': 'educational_program',
            'event_type': 'public',
            'start_datetime': datetime(2025, 9, 10, 14, 0),
            'end_datetime': datetime(2025, 9, 10, 17, 0),
            'location': 'Conference Hall',
            'description': 'Educational seminar on snake bite prevention, first aid, and antivenom treatment.',
            'target_audience': 'Healthcare workers, teachers, and general public',
            'max_participants': 100,
            'registration_fee': 0.0,
            'main_image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'organizers': ['Research Department', 'Medical Team'],
            'guest_speakers': ['Dr. Priya Sharma', 'Dr. Emergency Medicine Specialist'],
            'contact_person': 'Dr. Priya Sharma',
            'contact_email': 'venom@crocodilebank.org',
            'contact_phone': '+91-9876543221',
            'is_featured': True
        },
        {
            'title': 'Junior Naturalist Program',
            'subtitle': 'Summer Camp for Young Conservationists',
            'category': 'educational_program',
            'event_type': 'public',
            'start_datetime': datetime(2025, 6, 1, 9, 0),
            'end_datetime': datetime(2025, 6, 15, 16, 0),
            'location': 'Throughout the facility',
            'description': '15-day intensive program for children to learn about wildlife conservation.',
            'target_audience': 'Children aged 10-16',
            'max_participants': 25,
            'registration_fee': 5000.0,
            'what_to_bring': ['Field notebook', 'Water bottle', 'Hat', 'Comfortable shoes'],
            'main_image': 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'organizers': ['Education Department'],
            'contact_person': 'Mr. Venkat Rao',
            'contact_email': 'junior@crocodilebank.org',
            'contact_phone': '+91-9876543222',
            'is_featured': False
        }
    ]

    for event_data in additional_events:
        existing = Event.query.filter_by(title=event_data['title']).first()
        if not existing:
            Event.create(**event_data)
            print(f"Added event: {event_data['title']}")
        else:
            print(f"Event already exists: {event_data['title']}")

def add_more_team_members():
    """Add more team member profiles"""
    additional_members = [
        {
            'name': 'Dr. Meera Patel',
            'position': 'Marine Conservation Specialist',
            'department': 'conservation',
            'specialization': 'Sea Turtle Conservation and Marine Ecology',
            'bio': 'Dr. Patel leads our marine conservation efforts, focusing on sea turtle protection and coastal habitat restoration.',
            'education': [
                'PhD in Marine Biology - National Institute of Oceanography',
                'MSc in Marine Sciences - Cochin University',
                'BSc in Zoology - Mumbai University'
            ],
            'experience_years': 12,
            'research_interests': [
                'Sea turtle ecology and behavior',
                'Marine protected area management',
                'Coastal habitat restoration'
            ],
            'publications': [
                'Sea Turtle Migration Patterns in Indian Ocean (2023)',
                'Coastal Conservation Strategies (2022)'
            ],
            'awards': [
                'Marine Conservation Excellence Award (2021)',
                'Young Marine Biologist Award (2019)'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1582719471137-c3967ffaaf8e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'meera.patel@crocodilebank.org',
            'languages_spoken': ['English', 'Hindi', 'Gujarati'],
            'current_projects': ['Sea Turtle Conservation Program'],
            'join_date': date(2013, 4, 1),
            'is_featured': True
        },
        {
            'name': 'Dr. Arun Krishnan',
            'position': 'Amphibian Research Coordinator',
            'department': 'research',
            'specialization': 'Amphibian Taxonomy and Ecology',
            'bio': 'Dr. Krishnan specializes in amphibian research and has discovered several new species in the Western Ghats.',
            'education': [
                'PhD in Herpetology - University of Delhi',
                'MSc in Zoology - Kerala University'
            ],
            'experience_years': 10,
            'research_interests': [
                'Amphibian taxonomy and systematics',
                'Biodiversity conservation',
                'Species discovery and description'
            ],
            'publications': [
                'New Frog Species from Kerala (2023)',
                'Amphibian Diversity Patterns (2022)'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1454391304352-2bf4678b1a7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'arun.krishnan@crocodilebank.org',
            'languages_spoken': ['English', 'Malayalam', 'Tamil'],
            'current_projects': ['Amphibian Diversity Assessment'],
            'join_date': date(2015, 9, 15),
            'is_featured': False
        },
        {
            'name': 'Ms. Kavitha Nair',
            'position': 'Public Relations Manager',
            'department': 'administration',
            'specialization': 'Communications and Media Relations',
            'bio': 'Kavitha manages our public relations and media outreach, helping to spread awareness about conservation.',
            'education': [
                'MBA in Marketing - Indian Institute of Management',
                'BA in Mass Communication - Manipal University'
            ],
            'experience_years': 8,
            'research_interests': [
                'Conservation communication',
                'Public awareness campaigns',
                'Digital marketing strategies'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1502780402662-acc01917910e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'kavitha.nair@crocodilebank.org',
            'languages_spoken': ['English', 'Malayalam', 'Hindi'],
            'current_projects': ['Digital Outreach Initiative', 'Media Partnership Program'],
            'join_date': date(2017, 2, 1),
            'is_featured': False
        }
    ]

    for member_data in additional_members:
        existing = TeamMember.query.filter_by(email=member_data['email']).first()
        if not existing:
            TeamMember.create(**member_data)
            print(f"Added team member: {member_data['name']}")
        else:
            print(f"Team member already exists: {member_data['name']}")

def add_more_pages():
    """Add more informational pages"""
    additional_pages = [
        {
            'title': 'Conservation Success Stories',
            'slug': 'success-stories',
            'page_type': 'static',
            'content': 'Discover the remarkable conservation achievements of the Madras Crocodile Bank Trust over the decades.',
            'meta_description': 'Read about our successful conservation projects and their impact on wildlife protection',
            'meta_keywords': ['conservation', 'success', 'wildlife', 'protection'],
            'main_image': 'https://images.unsplash.com/photo-1566402685096-bf4b4e4c0053?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'sections': [
                {
                    'title': 'Gharial Recovery',
                    'content': 'From near extinction to thriving populations',
                    'subsections': [
                        {'title': 'The Challenge', 'content': 'In 1976, gharials were on the brink of extinction'},
                        {'title': 'Our Response', 'content': 'Established breeding programs and habitat protection'},
                        {'title': 'The Success', 'content': 'Over 200 gharials successfully bred and released'}
                    ]
                },
                {
                    'title': 'Community Engagement',
                    'content': 'Working with local communities for conservation',
                    'subsections': [
                        {'title': 'Education Programs', 'content': 'Reaching over 10,000 students annually'},
                        {'title': 'Livelihood Support', 'content': 'Alternative income sources for local communities'}
                    ]
                }
            ],
            'is_published': True,
            'author': 'Conservation Team',
            'publish_date': date.today(),
            'order_position': 3
        },
        {
            'title': 'Volunteer Opportunities',
            'slug': 'volunteer',
            'page_type': 'dynamic',
            'content': 'Join our conservation efforts as a volunteer and make a real difference in wildlife protection.',
            'meta_description': 'Volunteer opportunities at Madras Crocodile Bank Trust',
            'meta_keywords': ['volunteer', 'conservation', 'wildlife', 'opportunities'],
            'main_image': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'sections': [
                {
                    'title': 'Research Volunteers',
                    'content': 'Assist our scientists with ongoing research projects',
                    'subsections': [
                        {'title': 'Field Work', 'content': 'Help with data collection and monitoring'},
                        {'title': 'Lab Work', 'content': 'Assist with sample processing and analysis'}
                    ]
                },
                {
                    'title': 'Education Volunteers',
                    'content': 'Help with our educational programs and visitor activities',
                    'subsections': [
                        {'title': 'School Programs', 'content': 'Assist with educational tours and workshops'},
                        {'title': 'Public Events', 'content': 'Help organize and conduct public awareness events'}
                    ]
                }
            ],
            'is_published': True,
            'author': 'HR Department',
            'publish_date': date.today(),
            'order_position': 4
        }
    ]

    for page_data in additional_pages:
        existing = Page.query.filter_by(slug=page_data['slug']).first()
        if not existing:
            Page.create(**page_data)
            print(f"Added page: {page_data['title']}")
        else:
            print(f"Page already exists: {page_data['title']}")

def main():
    """Run all functions to add more demo data"""
    with app.app_context():
        print("Adding more comprehensive demo data to the database...")
        
        add_more_species()
        add_more_conservation_projects()
        add_more_events()
        add_more_team_members()
        add_more_pages()
        
        print("Enhanced demo data addition completed!")

if __name__ == "__main__":
    main()
