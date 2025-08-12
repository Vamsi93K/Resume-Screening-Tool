# Resume-Screening-Tool
A Django-powered web application that helps recruiters efficiently evaluate resumes against job descriptions using OCR, keyword matching, and scoring logic. Designed to bridge the gap between raw text and recruitment decisions, this tool combines intelligent automation with practical UX features to support both recruiters and job seekers.

## Features
-  OCR Parsing: Extracts text from scanned resumes using Tesseract, with fallback handling for parsing errors
-  Keyword Scoring Engine: Matches resume content against job description keywords to generate a relevance score
-  Dashboard & Leaderboard: Visual interface for reviewing scores, sorting candidates, and managing uploads
-  Resume Cleanup: Supports formatting fixes and parsing validation to improve input quality
-  Fast & Intuitive: Built with usability in mind — responsive interface, clear feedback, and error handling
-  Future Plans (in progress):
- Batch upload support for high-volume screening
- Auto keyword extraction from JD using basic NLP
- Recruiter tips and resume improvement guidance for freshers

## Tech Stack
| Layer | Technologies Used | 
| Backend | Django, Python | 
| OCR Parsing | Tesseract OCR, pdf2image | 
| Keyword Logic | Custom Python scoring functions | 
| Frontend | HTML/CSS (to be upgraded with templates) | 
| Data Storage | SQLite (switchable to PostgreSQL) | 

## How to Run Locally
- Clone the repo:
git clone https://github.com/Vamsi93K/Resume-Screening-Tool.git
cd Resume-Screening-Tool
## Create a virtual environment:
python -m venv env
source env/bin/activate  # Or use `env\Scripts\activate` on Windows
## Install dependencies:
pip install -r requirements.txt
- Make migrations & run server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
- Important: Install Poppler and add it to PATH for OCR support.
## Creator's Note
This tool was built as a learning and problem-solving exercise using AI guidance. Each feature was implemented through iterative development, debugging, and testing to solve a real-world challenge. It reflects a product-oriented mindset and passion for building user-focused
