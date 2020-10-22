# Matching Text at the Start or End of the string
# Problem: You need to check the start or end of a
# string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

filename = 'spam.txt'
print(filename.endswith('.txt'))

import os

file = os.listdir('.')
print(file)
print(any(name.endswith('.py') for name in file))

# use of any

def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']}")

applicants = [
    {
        "name": "Rishabh",
        "programming_languages": ["python", "java"],
        "year_of_experience": 1,
        "has_degree": True,
        "email_address": "rishabhthakur@gmail.com"
    },
    {
        "name": "Dev",
        "programming_languages": ["c++", "java"],
        "year_of_experience": 1,
        "has_degree": False,
        "email_address": "devd@gmail.com"
    },
    {
        "name": "Tera",
        "programming_languages": ["java"],
        "year_of_experience": 1,
        "has_degree": False,
        "email_address": "Tera@gmail.com"
    }, 
]

for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["year_of_experience"] >= 5

    credentials = (
        knows_python,
        experienced_dev,
        applicant['has_degree'],
    )
    if any(credentials):
        schedule_interview(applicant)