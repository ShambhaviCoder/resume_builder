class Resume:
    def __init__(self):
        self.data = {
            'personal_info': {
                'name': '',
                'contact_info': [],  # list of contact info dictionaries
                'address': ''
            },
            'experience': [],  # list of experience dictionaries
            'education': [],  # list of education dictionaries
            'skills': [],  # list of skill strings
            'projects': [],  # list of project dictionaries
            'additional_sections': {}  # dictionary to store additional sections
        }

    def add_contact_info(self, contact_info):
        self.data['personal_info']['contact_info'].append(contact_info)

    def add_experience(self, experience):
        self.data['experience'].append(experience)

    def add_education(self, education):
        self.data['education'].append(education)

    def add_skill(self, skill):
        self.data['skills'].append(skill)

    def add_project(self, project):
        self.data['projects'].append(project)

    def add_additional_section(self, section_name, section_data):
        self.data['additional_sections'][section_name] = section_data

    def to_dict(self):
        return self.data
    
    import os
from PIL import Image

class Resume:
    def __init__(self):
        self.data = {
            'personal_info': {
                'name': '',
                'contact_info': [],  # list of contact info dictionaries
                'address': ''
            },
            'experience': [],  # list of experience dictionaries
            'education': [],  # list of education dictionaries
            'skills': [],  # list of skill strings
            'projects': [],  # list of project dictionaries
            'additional_sections': {}  # dictionary to store additional sections
        }
        self.template_options = {
            '1': r'C:\Users\shamb\Downloads\download.jfif',
            '2': r'C:\Users\shamb\Downloads\download (1).jfif',
            '3': r'C:\Users\shamb\Downloads\images (1).jfif',
            '4': r'C:\Users\shamb\Downloads\download (1).png',
            
        }
        self.template_path = 'templates'
        self.font_sizes = {
            'small': 10,
            'medium': 12,
            'large': 14
        }
        self.font_styles = {
            'Arial': 'arial.ttf',
            'Calibri': 'calibri.ttf',
            'Times New Roman': 'times.ttf'
        }
        self.margin_options = {
            'left': 0.5,
            'right': 0.5,
            'top': 0.5,
            'bottom': 0.5
        }

    def add_contact_info(self):
        contact_info = {}
        contact_info['type'] = input("Enter contact info type (e.g., phone, email, LinkedIn): ")
        contact_info['value'] = input("Enter contact info value: ")
        self.data['personal_info']['contact_info'].append(contact_info)

    def add_experience(self):
        experience = {}
        experience['company'] = input("Enter company name: ")
        experience['job_title'] = input("Enter job title: ")
        experience['duration'] = input("Enter duration (e.g., 2018-2020): ")
        experience['achievements'] = input("Enter achievements (separated by commas): ")
        self.data['experience'].append(experience)

    def add_education(self):
        education = {}
        education['degree'] = input("Enter degree (e.g., Bachelor's, Master's): ")
        education['institution'] = input("Enter institution name: ")
        education['duration'] = input("Enter duration (e.g., 2015-2019): ")
        education['gpa'] = input("Enter GPA (optional): ")
        self.data['education'].append(education)

    def add_skill(self):
        skill = input("Enter skill: ")
        self.data['skills'].append(skill)

    def add_project(self):
        project = {}
        project['name'] = input("Enter project name: ")
        project['description'] = input("Enter project description: ")
        project['duration'] = input("Enter project duration (e.g., 2018-2020): ")
        project['achievements'] = input("Enter project achievements (separated by commas): ")
        self.data['projects'].append(project)

    # Add other methods as needed