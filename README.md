# 🛡️ Bug Bounty Submission Platform

This is a simple web-based bug bounty submission system created as part of an internship project. It allows ethical hackers to report vulnerabilities in a structured format.

## 📂 Project Structure

- `index.html` – Frontend form for bug submission  
- `submit.php` – Backend script that saves bug reports to a `.csv` file  
- `bugs.csv` – Stores submitted bug reports (created after the first submission)

## 🚀 How to Run Locally

1. Install **XAMPP** or **WAMP** to run a local PHP server.
2. Copy this folder into your `htdocs` directory.
3. Start Apache from the control panel.
4. Visit `http://localhost/bug-bounty-project/index.html` in your browser.
5. Submit a bug – it's saved in `bugs.csv`.

## 📌 Features

- Submit bug reports with severity levels
- Stores reports with timestamp
- Minimal, lightweight UI

## 📬 Future Improvements

- Admin panel to view bugs
- Email alerts for new submissions
- Auto-categorization of bug severity

---

Created by [Your Name] – Internship Project
