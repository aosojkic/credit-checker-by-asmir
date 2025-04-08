import streamlit as st

st.set_page_config(page_title="Creditworthiness Checker", layout="centered")

st.title("📋 Creditworthiness Checker")
st.markdown("Check your loan approval status based on income, credit score, and debt.")
st.markdown("**By Asmir Osojkic**")
st.markdown("---")

# User Inputs
income = st.number_input("Monthly Income ($)", min_value=0.0, format="%.2f")
debt = st.number_input("Monthly Debt Payments ($)", min_value=0.0, format="%.2f")
credit_score = st.number_input("Credit Score (300 - 850)", min_value=300, max_value=850, step=1)
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed", "Student"])
age = st.number_input("Age", min_value=0, step=1)

# Run when button is clicked
if st.button("Check Creditworthiness"):
    if age < 18:
        st.error("❌ Applicant must be 18 or older.")
    elif income == 0:
        st.error("❌ Monthly income cannot be $0.")
    else:
        dti = debt / income
        approved = False
        risk = "High"

        if credit_score >= 700 and dti < 0.35 and employment_status == "Employed":
            risk = "Low"
            approved = True
        elif credit_score >= 640 and dti < 0.45:
            risk = "Medium"
            approved = True

        # Display results
        st.markdown("### 📊 Results:")
        st.write(f"**Debt-to-Income Ratio:** {dti:.2f}")
        st.write(f"**Credit Score:** {credit_score}")
        st.write(f"**Risk Level:** {risk}")
        st.success("✅ Approved!") if approved else st.error("❌ Declined.")

st.markdown("---")
st.caption("Made by Asmir Osojkic") 
