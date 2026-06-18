import json
import pandas as pd

from model_a import generate_email_model_a
from model_b import generate_email_model_b
from evaluator import evaluate_model


# Load scenarios
with open("scenarios.json", "r", encoding="utf-8") as file:
    scenarios = json.load(file)


# Run Model A
print("Running Model A Evaluation...")

df_a = evaluate_model(
    generate_email_model_a,
    scenarios
)

df_a["model"] = "Model_A"


# Run Model B
print("Running Model B Evaluation...")

df_b = evaluate_model(
    generate_email_model_b,
    scenarios
)

df_b["model"] = "Model_B"


# Combine results
final_df = pd.concat(
    [df_a, df_b],
    ignore_index=True
)


# Save results
final_df.to_csv(
    "results.csv",
    index=False
)


# Print results
print("\nEvaluation Complete\n")

print(final_df)


# Average scores
print("\nAverage Scores\n")

average_scores = (
    final_df
    .groupby("model")["overall_score"]
    .mean()
)

print(average_scores)