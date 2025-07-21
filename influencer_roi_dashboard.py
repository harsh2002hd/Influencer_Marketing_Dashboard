import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Influencer Marketing ROI Dashboard", layout="wide")

# --- Sidebar Branding ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.markdown("""
# Influencer ROI
#### HealthKart Campaigns
---
""")

# --- Main Header ---
st.markdown("""
<style>
.big-title {
    font-size:3rem !important;
    font-weight:700;
    color:#FF4B4B;
    letter-spacing: -1px;
}
.metric-label {
    color: #555;
    font-size: 1.1rem;
}
.section-title {
    font-size:1.5rem;
    font-weight:600;
    margin-top:2em;
    color:#1a73e8;
}
</style>
<div class="big-title">📊 Influencer Marketing ROI Dashboard</div>
""", unsafe_allow_html=True)

st.markdown(
    "<span class='metric-label'>Track, analyze, and optimize your influencer campaigns with HealthKart.</span>",
    unsafe_allow_html=True
)

# 1. Data Upload
st.sidebar.header("Upload Data")
default_file = "influencer_marketing_roi_simulated.csv"
use_default = False
if os.path.exists(default_file):
    use_default = True

uploaded_file = st.sidebar.file_uploader("Upload influencer_marketing_roi_simulated.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data loaded from upload!")
elif use_default:
    df = pd.read_csv(default_file)
    st.info(f"Using default file: {default_file}")
else:
    st.warning("Please upload influencer_marketing_roi_simulated.csv to proceed.")
    st.stop()

# 2. Data Preview
with st.expander("🔍 Preview Data", expanded=False):
    st.dataframe(df.head(), use_container_width=True, height=250)

# 3. Data Cleaning (remove duplicates, missing, drop unnecessary columns)
df = df.drop_duplicates()
df = df.dropna()
if 'post_url' in df.columns:
    df = df.drop(columns=['post_url'])

# 4. Sidebar Filters
with st.sidebar:
    st.header("Filters")
    platforms = st.multiselect("Platform", options=df['platform'].unique(), default=list(df['platform'].unique()))
    brands = st.multiselect("Product", options=df['product'].unique(), default=list(df['product'].unique()))
    influencer_types = st.multiselect("Influencer Category", options=df['category'].unique(), default=list(df['category'].unique()))
    genders = st.multiselect("Gender", options=df['gender'].unique(), default=list(df['gender'].unique()))

# 5. Apply Filters
filtered_df = df[
    (df['platform'].isin(platforms)) &
    (df['product'].isin(brands)) &
    (df['category'].isin(influencer_types)) &
    (df['gender'].isin(genders))
]

# --- Metrics Section ---
st.markdown('<div class="section-title">📈 Campaign Performance Metrics</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.0f}", help="Sum of all campaign revenue.")
col2.metric("Total Orders", int(filtered_df['orders'].sum()), help="Total number of orders generated.")
col3.metric("Total Payout", f"${filtered_df['total_payout'].sum():,.0f}", help="Total payout to influencers.")
roas = filtered_df['revenue'].sum() / filtered_df['total_payout'].sum() if filtered_df['total_payout'].sum() > 0 else np.nan
col4.metric("ROAS", f"{roas:.2f}", help="Return on Ad Spend (Revenue / Payout)")

# --- Top Influencers ---
st.markdown('<div class="section-title">🏆 Top 5 Influencers by Revenue</div>', unsafe_allow_html=True)
top_influencers = (
    filtered_df.groupby(['influencer_id', 'name'])['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
st.dataframe(top_influencers, use_container_width=True, hide_index=True)

# --- Poor ROI Influencers ---
st.markdown('<div class="section-title">⚠️ Bottom 5 Influencers by ROAS</div>', unsafe_allow_html=True)
roi_df = (
    filtered_df.groupby(['influencer_id', 'name'])
    .agg({'revenue': 'sum', 'total_payout': 'sum', 'orders': 'sum'})
    .reset_index()
)
roi_df['roas'] = roi_df['revenue'] / roi_df['total_payout']
poor_roi = roi_df[roi_df['orders'] > 0].sort_values('roas').head(5)
st.dataframe(poor_roi[['influencer_id', 'name', 'revenue', 'total_payout', 'roas']], use_container_width=True, hide_index=True)

# --- Revenue by Platform ---
st.markdown('<div class="section-title">💹 Revenue by Platform</div>', unsafe_allow_html=True)
rev_by_platform = filtered_df.groupby('platform')['revenue'].sum().sort_values(ascending=False)
st.bar_chart(rev_by_platform, use_container_width=True)

# --- Pie Chart: Influencer Category ---
st.markdown('<div class="section-title">🧑‍💼 Distribution by Influencer Category</div>', unsafe_allow_html=True)
cat_counts = filtered_df['category'].value_counts()
fig = cat_counts.plot.pie(autopct='%1.1f%%', ylabel='', figsize=(4,4)).get_figure()
st.pyplot(fig)

# --- Export Data ---
st.markdown('<div class="section-title">⬇️ Export Data</div>', unsafe_allow_html=True)
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_influencer_data.csv",
    mime="text/csv"
)

# --- Insights ---
with st.expander("💡 Insights Summary", expanded=False):
    st.markdown("""
    - **Top Influencers:** See above table for those driving the most revenue.
    - **Poor ROI:** Influencers with lowest ROAS are highlighted for review.
    - **Platform Performance:** Bar chart shows which platforms are most effective.
    - **Category Distribution:** Pie chart shows influencer type mix.
    - **Use filters** to drill down by brand, platform, or persona.
    """)

# --- Footer ---
st.markdown("""
---
<center>
    <span style='color: #888;'>Built with ❤️ using Streamlit | HealthKart Influencer Analytics</span>
</center>
""", unsafe_allow_html=True) 