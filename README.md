# AI Recruiting Assistant

An AI-powered recruiting assistant that analyzes candidate data, ranks applicants, calculates recruiting metrics, and generates structured hiring reports.

Designed to help recruiters, hiring teams, and small businesses review candidates more efficiently and organize recruiting decisions through automated reporting.

---

## Features

### Candidate Management

- Read candidate data from CSV files
- Track candidate experience
- Track candidate skill scores
- Organize candidate information for review

### Recruiting Analysis

- Count total candidates
- Calculate average experience
- Calculate average skill score
- Identify top candidates

### Candidate Ranking

- Rank candidates by skill score
- Use experience as a secondary ranking factor
- Generate ordered candidate lists
- Support faster hiring decision workflows

### Recruiting Reporting

- Generate centralized recruiting reports
- Summarize hiring metrics
- List ranked candidates
- Save reports automatically in the outputs folder

---

## Technologies Used

- Python
- CSV Processing
- JSON Configuration
- File Handling
- Pathlib
- Modular Programming
- Recruiting Automation
- Business Process Automation

---

## Project Structure

```text
ai-recruiting-assistant/

├── main.py
├── config.json
├── candidates.csv
├── README.md
├── .gitignore
│
├── modules/
│   ├── candidate_analyzer.py
│   ├── candidate_ranker.py
│   └── report_generator.py
│
└── outputs/
    └── recruiting_report.txt