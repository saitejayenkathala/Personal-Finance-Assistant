# Personal Finance Assistant

## Overview

Personal Finance Assistant is a data-driven project that analyzes transaction data, categorizes transactions using machine learning, visualizes spending patterns, and uses Google Gemini AI to provide personalized financial advice.

## Features

- Data cleaning and preprocessing
- Duplicate and missing-value handling
- Transaction categorization using TF-IDF and Linear SVM
- Spending trend visualization
- Category-wise spending analysis
- AI-powered financial health analysis
- Personalized savings recommendations
- User-question-based financial advice

## Technologies

Python, Pandas, Scikit-learn, TF-IDF, Linear SVM, Matplotlib, Jupyter Notebook, Google Gemini API, Git and GitHub.

## Dataset

Daily Household Transactions dataset containing date, transaction mode, category, subcategory, note, amount, income/expense type, and currency.

After preprocessing, the dataset contains 2,452 transactions.

## Machine Learning

A Linear SVM model was trained using TF-IDF features created from transaction descriptions, subcategories, and payment modes.

Test accuracy: **89.61%**

A hybrid keyword and machine-learning approach is used for transaction categorization.

## AI Integration

Google Gemini is used to analyze verified financial statistics, identify spending patterns, answer financial questions, and generate personalized savings recommendations.

The API key is stored securely in `.env` and is excluded from GitHub using `.gitignore`.

## Project Structure

```text
Personal-Finance-Assistant/
├── data/
├── notebooks/
├── src/
├── svm_category_model.pkl
├── tfidf_vectorizer.pkl
├── .gitignore
└── README.md
```

## Setup

Install the required packages:

```bash
python -m pip install pandas scikit-learn matplotlib joblib python-dotenv google-genai jupyter
```

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Run the notebooks in order:

1. Week 4 – Data Cleaning and Categorization
2. Week 5 – Spending Visualization
3. Week 6 – LLM Integration
4. Week 7 – AI Financial Advisor

## Conclusion

The project combines data preprocessing, machine learning, visualization, and generative AI to create a practical Personal Finance Assistant capable of analyzing financial data and providing personalized financial guidance.