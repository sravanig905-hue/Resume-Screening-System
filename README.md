# Resume Screening System

A premium SaaS-style **Resume Screening System** built using **Flask** for the backend and **React + Tailwind CSS** for the frontend. The application analyzes uploaded resumes, compares them with a selected job role, calculates an ATS-style score, and presents the results through a modern analytics dashboard.

---

## Features

* Upload resumes in **PDF, DOCX, and TXT** formats.
* Automatically extract:

  * Candidate Name
  * Email Address
  * Phone Number
  * Resume Sections
* Analyze resumes based on the selected job role.
* Match technical skills and certifications.
* Detect missing skills required for the selected role.
* Generate an ATS-style resume score.
* Display candidate status:

  * Excellent
  * Good
  * Average
  * Needs Improvement
* Interactive analytics dashboard with:

  * Circular ATS Score
  * Skill Match Progress Bars
  * Matched Skills
  * Missing Skills
  * Analytics Counters
  * Personalized Recommendations
* Loading animations and smooth UI transitions.

---

## Tech Stack

### Backend

* Python
* Flask
* pdfplumber
* python-docx

### Frontend

* React (CDN)
* Tailwind CSS
* Framer Motion
* Lenis (Smooth Scrolling)

---

## Project Structure

```text
Resume-Screening-System/
│
├── app.py                     # Flask Backend
├── templates/
│   └── index.html             # React Application Shell
├── static/
│   ├── css/
│   │   └── app.css            # Styles
│   └── js/
│       └── app.jsx            # React Frontend
├── uploads/                   # Uploaded Resumes
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sravanig905-hue/Resume-Screening-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Resume-Screening-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Your Browser

```text
http://127.0.0.1:5000
```

---

## How It Works

1. Upload a resume (PDF, DOCX, or TXT).
2. Select the target job role.
3. The backend extracts resume information.
4. Skills and certifications are matched with the selected role.
5. An ATS score is calculated.
6. Results are displayed on an interactive analytics dashboard with:

   * ATS Score
   * Matched Skills
   * Missing Skills
   * Recommendations
   * Analytics

---

## Future Improvements

* AI-powered resume summarization
* Job description upload and comparison
* Multiple resume comparison
* Resume improvement suggestions using LLMs
* User authentication and history tracking
* Export analysis reports as PDF

---

## Notes

* Built with a modern SaaS-inspired user interface.
* Uses a Flask backend with a React frontend for a smooth user experience.
* Developed as a final-year academic project demonstrating resume parsing, ATS score calculation, and intelligent skill matching.

---

## License

This project is intended for **educational and learning purposes**.

---

## Author

**Sravani Gedela**

Final Year B.Tech Student (AI & Data Science)

Developed this Resume Screening System to demonstrate resume parsing, ATS score calculation, skill matching, and a modern analytics dashboard using Flask, React, and Tailwind CSS.
