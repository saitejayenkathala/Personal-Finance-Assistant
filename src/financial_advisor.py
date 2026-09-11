import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_financial_question(user_question, total_income, total_expense, total_savings, savings_rate, category_text):
    prompt = f"""
    You are a personal finance assistant.

    Use the following verified financial information to answer the user's question.

    Total Income: ₹{total_income:.2f}
    Total Expenses: ₹{total_expense:.2f}
    Total Savings: ₹{total_savings:.2f}
    Savings Rate: {savings_rate:.2f}%

    Spending Categories:
    {category_text}

    User Question:
    {user_question}

    Give clear, practical and personalized advice.
    Use only the supplied financial information.
    Do not invent financial values.
    Do not calculate monthly or annual amounts.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text