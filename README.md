# AI Internship Recommendation Engine

An AI-powered web application that analyzes resumes, extracts skills using NLP techniques, and recommends relevant internships based on the candidate's profile.

## Features

* Upload Resume (PDF)
* Automatic Skill Extraction
* Internship Recommendations
* Match Percentage Calculation
* FastAPI Backend
* React Frontend
* Adzuna Jobs API Integration
* Responsive User Interface

## Tech Stack

### Frontend

* React.js
* Axios
* CSS

### Backend

* FastAPI
* Python
* PyPDF2
* Requests

### APIs

* Adzuna Jobs API

## Project Architecture

AI_Internship/

├── backend/

│ ├── main.py

│ ├── nlp_parser.py

│ ├── recommender.py

│ └── requirements.txt

│

├── frontend/

│ ├── src/

│ ├── public/

│ └── package.json

│

└── README.md

## Workflow

1. User uploads resume PDF.
2. Backend extracts text from the resume.
3. Skills are identified using NLP-based matching.
4. Relevant internships are fetched from Adzuna API.
5. Match percentage is calculated.
6. Recommended internships are displayed in the frontend.

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-internship-recommendation-engine.git
cd ai-internship-recommendation-engine
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

### Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend runs on:

```text
http://localhost:3000
```

## Sample Skills Detected

* Python
* Java
* React
* SQL
* Django
* Machine Learning
* Data Science
* Communication
* Marketing

## Future Enhancements

* Resume Ranking
* AI-Based Skill Extraction using Transformers
* Internship Filtering
* User Authentication
* MongoDB Database Integration
* Resume Score Analysis
* Personalized Career Suggestions

## Learning Outcomes

* Full Stack Development
* FastAPI Development
* React Integration
* REST APIs
* Resume Parsing
* NLP Fundamentals
* API Consumption

## Author

Pardhu Rao

B.Tech – Computer Science & Engineering

## License

This project is developed for educational and learning purposes.
