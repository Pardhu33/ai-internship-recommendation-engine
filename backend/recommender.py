import requests

APP_ID = "1b92fe85"
API_KEY = "e2054f9b673a17580a03f508a7891523"


def fetch_online_internships(skill):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": API_KEY,
        "results_per_page": 10,
        "what": f"{skill} intern"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print("API Error:", response.status_code)
            return []

        data = response.json()

    except Exception as e:
        print("Error:", e)
        return []

    internships = []

    for job in data.get("results", []):
        internships.append({
            "title": job.get("title", ""),
            "company": job.get("company", {}).get("display_name", ""),
            "location": job.get("location", {}).get("display_name", ""),
            "description": job.get("description", ""),
            "link": job.get("redirect_url", "")
        })

    return internships


def recommend_internships(user_skills):
    all_jobs = []

    for skill in user_skills:
        jobs = fetch_online_internships(skill)
        all_jobs.extend(jobs)

    results = []

    for job in all_jobs:

        job_text = (
            job["title"] + " " +
            job["description"]
        ).lower()

        match_count = 0

        for skill in user_skills:
            if skill.lower() in job_text:
                match_count += 1

        score = (
            (match_count / len(user_skills)) * 100
            if user_skills else 0
        )

        job["match"] = round(score, 2)

        results.append(job)

    # Remove duplicate jobs
    unique_jobs = {}

    for job in results:
        unique_jobs[job["title"]] = job

    return sorted(
        unique_jobs.values(),
        key=lambda x: x["match"],
        reverse=True
    )