
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "svm_category_model.pkl")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")

def categorize_transaction(description):
    text = description.lower()

    keyword_rules = {
        "Transportation": ["uber", "ola", "taxi", "train", "bus", "metro", "flight", "fuel", "petrol", "diesel"],
        "subscription": ["netflix", "spotify", "prime", "subscription", "recharge", "hotstar"],
        "Health": ["doctor", "hospital", "medicine", "pharmacy", "medical", "clinic"],
        "Apparel": ["clothes", "shirt", "dress", "shoes", "jeans", "apparel"],
        "Food": ["grocery", "vegetables", "restaurant", "food", "lunch", "dinner", "breakfast"],
        "Household": ["furniture", "cleaning", "household", "kitchen", "electricity", "water bill", "gas bill"],
        "Shopping": ["amazon", "shopping", "flipkart", "online order", "purchase"],
        "Income": ["salary", "credited", "income", "paycheck", "wages"]
    }

    for category, keywords in keyword_rules.items():
        if any(keyword in text for keyword in keywords):
            return category

    features = vectorizer.transform([description + " Unknown Cash"])
    return model.predict(features)[0]
