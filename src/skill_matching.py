# This is skill_matching.py
import re
from src.experience_data import experiences
from experience_data import skillset

# skillset = [
#     "Data analytics", "statistics",
#     "Python", "R", "SQL", "Databricks", "Git", "Excel", "VBA", "Power BI", "DAX", "Power Query",
#     "Machine learning", "ETL", "ML / AI", "Pandas", "cloud-computing", "AWS", "Azure",
#     "reporting", "visualisations"
# ]

def extract_match_skillset(jdtext):
    return [skill for skill in skillset if re.search(re.escape(skill), jdtext, re.IGNORECASE)]

def extract_relevant_experiences(jdtext):
    selected_experiences = {section: [] for section in experiences}
    jdtext = jdtext.lower()
    
    for section, exp_list in experiences.items():
        for exp in exp_list:
            matched_keywords = [kw for kw in exp["keywords"] if re.search(re.escape(kw.lower()), jdtext, re.IGNORECASE)]
            
            if matched_keywords:
                print(f"Matched: {matched_keywords}")
                # print(f"✅ Matched: {matched_keywords} \n {exp['sentence']}")
                selected_experiences[section].append(exp["sentence"])

    return selected_experiences
