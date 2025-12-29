import streamlit as st
import pandas as pd

st.set_page_config(page_title="Survey Report", page_icon="📊", layout="wide")
st.title("📊 Survey Report Dashboard")
st.markdown("Upload your Excel or CSV file to view and analyze survey data.")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your survey file (Excel/CSV)", type=["xlsx", "xls", "csv"])

if uploaded_file:
    try:
        # Read based on file extension
        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Show success message
        st.success(f"✅ Loaded {len(df):,} rows and {len(df.columns)} columns")

        # Display data
        st.subheader("📋 Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Show basic stats
        st.subheader("📈 Summary Statistics")
        st.write(df.describe())

        # Optional: Download button for cleaned data
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned Data",
            data=csv,
            file_name="survey_report_cleaned.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error loading file: {str(e)}")
