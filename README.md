# 📄 CV/Resume Generator Web App

## 🚀 Overview

The **CV/Resume Generator** is a powerful web application designed to help users create professional resumes dynamically. Currently, the backend is fully developed using Django, and the frontend is styled with Bootstrap and CSS for simplicity. In the future, the UI will be revamped with **React** to provide a highly interactive and modern user experience.

## 🎯 Features

- 📝 **User-Friendly Form** – Enter personal details, education, skills, and work experience.
- 💾 **Data Storage** – Submitted details are stored in a backend database.
- 📜 **List Profiles** – View all submitted CV profiles.
- 📥 **Download CVs** – Generate and download CVs in PDF format.
- 📄 **Professional Design** – Structured and clean CV layout.

## 🛠️ Tech Stack

- **Backend:** Django (Python Framework)
- **Frontend:** Bootstrap, CSS (Future Upgrade: React)
- Database: SQLite
- **PDF Generation:** PDFKIT

## 🏗️ Installation Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DS-Vijayapala/Django-CV-Resume-Generator-Web-App.git
   cd cv-resume-generator
   ```
2. **Create a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
6. **Open in Browser:**
   - Visit `http://127.0.0.1:8000/`
   - Download Your CV `http://127.0.0.1:8000/list`

## 🚀 Future Plans

- 🌟 **Upgrade Frontend:** Implement a modern, interactive UI using React.
- 📌 **Enhance User Experience:** Customize the design for a more intuitive workflow.
- 🔧 **Additional Features:** Improve PDF customization and add more styling options.

## 🏆 Contributing

Contributions are welcome! Feel free to fork the repo, make changes, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.


**This is just the beginning! Stay tuned for exciting updates. 🚀🔥**


