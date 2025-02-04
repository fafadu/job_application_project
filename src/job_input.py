#This is job_input.py
import pandas as pd
def get_job_description():
    """
    Choose Job Description Source：
    1. CSV (`m2.csv`)
    2. Manual
    """
    choice = input("Choose Job Description Source：(1: CSV, 2: Manual)： ")

    if choice == "1":
        # CSV 
        df = pd.read_csv("data/m2.csv")
        print(df[["Job Title", "Company"]].head(10))
        index = int(input("Please enter the job index (0 - N)： "))
        try:
            jdtext = df["Job Description"].iloc[index]
            role = df["Job Title"].iloc[index]
            company = df["Company"].iloc[index]
        except IndexError:
            print("Failed")
            return None, None, None

    elif choice == "2":
        role = input("Role: ")
        company = input("Company: ")
        jdtext = input("Job Description: ")

    else:
        print(" Invalid selection, please enter 1 or 2")
        return None, None, None

    return jdtext, role, company



# jdtext = "We are looking for a Data Analyst with experience in Python, SQL, and Power BI."
# role = "Data Analyst"
# company = "TechCorp"