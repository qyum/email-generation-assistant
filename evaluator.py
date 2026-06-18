import pandas as pd

from metrics import (
fact_recall_score,
tone_accuracy_score,
format_adherence_score
)

def evaluate_model(model_function, scenarios):


    results = []

    for scenario in scenarios:

        generated_email = model_function(
            scenario["intent"],
            scenario["facts"],
            scenario["tone"]
        )

        fact_score = fact_recall_score(
            generated_email,
            scenario["facts"]
        )

        tone_score = tone_accuracy_score(
            generated_email,
            scenario["tone"]
        )

        format_score = format_adherence_score(
            generated_email
        )

        overall_score = round(
            (
                fact_score
                + tone_score
                + format_score
            ) / 3,
            2
        )

        results.append({
            "scenario_id": scenario["id"],
            "intent": scenario["intent"],
            "tone": scenario["tone"],
            "fact_score": fact_score,
            "tone_score": tone_score,
            "format_score": format_score,
            "overall_score": overall_score,
            "generated_email": generated_email
        })

    return pd.DataFrame(results)

