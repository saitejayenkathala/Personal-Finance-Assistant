import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def generate_savings_tips(total_income, total_expense, total_savings, top_categories):
    category_data = top_categories.copy()
    category_data["Percentage"] = (
        category_data["Amount"] / total_expense * 100
    )

    category_text = category_data.to_string(
        index=False,
        formatters={"Amount": "{:.2f}".format, "Percentage": "{:.2f}%".format}
    )

    prompt = f"""
    Analyze these verified personal finance statistics.

    Total Income: ₹{total_income:.2f}
    Total Expenses: ₹{total_expense:.2f}
    Total Savings: ₹{total_savings:.2f}

    Top Spending Categories:
    {category_text}

    These figures cover the complete available dataset period.

    Provide exactly 3 practical and personalized savings recommendations.

    Do not include any numbers, percentages, amounts, monthly values, annual values, yearly values, savings rates, or calculated financial statistics in your response.

    Do not make assumptions about the time period of the data.

    Focus only on explaining spending patterns and giving actionable advice.

    Base the recommendations only on the supplied categories and financial patterns.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text