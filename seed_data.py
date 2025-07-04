"""
Seed script to populate the database with dummy data including images for all sections
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

def seed_about_us():
    """Seed About Us section with subsections"""
    about_sections = [
        {
            'title': 'Our Mission',
            'subtitle': 'Protecting and Preserving Reptilian Heritage',
            'section_type': 'mission',
            'text': 'The Madras Crocodile Bank Trust is dedicated to the conservation of reptiles and amphibians through education, research, and captive breeding programs.',
            'image': 'https://images.unsplash.com/photo-1562690868-60bbe7293e94?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80',
            'additional_images': [
                'https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'information': 'Founded in 1976, we have been at the forefront of herpetological conservation for over four decades.',
            'additional_information': 'Our work spans across research, education, conservation breeding, and field programs.',
            'subsections': [
                {
                    'title': 'Conservation',
                    'content': 'Protecting endangered species through breeding programs and habitat restoration',
                    'image': 'https://images.unsplash.com/photo-1551601651-2a8555f1a136?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Education',
                    'content': 'Raising awareness about reptile conservation through educational programs',
                    'image': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Research',
                    'content': 'Conducting scientific studies to better understand reptile behavior and ecology',
                    'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                }
            ],
            'key_points': [
                'First crocodile conservation facility in India',
                'Over 2,500 crocodiles bred and released',
                '100+ species in our collection',
                'Leading research in venom studies'
            ],
            'statistics': {
                'years_operating': 47,
                'species_conserved': 100,
                'animals_bred': 2500,
                'visitors_annually': 150000
            },
            'order_position': 1,
            'is_featured': True
        },
        {
            'title': 'Our History',
            'subtitle': 'Four Decades of Conservation Excellence',
            'section_type': 'history',
            'text': 'The Madras Crocodile Bank was established in 1976 by Romulus Whitaker and others with the vision of saving India\'s crocodilians from extinction.',
            'image': 'https://images.unsplash.com/photo-1566402685096-bf4b4e4c0053?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'additional_images': [
                'https://images.unsplash.com/photo-1618824834469-7ad3f1c0a57c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1454391304352-2bf4678b1a7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'information': 'What started as a small conservation initiative has grown into a world-renowned research and conservation center.',
            'additional_information': 'Today, we continue to pioneer new approaches to reptile conservation and education.',
            'timeline_data': [
                {'year': '1976', 'event': 'Madras Crocodile Bank Trust established'},
                {'year': '1980', 'event': 'First successful crocodile breeding program'},
                {'year': '1985', 'event': 'Venom research program initiated'},
                {'year': '1995', 'event': 'Educational outreach programs launched'},
                {'year': '2000', 'event': 'International partnerships established'},
                {'year': '2010', 'event': 'Digital conservation initiatives begun'},
                {'year': '2020', 'event': 'Virtual education programs launched'}
            ],
            'subsections': [
                {
                    'title': 'The Early Years (1976-1985)',
                    'content': 'Establishing the foundation for crocodile conservation in India',
                    'image': 'https://images.unsplash.com/photo-1509927083803-4bd519298ac4?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Expansion Era (1985-2000)',
                    'content': 'Growing our programs and establishing international recognition',
                    'image': 'https://images.unsplash.com/photo-1502780402662-acc01917910e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Modern Era (2000-Present)',
                    'content': 'Embracing technology and expanding our conservation impact',
                    'image': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                }
            ],
            'order_position': 2,
            'is_featured': False
        },
        {
            'title': 'Our Vision',
            'subtitle': 'Building a Future Where Reptiles Thrive',
            'section_type': 'vision',
            'text': 'We envision a world where reptiles and amphibians are valued, protected, and thrive in their natural habitats.',
            'image': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'additional_images': [
                'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1580407196238-dac33f57c410?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'information': 'Our vision drives everything we do, from our daily care routines to our long-term conservation strategies.',
            'additional_information': 'We believe that education and research are the keys to achieving lasting conservation success.',
            'subsections': [
                {
                    'title': 'Global Impact',
                    'content': 'Expanding our conservation efforts worldwide through partnerships',
                    'image': 'https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Future Technology',
                    'content': 'Leveraging cutting-edge technology for conservation research',
                    'image': 'https://images.unsplash.com/photo-1507146426996-ef05306b995a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                },
                {
                    'title': 'Next Generation',
                    'content': 'Inspiring young conservationists to carry on our mission',
                    'image': 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
                }
            ],
            'quotes': [
                {
                    'text': 'Conservation is not just about saving animals; it\'s about preserving the intricate web of life.',
                    'author': 'Romulus Whitaker'
                },
                {
                    'text': 'Every species saved is a victory for biodiversity.',
                    'author': 'Dr. Jane Smith, Research Director'
                }
            ],
            'order_position': 3,
            'is_featured': False
        }
    ]

    for section_data in about_sections:
        existing = AboutUs.query.filter_by(title=section_data['title']).first()
        if not existing:
            AboutUs.create(**section_data)
            print(f"Created About Us section: {section_data['title']}")

def seed_species():
    """Seed Species data with detailed information and images"""
    species_data = [
        {
            'name': 'Saltwater Crocodile',
            'scientific_name': 'Crocodylus porosus',
            'category': 'reptile',
            'conservation_status': 'Least Concern',
            'habitat': 'Mangroves, estuaries, and coastal areas',
            'description': 'The saltwater crocodile is the largest living reptile and crocodilian known to science.',
            'diet': 'Fish, birds, mammals, and other reptiles',
            'size': 'Males: 4.3-5.2m, Females: 2.5-3.0m',
            'lifespan': '70-100 years',
            'main_image': 'https://images.unsplash.com/photo-1562690868-60bbe7293e94?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1551601651-2a8555f1a136?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Can hold their breath underwater for up to 1 hour',
                'Have the strongest bite force of any animal',
                'Can live for over 100 years',
                'Excellent mothers that carry babies to water'
            ],
            'breeding_info': 'Breeding season is during the wet season. Females build nest mounds and lay 40-60 eggs.',
            'threats': 'Habitat loss, illegal hunting, and human-wildlife conflict',
            'distribution': 'Southeast Asia, Northern Australia, and Eastern India',
            'is_venomous': False,
            'is_featured': True
        },
        {
            'name': 'Indian Rock Python',
            'scientific_name': 'Python molurus',
            'category': 'reptile',
            'conservation_status': 'Near Threatened',
            'habitat': 'Grasslands, scrublands, and rocky outcrops',
            'description': 'A large non-venomous python species native to the Indian subcontinent.',
            'diet': 'Birds, mammals, and other reptiles',
            'size': '3-4.5 meters',
            'lifespan': '20-30 years',
            'main_image': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1580407196238-dac33f57c410?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Can unhinge their jaws to swallow large prey',
                'Excellent swimmers and climbers',
                'Shed their skin several times a year',
                'Can sense heat with special organs'
            ],
            'breeding_info': 'Females lay 20-50 eggs and incubate them by coiling around the clutch.',
            'threats': 'Habitat destruction and illegal trade for skin',
            'distribution': 'Indian subcontinent and Southeast Asia',
            'is_venomous': False,
            'is_featured': True
        },
        {
            'name': 'King Cobra',
            'scientific_name': 'Ophiophagus hannah',
            'category': 'reptile',
            'conservation_status': 'Vulnerable',
            'habitat': 'Dense forests and bamboo thickets',
            'description': 'The world\'s longest venomous snake and the only snake that builds nests.',
            'diet': 'Primarily other snakes, including venomous species',
            'size': '3-4 meters (up to 5.7m)',
            'lifespan': '20-25 years',
            'main_image': 'https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1507146426996-ef05306b995a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1509927083803-4bd519298ac4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'interesting_facts': [
                'Can raise up to one-third of its body off the ground',
                'Has enough venom to kill an elephant',
                'Only snake that builds a nest for its eggs',
                'Can live up to 3 months without food'
            ],
            'breeding_info': 'Builds elaborate nests from vegetation. Females guard the nest until eggs hatch.',
            'threats': 'Deforestation and human encroachment',
            'distribution': 'Southeast Asia and parts of India',
            'is_venomous': True,
            'is_featured': True
        }
    ]

    for species in species_data:
        existing = Species.query.filter_by(scientific_name=species['scientific_name']).first()
        if not existing:
            Species.create(**species)
            print(f"Created species: {species['name']}")

def seed_conservation_projects():
    """Seed Conservation Projects with detailed information"""
    projects_data = [
        {
            'title': 'Gharial Conservation Program',
            'subtitle': 'Saving India\'s Most Endangered Crocodilian',
            'category': 'breeding',
            'status': 'ongoing',
            'start_date': date(2010, 1, 1),
            'location': 'Chambal River, India',
            'description': 'A comprehensive program to breed and release gharials back into their natural habitat.',
            'objectives': [
                'Breed gharials in captivity',
                'Release young gharials into the wild',
                'Monitor wild populations',
                'Educate local communities'
            ],
            'methodology': 'Captive breeding combined with habitat restoration and community engagement.',
            'results': 'Over 200 gharials successfully bred and released since program inception.',
            'impact': 'Significant increase in wild gharial population in the Chambal River.',
            'main_image': 'https://images.unsplash.com/photo-1566402685096-bf4b4e4c0053?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1618824834469-7ad3f1c0a57c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1454391304352-2bf4678b1a7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'species_involved': ['Gharial', 'Marsh Crocodile'],
            'partners': ['Wildlife Institute of India', 'Uttar Pradesh Forest Department'],
            'funding_sources': ['Government of India', 'International donors'],
            'budget': '$500,000 annually',
            'lead_researcher': 'Dr. Rajesh Kumar',
            'publications': [
                'Gharial Recovery in the Chambal: A Success Story (2023)',
                'Community-Based Conservation Approaches (2022)'
            ],
            'is_featured': True
        },
        {
            'title': 'Venom Research Initiative',
            'subtitle': 'Understanding Snake Venoms for Medical Breakthroughs',
            'category': 'research',
            'status': 'ongoing',
            'start_date': date(2015, 6, 1),
            'location': 'Madras Crocodile Bank Laboratory',
            'description': 'Cutting-edge research into snake venoms for developing life-saving antivenoms and medicines.',
            'objectives': [
                'Analyze venom compositions',
                'Develop improved antivenoms',
                'Study venom evolution',
                'Train researchers'
            ],
            'methodology': 'Advanced biochemical analysis combined with computational modeling.',
            'results': 'Identified 15 new venom compounds with potential medical applications.',
            'impact': 'Contributed to development of more effective antivenoms saving hundreds of lives.',
            'main_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1582719471137-c3967ffaaf8e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'species_involved': ['King Cobra', 'Russell\'s Viper', 'Common Krait'],
            'partners': ['Indian Institute of Science', 'CSIR'],
            'funding_sources': ['DBT India', 'Wellcome Trust'],
            'budget': '$300,000 annually',
            'lead_researcher': 'Dr. Priya Sharma',
            'publications': [
                'Novel Venom Compounds and Their Therapeutic Potential (2023)',
                'Evolution of Snake Venom Toxins (2022)'
            ],
            'is_featured': True
        }
    ]

    for project in projects_data:
        existing = ConservationProject.query.filter_by(title=project['title']).first()
        if not existing:
            ConservationProject.create(**project)
            print(f"Created conservation project: {project['title']}")

def seed_events():
    """Seed Events with upcoming and past events"""
    events_data = [
        {
            'title': 'World Wildlife Day Celebration',
            'subtitle': 'Celebrating Biodiversity and Conservation',
            'category': 'special_event',
            'event_type': 'public',
            'start_datetime': datetime(2025, 3, 3, 9, 0),
            'end_datetime': datetime(2025, 3, 3, 17, 0),
            'location': 'Madras Crocodile Bank',
            'venue_details': 'Main auditorium and outdoor exhibition areas',
            'description': 'Join us for a day-long celebration of wildlife conservation with special exhibits, talks, and activities.',
            'detailed_agenda': 'Morning: Expert talks, Afternoon: Guided tours, Evening: Cultural programs',
            'target_audience': 'All ages',
            'max_participants': 500,
            'registration_fee': 0.0,
            'what_to_bring': ['Water bottle', 'Sun hat', 'Comfortable shoes'],
            'main_image': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'gallery_images': [
                'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1502780402662-acc01917910e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            ],
            'organizers': ['Conservation Team', 'Education Department'],
            'guest_speakers': ['Dr. Jane Doe - Wildlife Biologist', 'Prof. John Smith - Herpetologist'],
            'contact_person': 'Sarah Johnson',
            'contact_email': 'events@crocodilebank.org',
            'contact_phone': '+91-9876543210',
            'is_featured': True
        },
        {
            'title': 'Snake Identification Workshop',
            'subtitle': 'Learn to Identify Common Indian Snakes',
            'category': 'workshop',
            'event_type': 'educational_program',
            'start_datetime': datetime(2025, 4, 15, 10, 0),
            'end_datetime': datetime(2025, 4, 15, 16, 0),
            'location': 'Education Center',
            'venue_details': 'Classroom and live demonstration area',
            'description': 'A comprehensive workshop on identifying venomous and non-venomous snakes found in India.',
            'detailed_agenda': 'Theory session, Practical identification, Safety protocols, Q&A session',
            'target_audience': 'Adults and teenagers (16+)',
            'max_participants': 30,
            'registration_fee': 500.0,
            'prerequisites': 'Basic interest in wildlife',
            'what_to_bring': ['Notebook', 'Pen', 'Camera (optional)'],
            'main_image': 'https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'organizers': ['Dr. Venkat Rao', 'Education Team'],
            'contact_person': 'Dr. Venkat Rao',
            'contact_email': 'education@crocodilebank.org',
            'contact_phone': '+91-9876543211',
            'is_featured': True
        },
        {
            'title': 'School Field Trip Program',
            'subtitle': 'Educational Tours for Students',
            'category': 'educational_program',
            'event_type': 'school_group',
            'start_datetime': datetime(2025, 5, 1, 9, 0),
            'end_datetime': datetime(2025, 5, 31, 15, 0),
            'location': 'Throughout the facility',
            'description': 'Specially designed educational tours for school students to learn about reptile conservation.',
            'target_audience': 'School students (grades 5-12)',
            'max_participants': 50,
            'registration_fee': 200.0,
            'main_image': 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'organizers': ['Education Department'],
            'contact_person': 'Ms. Priya Nair',
            'contact_email': 'schools@crocodilebank.org',
            'contact_phone': '+91-9876543212',
            'is_featured': False
        }
    ]

    for event in events_data:
        existing = Event.query.filter_by(title=event['title']).first()
        if not existing:
            Event.create(**event)
            print(f"Created event: {event['title']}")

def seed_team_members():
    """Seed Team Members with detailed profiles"""
    team_data = [
        {
            'name': 'Dr. Rajesh Kumar',
            'position': 'Director of Conservation',
            'department': 'conservation',
            'specialization': 'Crocodilian Conservation and Ecology',
            'bio': 'Dr. Kumar has over 20 years of experience in wildlife conservation, specializing in crocodilian research and habitat restoration.',
            'education': [
                'PhD in Wildlife Biology - Wildlife Institute of India',
                'MSc in Zoology - Delhi University',
                'BSc in Biology - Madras University'
            ],
            'experience_years': 20,
            'research_interests': [
                'Crocodilian behavior and ecology',
                'Habitat restoration techniques',
                'Human-wildlife conflict mitigation'
            ],
            'publications': [
                'Crocodilian Conservation in Modern India (2023)',
                'Habitat Requirements of Gharials (2022)',
                'Community-Based Conservation Strategies (2021)'
            ],
            'awards': [
                'Wildlife Conservation Excellence Award (2020)',
                'Government of India Conservation Medal (2018)'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'rajesh.kumar@crocodilebank.org',
            'phone': '+91-9876543213',
            'languages_spoken': ['English', 'Hindi', 'Tamil'],
            'current_projects': ['Gharial Conservation Program', 'Wetland Restoration Initiative'],
            'join_date': date(2005, 3, 15),
            'is_featured': True
        },
        {
            'name': 'Dr. Priya Sharma',
            'position': 'Head of Venom Research',
            'department': 'research',
            'specialization': 'Snake Venom Biochemistry and Toxicology',
            'bio': 'Dr. Sharma leads our world-renowned venom research program, contributing to antivenom development and medical research.',
            'education': [
                'PhD in Biochemistry - Indian Institute of Science',
                'MSc in Biotechnology - Jawaharlal Nehru University',
                'BSc in Chemistry - St. Stephen\'s College'
            ],
            'experience_years': 15,
            'research_interests': [
                'Venom protein structure and function',
                'Antivenom development',
                'Evolutionary toxinology'
            ],
            'publications': [
                'Novel Venom Compounds and Their Therapeutic Potential (2023)',
                'Evolution of Snake Venom Toxins (2022)',
                'Improved Antivenom Production Methods (2021)'
            ],
            'awards': [
                'Young Scientist Award - Indian Academy of Sciences (2019)',
                'Best Research Paper Award - International Toxinology Society (2020)'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'priya.sharma@crocodilebank.org',
            'orcid_id': '0000-0002-1234-5678',
            'languages_spoken': ['English', 'Hindi'],
            'current_projects': ['Venom Research Initiative', 'Antivenom Improvement Program'],
            'join_date': date(2010, 8, 1),
            'is_featured': True
        },
        {
            'name': 'Mr. Venkat Rao',
            'position': 'Senior Education Officer',
            'department': 'education',
            'specialization': 'Wildlife Education and Outreach',
            'bio': 'Venkat has been instrumental in developing our education programs and has taught thousands of visitors about reptile conservation.',
            'education': [
                'MSc in Environmental Education - Madras University',
                'BSc in Zoology - University of Madras'
            ],
            'experience_years': 18,
            'research_interests': [
                'Environmental education methodologies',
                'Public awareness campaigns',
                'Wildlife interpretation'
            ],
            'profile_image': 'https://images.unsplash.com/photo-1582719471137-c3967ffaaf8e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'email': 'venkat.rao@crocodilebank.org',
            'languages_spoken': ['English', 'Tamil', 'Telugu'],
            'current_projects': ['School Education Program', 'Community Outreach Initiative'],
            'join_date': date(2007, 1, 10),
            'is_featured': False
        }
    ]

    for member in team_data:
        existing = TeamMember.query.filter_by(email=member['email']).first()
        if not existing:
            TeamMember.create(**member)
            print(f"Created team member: {member['name']}")

def seed_slides():
    """Seed Homepage Slides with beautiful images"""
    slides_data = [
        {
            'title': 'Welcome to the Madras Crocodile Bank',
            'subtitle': 'Protecting Reptiles Since 1976',
            'description': 'Discover the fascinating world of reptiles and our conservation efforts.',
            'image_url': 'https://images.unsplash.com/photo-1562690868-60bbe7293e94?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
            'call_to_action_text': 'Explore Our Work',
            'call_to_action_url': '/conservation',
            'order_position': 1,
            'category': 'hero',
            'overlay_color': 'rgba(0,0,0,0.4)',
            'text_color': '#ffffff',
            'animation_type': 'fade',
            'display_duration': 6000
        },
        {
            'title': 'Conservation in Action',
            'subtitle': 'Breeding Programs for Endangered Species',
            'description': 'Learn about our successful breeding programs that have saved species from extinction.',
            'image_url': 'https://images.unsplash.com/photo-1566402685096-bf4b4e4c0053?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
            'call_to_action_text': 'Learn More',
            'call_to_action_url': '/conservation',
            'order_position': 2,
            'category': 'hero',
            'overlay_color': 'rgba(0,0,0,0.3)',
            'text_color': '#ffffff',
            'animation_type': 'slide',
            'display_duration': 6000
        },
        {
            'title': 'Educational Excellence',
            'subtitle': 'Inspiring the Next Generation',
            'description': 'Join our educational programs and workshops to learn about reptile conservation.',
            'image_url': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
            'call_to_action_text': 'View Events',
            'call_to_action_url': '/events',
            'order_position': 3,
            'category': 'hero',
            'overlay_color': 'rgba(0,0,0,0.4)',
            'text_color': '#ffffff',
            'animation_type': 'zoom',
            'display_duration': 6000
        },
        {
            'title': 'Visit Us Today',
            'subtitle': 'Experience Wildlife Conservation',
            'description': 'Plan your visit to see our amazing collection and learn about our work.',
            'image_url': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
            'call_to_action_text': 'Plan Your Visit',
            'call_to_action_url': '/visit',
            'order_position': 4,
            'category': 'hero',
            'overlay_color': 'rgba(0,0,0,0.3)',
            'text_color': '#ffffff',
            'animation_type': 'fade',
            'display_duration': 6000
        }
    ]

    for slide in slides_data:
        existing = Slide.query.filter_by(title=slide['title']).first()
        if not existing:
            Slide.create(**slide)
            print(f"Created slide: {slide['title']}")

def seed_pages():
    """Seed additional pages with content"""
    pages_data = [
        {
            'title': 'Visit Information',
            'slug': 'visit-info',
            'page_type': 'static',
            'content': 'Plan your visit to the Madras Crocodile Bank Trust and make the most of your experience.',
            'meta_description': 'Visitor information for Madras Crocodile Bank including hours, tickets, and facilities',
            'meta_keywords': ['visit', 'hours', 'tickets', 'madras crocodile bank'],
            'main_image': 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'sections': [
                {
                    'title': 'Opening Hours',
                    'content': 'Open daily from 8:30 AM to 5:30 PM',
                    'subsections': [
                        {'title': 'Weekdays', 'content': '8:30 AM - 5:30 PM'},
                        {'title': 'Weekends', 'content': '8:00 AM - 6:00 PM'},
                        {'title': 'Holidays', 'content': 'Special holiday hours apply'}
                    ]
                },
                {
                    'title': 'Ticket Prices',
                    'content': 'Affordable admission for all visitors',
                    'subsections': [
                        {'title': 'Adults', 'content': 'INR 50'},
                        {'title': 'Children (5-12)', 'content': 'INR 25'},
                        {'title': 'Students', 'content': 'INR 30 (with ID)'},
                        {'title': 'Senior Citizens', 'content': 'INR 30'}
                    ]
                },
                {
                    'title': 'Facilities',
                    'content': 'We provide various amenities for visitor comfort',
                    'subsections': [
                        {'title': 'Parking', 'content': 'Free parking available'},
                        {'title': 'Restaurant', 'content': 'On-site dining options'},
                        {'title': 'Gift Shop', 'content': 'Conservation-themed souvenirs'},
                        {'title': 'Accessibility', 'content': 'Wheelchair accessible paths'}
                    ]
                }
            ],
            'is_published': True,
            'is_featured': True,
            'author': 'Admin Team',
            'publish_date': date.today(),
            'order_position': 1
        },
        {
            'title': 'Research Publications',
            'slug': 'research-publications',
            'page_type': 'dynamic',
            'content': 'Explore our latest research findings and scientific publications.',
            'meta_description': 'Research publications from Madras Crocodile Bank Trust scientists',
            'meta_keywords': ['research', 'publications', 'science', 'herpetology'],
            'main_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'sections': [
                {
                    'title': 'Recent Publications',
                    'content': 'Our latest scientific contributions',
                    'subsections': [
                        {
                            'title': '2023 Publications',
                            'content': '15 peer-reviewed papers published in international journals'
                        },
                        {
                            'title': '2022 Publications', 
                            'content': '12 papers covering venom research and conservation'
                        }
                    ]
                }
            ],
            'is_published': True,
            'author': 'Research Team',
            'publish_date': date.today(),
            'order_position': 2
        }
    ]

    for page in pages_data:
        existing = Page.query.filter_by(slug=page['slug']).first()
        if not existing:
            Page.create(**page)
            print(f"Created page: {page['title']}")

def main():
    """Run all seed functions"""
    with app.app_context():
        print("Starting database seeding...")
        
        seed_about_us()
        seed_species()
        seed_conservation_projects()
        seed_events()
        seed_team_members()
        seed_slides()
        seed_pages()
        
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    main()
