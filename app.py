import streamlit as st
import pandas as pd
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent

sys.path.append(str(BASE_DIR / "src"))
from transaction_categorization import categorize_transaction
from financial_advisor import answer_financial_question

st.set_page_config(
    page_title="Personal Finance Assistant",
    page_icon="💰",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #172554, #1e3a8a);
}

[data-testid="stSidebar"] * {
    color: white;
}

h1 {
    color: #172554;
    font-weight: 800;
}

h2 {
    color: #1e3a8a;
}

h3 {
    color: #1e40af;
}

[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv(BASE_DIR / "data" / "cleaned_transactions.csv")

monthly_summary = pd.read_csv(
    BASE_DIR / "data" / "monthly_financial_summary.csv"
)

st.sidebar.title("💰 Personal Finance Assistant")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Spending Analysis",
        "Transaction Categorizer",
        "AI Financial Advisor",
        "AI Savings Tips"
    ]
)

st.title("💰 Personal Finance Assistant")
st.write("Analyze your finances and get AI-powered financial guidance.")

if page == "Dashboard":
    st.header("📊 Financial Dashboard")

    total_income = monthly_summary["Income"].sum()
    total_expense = monthly_summary["Amount"].sum()
    total_savings = monthly_summary["Savings"].sum()

    savings_rate = (
        total_savings / total_income * 100
        if total_income > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Income", f"₹{total_income:,.2f}")
    col2.metric("Total Expenses", f"₹{total_expense:,.2f}")
    col3.metric("Total Savings", f"₹{total_savings:,.2f}")
    col4.metric("Savings Rate", f"{savings_rate:.2f}%")

    st.subheader("Financial Overview")

    chart_data = monthly_summary[["Month", "Income", "Amount"]].copy()

    chart_data["Income"] = pd.to_numeric(chart_data["Income"], errors="coerce")
    chart_data["Amount"] = pd.to_numeric(chart_data["Amount"], errors="coerce")

    st.line_chart(
        chart_data,
        x="Month",
        y=["Income", "Amount"]
    )



    st.subheader("Recent Monthly Summary")

    st.dataframe(
        monthly_summary.tail(10),
        use_container_width=True
    )

elif page == "Spending Analysis":
    st.header("📈 Spending Analysis")

    category_spending = pd.read_csv(
        BASE_DIR / "data" / "category_spending.csv"
    )

    mode_spending = pd.read_csv(
        BASE_DIR / "data" / "mode_spending.csv"
    )

    yearly_spending = pd.read_csv(
        BASE_DIR / "data" / "yearly_spending.csv"
    )

    st.subheader("Monthly Spending")

    monthly_chart = monthly_summary[["Month", "Amount"]].copy()
    monthly_chart["Amount"] = pd.to_numeric(
        monthly_chart["Amount"],
        errors="coerce"
    )

    st.line_chart(
        monthly_chart,
        x="Month",
        y="Amount"
    )

    st.subheader("Top Spending Categories")

    top_categories = category_spending.head(10).set_index("Category")
    st.bar_chart(top_categories["Amount"])

    st.subheader("Spending by Payment Mode")

    mode_chart = mode_spending.set_index("Mode")
    st.bar_chart(mode_chart["Amount"])

    st.subheader("Yearly Spending")

    yearly_chart = yearly_spending.set_index("Year")
    st.bar_chart(yearly_chart["Amount"])

    st.subheader("Category Spending Details")

    st.dataframe(
        category_spending,
        use_container_width=True
    )

elif page == "Transaction Categorizer":
    st.header("🏷️ Transaction Categorizer")

    st.write("Enter a transaction description to predict its category.")

    transaction = st.text_input(
        "Transaction Description",
        placeholder="Example: Uber ride to college"
    )

    if st.button("Categorize Transaction"):
        if transaction.strip():
            category = categorize_transaction(transaction)
            st.success(f"Predicted Category: {category}")
        else:
            st.warning("Please enter a transaction description.")
elif page == "AI Financial Advisor":
    st.header("🤖 AI Financial Advisor")

    category_spending = pd.read_csv(
        BASE_DIR / "data" / "category_spending.csv"
    )

    total_income = monthly_summary["Income"].sum()
    total_expense = monthly_summary["Amount"].sum()
    total_savings = monthly_summary["Savings"].sum()

    savings_rate = (
        total_savings / total_income * 100
        if total_income > 0
        else 0
    )

    category_text = category_spending.head(10).to_string(
        index=False
    )

    st.write("Ask a question about your spending and finances.")

    user_question = st.text_area(
        "Your Question",
        placeholder="Example: How can I reduce my spending?"
    )

    if st.button("Ask AI Advisor"):
        if user_question.strip():
            with st.spinner("Analyzing your financial data..."):
                answer = answer_financial_question(
                    user_question,
                    total_income,
                    total_expense,
                    total_savings,
                    savings_rate,
                    category_text
                )

            st.success("AI Financial Advice")
            st.write(answer)
        else:
            st.warning("Please enter a question.")

elif page == "AI Savings Tips":
    st.header("💡 AI Savings Tips")

    tips_file = BASE_DIR / "data" / "ai_savings_tips.txt"

    if tips_file.exists():
        with open(tips_file, "r", encoding="utf-8") as file:
            tips = file.read()

        st.success("Personalized savings recommendations")
        st.write(tips)
    else:
        st.warning("Savings tips file not found.")