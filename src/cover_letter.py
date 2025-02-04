#This is cover_letter.py
import re
from src.skill_matching import extract_match_skillset, extract_relevant_experiences
from src.experience_data import experiences
from src.config import EMAIL, APPNAME, PHONE, PERSONAL_SITE, GITHUB, VISA_STATUS, LOCATION 


def generate_cover_letter(jdtext, role, company):
    '''
    Generate Cover Letter based on job description (jdtext), job title (role), company name (company)
    '''
    matchskillset = extract_match_skillset(jdtext)
    relevant_experiences = extract_relevant_experiences(jdtext)
    # print( f"""Application for {role} within {company} """)
    cover_letter = f"""
Application for {role} within {company}

Dear Hiring Manager,

I am writing to express my interest in the {role} position within {company}. I am a recent Master of IT graduate in Data Analytics from Griffith University with hands-on experience in {", ".join(matchskillset)} as your organization required.

Below are the practical experiences I had that match your desired expertise.

**As a data analyst intern at Gold Coast Health Integrated Complex Care Team**  
I collaborated with the Allied Services Team to extract insights from healthcare data and evaluate the effectiveness of services.
"""

    for exp in relevant_experiences["Gold Coast Health"]:
        cover_letter += f"- {exp}\n"

    cover_letter += "\n**Data Analyst/Assistant with Griffith University’s STEM Outreach Program**\nI built Tableau reports to highlight 18 years of long-term impact on science education achievements.\n"

    for exp in relevant_experiences["STEM Outreach Program"]:
        cover_letter += f"- {exp}\n"

    cover_letter += "\n**Education and Personal Side Projects (https://github.com/fafadu) **\n"

    for exp in relevant_experiences["Education & Side Projects"] :
        cover_letter += f"- {exp}\n"

    cover_letter += "\n**Volunteer & Leadership**\nBeyond my technical expertise, I actively contribute to volunteering efforts, serving as the secretary of an IT club and an online webinar organiser.\n"

    for exp in relevant_experiences["Volunteer & Leadership"]:
        cover_letter += f"- {exp}\n"

    
    cover_letter += f"""    

    
{VISA_STATUS}
{LOCATION}

I look forward to the possibility of contributing to your organization’s success.

Kind regards,  
{APPNAME}
{EMAIL} | {PHONE} | {PERSONAL_SITE} | {GITHUB}
"""
    
    return cover_letter
