from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from nlp_parser import extract_skills
from recommender import recommend_internships
import shutil

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    skills = extract_skills(file_path)
    recommendations = recommend_internships(skills)

    return {
        "skills": skills,
        "recommendations": recommendations
    }