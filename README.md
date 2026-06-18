# Email Generation Assistant

## Overview

This project is an AI-powered Email Generation Assistant built using Large Language Models (LLMs).

The assistant generates professional emails based on:

* Intent
* Key Facts
* Tone

The project also includes:

* Advanced Prompt Engineering
* Custom Evaluation Metrics
* Automated Model Comparison
* CSV Report Generation

---

# Features

## Email Generation

The assistant generates complete professional emails containing:

* Subject
* Greeting
* Body
* Closing

---

## Two Prompting Strategies

### Model A

Simple prompting approach.

### Model B

Advanced prompting approach using:

* Role Prompting
* Few-Shot Prompting
* Structured Instructions

---

# Evaluation Metrics

The project evaluates generated emails using 3 custom metrics.

---

## 1. Fact Recall Score

Measures whether the generated email includes all required facts.

### Logic

* Each fact is checked against the generated email.
* Score = matched facts / total facts

---

## 2. Tone Accuracy Score

Measures whether the generated email matches the requested tone.

### Supported Tones

* formal
* professional
* warm
* empathetic
* friendly
* respectful
* enthusiastic
* polite

---

## 3. Format Adherence Score

Checks whether the email contains:

* Subject line
* Greeting
* Closing

---

# Project Structure

email-generation-assistant/

├── main.py
├── model_a.py
├── model_b.py
├── metrics.py
├── evaluator.py
├── scenarios.json
├── results.csv
├── requirements.txt
├── .env
├── README.md
└── reports/
└── analysis.txt

---

# Installation

## 1. Clone Repository

git clone <your_github_repo>

cd email-generation-assistant

---

## 2. Install Dependencies

pip install -r requirements.txt

---

# Setup API Key

Create a `.env` file.

Add:

OPENROUTER_API_KEY=your_openrouter_api_key

---

# Run Project

python main.py

---

# Output

The project generates:

## results.csv

Contains:

* Scenario ID
* Intent
* Tone
* Fact Recall Score
* Tone Accuracy Score
* Format Adherence Score
* Overall Score
* Generated Email
* Model Name

---

# Models Used

The project uses free OpenRouter models.

Default model:

openai/gpt-oss-120b:free

You can change the model inside:

* model_a.py
* model_b.py

---

# Example Console Output

Running Model A Evaluation...

Running Model B Evaluation...

Evaluation Complete

Average Scores

Model_A    0.71

Model_B    0.89

---

# Advanced Prompt Engineering

Model B uses:

## Role Prompting

"You are a senior executive communications specialist."

## Few-Shot Prompting

Includes example input-output email pairs.

## Structured Prompting

Strict formatting instructions for:

* Subject
* Greeting
* Body
* Closing

---

# Comparative Analysis

## Higher Performing Model

Model B typically performs better because:

* Better fact retention
* Improved formatting
* More consistent tone control

## Biggest Failure Mode of Model A

* Missing facts
* Inconsistent formatting
* Weak tone alignment

## Recommended Production Model

Model B is recommended for production because it achieves:

* Higher overall scores
* Better reliability
* More professional outputs

---

# Requirements

* Python 3.10+
* OpenRouter API Key

---

# Install Requirements

pip install -r requirements.txt

---

# requirements.txt

requests

pandas

python-dotenv

---

# OpenRouter API Key

Get API key from:

https://openrouter.ai/keys

---

# Free Models

Browse free models:

https://openrouter.ai/models?max_price=0

---

# Author
