def rank_candidates(candidates):
    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: (
            int(candidate["skills_score"]),
            int(candidate["experience_years"])
        ),
        reverse=True
    )

    return ranked_candidates