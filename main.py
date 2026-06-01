import csv
import json
from pathlib import Path
from modules.candidate_analyzer import analyze_candidates
from modules.candidate_ranker import rank_candidates
from modules.report_generator import generate_recruiting_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]

Path(output_folder).mkdir(exist_ok=True)

candidates = []

with open("candidates.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        candidates.append(row)

recruiting_summary = analyze_candidates(candidates)
ranked_candidates = rank_candidates(candidates)
recruiting_report = generate_recruiting_report(
    recruiting_summary,
    ranked_candidates
)

print("AI Recruiting Assistant")
print("========================")
print()

print(f"Candidates loaded: {len(candidates)}")

for candidate in candidates:
    print(candidate["name"])

print()
print("RECRUITING SUMMARY")
print("------------------")

print(
    f"Total Candidates: "
    f"{recruiting_summary['total_candidates']}"
)

print(
    f"Average Experience: "
    f"{recruiting_summary['average_experience']} years"
)

print(
    f"Average Skill Score: "
    f"{recruiting_summary['average_skill_score']}"
)

print(
    f"Top Candidates: "
    f"{recruiting_summary['top_candidates']}"
)

print()
print("TOP CANDIDATES")
print("--------------")

for index, candidate in enumerate(ranked_candidates, start=1):
    print(
        f"{index}. {candidate['name']} - "
        f"Experience: {candidate['experience_years']} years - "
        f"Skill Score: {candidate['skills_score']}"
    )

report_file = (
    Path(output_folder)
    / config["recruiting_report_file"]
)

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:
    file.write(recruiting_report)

print()
print(
    f"Recruiting report generated: "
    f"{report_file}"
)
