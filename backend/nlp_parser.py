import PyPDF2

def extract_skills(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    text = text.lower()

    skills_db = [
        "python", "java", "c++", "machine learning",
        "data science", "django", "react",
        "communication", "marketing", "sql"
    ]

    found_skills = [skill for skill in skills_db if skill in text]

    return found_skills