# Influencer Marketing ROI Dashboard

## Overview
This project is an open-source dashboard for tracking and visualizing the ROI of influencer campaigns across multiple platforms and products. It is designed for HealthKart's marketing analytics but is adaptable for any brand or agency.

## Features
- Upload or use a simulated influencer campaign dataset
- Track performance of posts, influencers, and campaigns
- Calculate ROI and ROAS (Return on Ad Spend)
- Filter by brand, product, influencer type, and platform
- Visualize top and poor ROI influencers
- Export filtered data as CSV
- Modern, recruiter-friendly UI with branding

## Data Model
The dashboard uses a simulated dataset (`influencer_marketing_roi_simulated.csv`) with the following columns:
- `influencer_id`, `name`, `category`, `gender`, `follower_count`, `platform`
- `post_id`, `post_date`, `caption`, `reach`, `likes`, `comments`
- `campaign`, `product`, `orders`, `revenue`
- `payout_basis`, `payout_rate`, `total_payout`

## Setup Instructions
1. **Clone or download this repository**
2. **Install dependencies:**
   ```bash
   pip install streamlit pandas numpy
   ```
3. **Run the dashboard:**
   ```bash
   streamlit run influencer_roi_dashboard.py
   ```
4. **Upload your own CSV** or use the provided `influencer_marketing_roi_simulated.csv` (auto-loads by default)

## Usage
- Use the sidebar to filter by platform, product, influencer type, and gender
- View campaign metrics, top/poor ROI influencers, and platform/category breakdowns
- Download filtered data for further analysis

## Evaluation Criteria Mapping
- **Data modeling:** Realistic, multi-dimensional influencer dataset
- **Analytical thinking:** ROAS, top/poor ROI, platform and category analysis
- **Product sense:** Practical filters, export, and insights for marketing teams
- **Code quality and UX:** Clean, modular code and modern UI
- **Insights and storytelling:** Actionable tables, charts, and summary
- **Documentation clarity:** This README and in-code comments

## Credits
- Built by Harsh Sharma for HealthKart Influencer Analytics
- Powered by Streamlit, Pandas, and Python 
