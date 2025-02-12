# Job Application Cover Letter Generator

## Overview
This project automates the process of generating customised cover letters for job applications. The system takes a job description (JD) either from a CSV file or user input and generates a tailored cover letter in both PDF and Word formats. 

By utilising predefined skill-matching logic, the system automatically identifies relevant keywords in the JD and maps them to corresponding skills and experiences. This ensures that each cover letter is concise, relevant, and aligned with the job requirements.

## Features
- **Choose JD Source:** Users can input a JD manually or extract one from a CSV file.
- **Automated Skill Matching:** Keywords from the JD are mapped to relevant skills and experiences.
- **Experience Integration:** The system pulls relevant past experiences based on keyword matches.
- **Multi-Format Output:** Generates cover letters in both Word (`.docx`) and PDF (`.pdf`).
- **Fast Job Application Process:** Speeds up the process of applying to multiple job postings with personalized cover letters.

## Project Structure
```
job_application_project/
│── main.ipynb                    # Jupyter Notebook version
│── main.py                        # Terminal version
│── requirements.txt               # Required dependencies
│── README.md                      # Project documentation
│── data/
│   ├── m2.csv                     # Job descriptions (from external source or CSV input)
│── src/                            # Source code directory
│   ├── __init__.py                 # Package initialization
│   ├── cover_letter.py             # Cover letter generation logic
│   ├── experience_data.py          # Predefined experiences dictionary
│   ├── skill_matching.py           # Keyword-based skill matching
│   ├── job_input.py                # Allows users to select JD source (CSV or manual input)
│── outputs/
│   ├── generated_cover_letters/    # Folder for generated cover letters (Word & PDF)
```

## How It Works
1. **Input Selection:** Users choose to input a job description manually or extract one from `m2.csv`.
![Demo: input jobs' info ](assets/jobinput.png)
2. **Keyword Detection:** The system scans the JD for predefined keywords related to skills and experience.
3. **Cover Letter Generation:** A structured cover letter is created based on matched skills and experiences.
![Demo: Text output ](assets/coverletter_example.png)
4. **File Output:** The cover letter is saved as both a `.docx` (Word) and `.pdf` file.

## Setup & Usage
### **1. Install Dependencies**
Make sure you have the required packages installed:
```bash
pip install -r requirements.txt
```

### **2. Run the Script**
#### **Jupyter Notebook Version**
```bash
jupyter notebook main.ipynb
```
#### **Terminal Version**
```bash
python main.py
```

## Future Improvements
- **Automated Web Scraping:** Currently, CSV import is required; web scraping part please refer to my other repository: [Indeed-data-scraping-and-visualization](https://github.com/fafadu/Indeed-data-scraping-and-visualization).)


