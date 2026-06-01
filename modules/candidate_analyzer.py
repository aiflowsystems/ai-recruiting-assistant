def analyze_candidates(candidates):
    total_candidates = len(candidates)

    total_experience = 0
    total_skill_score = 0
    top_candidates = 0

    for candidate in candidates:
        experience = int(candidate["experience_years"])
        skill_score = int(candidate["skills_score"])

        total_experience += experience
        total_skill_score += skill_score

        if skill_score >= 90:
            top_candidates += 1

    average_experience = round(
        total_experience / total_candidates, 1
    )

    average_skill_score = round(
        total_skill_score / total_candidates, 1
    )

    return {
        "total_candidates": total_candidates,
        "average_experience": average_experience,
        "average_skill_score": average_skill_score,
        "top_candidates": top_candidates
    }