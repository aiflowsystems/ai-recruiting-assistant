def generate_recruiting_report(
    recruiting_summary,
    ranked_candidates
):
    ranking_text = ""

    for index, candidate in enumerate(
        ranked_candidates,
        start=1
    ):
        ranking_text += (
            f"{index}. "
            f"{candidate['name']} | "
            f"Experience: "
            f"{candidate['experience_years']} years | "
            f"Skill Score: "
            f"{candidate['skills_score']}\n"
        )

    report = f"""AI Recruiting Assistant Report

RECRUITING SUMMARY
==================

Total Candidates:
{recruiting_summary['total_candidates']}

Average Experience:
{recruiting_summary['average_experience']} years

Average Skill Score:
{recruiting_summary['average_skill_score']}

Top Candidates:
{recruiting_summary['top_candidates']}

TOP RANKED CANDIDATES
=====================

{ranking_text}
"""

    return report