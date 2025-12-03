# Bank Marketing Prediction - Streamlit App
# ============================================
# This file must be run in the command line with: streamlit run myst.py
# Previously, Streamlit has to be installed with pip install streamlit
#
# Adapted from myst_v4.py for the Bank Marketing dataset (Assignment 1)
# Authors: Marcos Santiago Soto, Javier Rodríguez Márquez

import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Bank Deposit Prediction", 
    page_icon="🏦", 
    layout="centered"
)

st.title("🏦 Bank Term Deposit Subscription Prediction")
st.markdown("**Predict whether a customer will subscribe to a term deposit based on their profile.**")

# Load the pack file
@st.cache_resource
def load_pack():
    return load("pack_for_streamlit.joblib")

try:
    pack = load_pack()
    model = pack["model"]
    num_cols = pack["num_cols"]
    cat_cols = pack["cat_cols"]
    num_summary = pack["num_summary"]
    cat_options = pack["cat_options"]
    classes_ = pack["classes_"]
    acc = pack.get("accuracy", None)
except FileNotFoundError:
    st.error("❌ Error: 'pack_for_streamlit.joblib' not found. Please run the deployment notebook first.")
    st.stop()

# Display model accuracy
if acc is not None:
    st.caption(f"📊 Model Test Accuracy: **{acc:.4f}** ({acc*100:.2f}%)")

st.markdown("---")
st.markdown("### Input Customer Information")
st.markdown("Fill in the values for each feature and click **Predict** to get the model's prediction.")

with st.form("prediction_form"):
    
    # ====================
    # NUMERICAL FEATURES
    # ====================
    st.subheader("📈 Numerical Features")
    
    num_inputs = {}
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    for i, c in enumerate(num_cols):
        # Get statistics for this feature
        stats = num_summary.get(c, {"p1": 0, "median": 0, "p99": 100})
        p1 = stats["p1"]
        p99 = stats["p99"]
        med = stats["median"]
        
        # Special handling for pdays_contacted (boolean stored as numeric)
        if c == "pdays_contacted":
            with (col1 if i % 2 == 0 else col2):
                val = st.selectbox(
                    f"{c} (was previously contacted?)",
                    options=["False", "True"],
                    index=0,
                    help="Whether the client was contacted in a previous campaign"
                )
                num_inputs[c] = val == "True"
        
        # Special handling for pdays_clean (can be NaN)
        elif c == "pdays_clean":
            with (col1 if i % 2 == 0 else col2):
                raw = st.text_input(
                    f"{c}",
                    value="" if np.isnan(med) else str(int(med)),
                    placeholder="Leave empty if not contacted",
                    help="Days since last contact (leave empty if never contacted)"
                )
                if raw.strip() == "":
                    num_inputs[c] = np.nan
                else:
                    try:
                        num_inputs[c] = float(raw)
                    except:
                        num_inputs[c] = np.nan
        
        # Regular numerical features
        else:
            with (col1 if i % 2 == 0 else col2):
                raw = st.text_input(
                    f"{c}",
                    value=str(int(med) if med == int(med) else round(med, 2)),
                    placeholder=f"Range: {p1:.0f} - {p99:.0f}",
                    help=f"Typical range: {p1:.0f} to {p99:.0f}, median: {med:.0f}"
                )
                
                if raw.strip() == "":
                    num_inputs[c] = np.nan
                else:
                    try:
                        num_inputs[c] = float(raw)
                    except:
                        num_inputs[c] = np.nan
    
    st.markdown("---")
    
    # ====================
    # CATEGORICAL FEATURES
    # ====================
    st.subheader("📋 Categorical Features")
    
    cat_inputs = {}
    
    col1, col2 = st.columns(2)
    
    for i, c in enumerate(cat_cols):
        opts = cat_options.get(c, ["unknown"])
        default_idx = 0
        
        with (col1 if i % 2 == 0 else col2):
            # Special handling for pdays_contacted (boolean feature stored as categorical)
            if c == "pdays_contacted":
                val = st.selectbox(
                    f"{c} (was previously contacted?)",
                    options=["False", "True"],
                    index=0,
                    help="Whether the client was contacted in a previous campaign"
                )
                # Convert to actual boolean for the model
                cat_inputs[c] = (val == "True")
            else:
                cat_inputs[c] = st.selectbox(
                    f"{c}",
                    options=opts,
                    index=default_idx,
                    help=f"Select the {c} value"
                )
    
    st.markdown("---")
    
    # Submit button
    submitted = st.form_submit_button("🔮 Predict", use_container_width=True)

# ====================
# PREDICTION
# ====================
if submitted:
    # Construct the data point with values given for each feature
    data = {**num_inputs, **cat_inputs}
    
    # Create DataFrame with correct column order (num_cols + cat_cols)
    X_one = pd.DataFrame([data], columns=num_cols + cat_cols)
    
    try:
        # Get probabilities and prediction
        proba = model.predict_proba(X_one)[0]
        pred_idx = int(np.argmax(proba))
        y_pred = classes_[pred_idx]
        
        st.markdown("---")
        st.subheader("🎯 Prediction Result")
        
        # Display prediction with appropriate styling
        if y_pred == "yes":
            st.success(f"### ✅ Prediction: **{y_pred.upper()}**")
            st.markdown("*The customer is predicted to **subscribe** to the term deposit.*")
        else:
            st.warning(f"### ❌ Prediction: **{y_pred.upper()}**")
            st.markdown("*The customer is predicted to **not subscribe** to the term deposit.*")
        
        # Display probabilities
        st.markdown("#### Probabilities per class:")
        prob_df = pd.DataFrame({
            'Class': classes_,
            'Probability': [f"{100*p:.1f}%" for p in proba]
        })
        st.table(prob_df)
        
        # Visual probability bar
        st.markdown("#### Probability Distribution:")
        prob_data = pd.DataFrame({
            'Class': classes_,
            'Probability': proba
        })
        st.bar_chart(prob_data.set_index('Class'))
        
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
        st.stop()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    Bank Marketing Prediction Model - Assignment 1 Extension<br>
    Machine Learning for Business Decision Making - UC3M
    </div>
    """, 
    unsafe_allow_html=True
)
