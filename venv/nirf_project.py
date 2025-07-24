import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    # Read the Excel file (adjust path if needed)
    df = pd.read_excel('2023overall.xlsx', sheet_name='Table 1')
    return df

df = load_data()

# App title
st.title("🏛️ Indian Institute Rankings 2023")
st.subheader("Analysis of Top Educational Institutes in India")

# Sidebar filters
st.sidebar.header("Filter Data")

# State filter
all_states = ['All'] + sorted(df['State'].unique().tolist())
selected_state = st.sidebar.selectbox("Select State", all_states)

# Rank range filter
min_rank, max_rank = int(df['Rank'].min()), int(df['Rank'].max())
rank_range = st.sidebar.slider("Rank Range", min_rank, max_rank, (1, 100))

# Score filter
score_range = st.sidebar.slider(
    "Score Range", 
    float(df['Score'].min()), 
    float(df['Score'].max()),
    (float(df['Score'].min()), float(df['Score'].max()))
)

# Apply filters
filtered_df = df.copy()
if selected_state != 'All':
    filtered_df = filtered_df[filtered_df['State'] == selected_state]

filtered_df = filtered_df[
    (filtered_df['Rank'] >= rank_range[0]) & 
    (filtered_df['Rank'] <= rank_range[1]) &
    (filtered_df['Score'] >= score_range[0]) & 
    (filtered_df['Score'] <= score_range[1])
]

# Main content
st.header("Filtered Rankings")
st.dataframe(filtered_df[['Name', 'City', 'State', 'Score', 'Rank']], height=400)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Institutes", len(filtered_df))
col2.metric("Average Score", f"{filtered_df['Score'].mean():.2f}")
col3.metric("Top Ranked", filtered_df.iloc[0]['Name'] if not filtered_df.empty else "N/A")

# Visualizations
st.header("Data Visualizations")

# Top institutes chart
st.subheader(f"Top {min(10, len(filtered_df))} Institutes")
top_df = filtered_df.head(10).sort_values('Score', ascending=True)
fig = px.bar(
    top_df, 
    x='Score', 
    y='Name', 
    orientation='h',
    color='Rank',
    text='Score',
    height=500
)
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# State distribution
st.subheader("Distribution by State")
state_counts = filtered_df['State'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']
fig2 = px.pie(
    state_counts, 
    names='State', 
    values='Count',
    hole=0.3
)
st.plotly_chart(fig2, use_container_width=True)

# Score vs Rank
st.subheader("Score vs Rank Correlation")
fig3 = px.scatter(
    filtered_df,
    x='Rank',
    y='Score',
    color='State',
    size='Score',
    hover_name='Name',
    trendline='ols'
)
st.plotly_chart(fig3, use_container_width=True)

# City analysis
st.subheader("Top Cities by Institute Count")
city_counts = filtered_df['City'].value_counts().head(10).reset_index()
city_counts.columns = ['City', 'Count']
fig4 = px.bar(city_counts, x='City', y='Count', color='Count')
st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Data Source: 2023 Indian Institute Rankings")
