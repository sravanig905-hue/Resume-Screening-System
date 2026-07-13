from flask import Flask, render_template, request
import os
import re
import pdfplumber
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# -----------------------------
# Job Roles
# -----------------------------
JOB_ROLES = {
    "Python Developer": ["python", "flask", "sql", "ml", "tensorflow", "keras"],
    "Java Developer": ["java", "sql", "spring", "hibernate"],
    "Data Scientist": ["python", "ml", "data science", "statistics", "tensorflow", "keras", "nlp"],
    "Full Stack Developer": ["html", "css", "javascript", "python", "flask", "sql"]
}

CERTIFICATIONS = ["aws", "google", "azure", "ibm", "oracle", "coursera", "udemy", "nptel"]

# -----------------------------
# Read Resume
# -----------------------------
def read_resume(path):
    text = ""

    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"

    elif path.endswith(".docx"):
        doc = Document(path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

    return text.lower()

# -----------------------------
# Skills
# -----------------------------
def extract_skills(text, required):
    return [s for s in required if s in text]

def missing_skills(required, matched):
    return [s for s in required if s not in matched]

# -----------------------------
# Name (FIXED)
# -----------------------------
def extract_name(text):

    lines = text.split("\n")

    for line in lines[:10]:
        line = line.strip()
        words = line.split()

        if (
            len(words) >= 2
            and len(words) <= 4
            and "resume" not in line.lower()
            and "email" not in line.lower()
            and "objective" not in line.lower()
            and "profile" not in line.lower()
            and "@" not in line
            and line.replace(" ", "").isalpha()
        ):
            return line.title()

    return "Not Found"

# -----------------------------
# Email
# -----------------------------
def extract_email(text):
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group() if match else "Not Found"

# -----------------------------
# Route
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    result = {}

    if request.method == "POST":

        job_role = request.form["job_role"]
        file = request.files["resume"]

        if file.filename == "":
            return render_template("index.html", result={})

        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        text = read_resume(path)

        required = JOB_ROLES[job_role]

        matched = extract_skills(text, required)
        missing = missing_skills(required, matched)

        score = int((len(matched) / len(required)) * 100)
        status = "Selected" if score >= 70 else "Rejected"

        # FIXED certificates
        certificates = [c for c in CERTIFICATIONS if c.lower() in text]

        if not certificates:
            certificates = ["No Certifications Found"]

        result = {
            "Candidate Name": extract_name(text),
            "Email": extract_email(text),
            "Job Role": job_role,
            "Score": score,
            "Status": status,
            "Matched Skills": matched,
            "Missing Skills": missing,
            "Certificates": certificates
        }

    return render_template("index.html", result=result)

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)