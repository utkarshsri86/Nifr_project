import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as mticker  # Already part of matplotlib

def format_year_axis(ax):
    """Fixes comma in year values on x-axis like 2,021 → 2021"""
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}'))


# Set page config
st.set_page_config(page_title="NIRF Data Analysis", layout="wide")

# Title
st.title("🏛️ NIRF Institutional Ranking Dashboard")
st.markdown("Analyzing Indian educational institute rankings across multiple years")

# File paths
csv_files = [
    r"Book1.csv",
    r"Book2.csv",
    r"Book3.csv",
    r"Book4.csv",
    r"Book5.csv",
    r"Book6.csv",
    r"Book7.csv",
    r"Book8.csv"
]

@st.cache_data
def load_and_merge_data():
    """Load and merge all CSV files"""
    dataframes = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            # Extract year from filename (assuming Book1=2024, Book2=2023, etc.)
            year = 2024 - int(file.split("Book")[1].split(".")[0]) + 1
            df['Year'] = year
            dataframes.append(df)
        except Exception as e:
            st.error(f"Error reading {file}: {str(e)}")
    return pd.concat(dataframes, ignore_index=True)

# Load data
with st.spinner("Loading and merging data..."):
    merged_df = load_and_merge_data()

# Display basic info
st.sidebar.header("Data Overview")
st.sidebar.metric("Total Records", len(merged_df))
st.sidebar.metric("Unique Institutes", merged_df['Name'].nunique())
st.sidebar.metric("Years Covered", f"{merged_df['Year'].min()} - {merged_df['Year'].max()}")

# Main content
tab1, tab2, tab3 = st.tabs([
    "📊 Data Explorer",
    "📈 Trends Analysis",
    "🏆 Top Performers",
])


with tab1:
    st.subheader("Merged Dataset")
    st.dataframe(merged_df.head(100))
    
    # Data summary
    if st.checkbox("Show Data Summary"):
        st.write(merged_df.describe())
    
    # Column explorer
    if st.checkbox("Explore Columns"):
        col = st.selectbox("Select column", merged_df.columns)
        st.write(merged_df[col].value_counts())

with tab2:
    st.subheader("Performance Trends Over Years")
    
    # Select institute
    institute = st.selectbox("Select Institute", sorted(merged_df['Name'].unique()))
    
    # Filter data
    institute_data = merged_df[merged_df['Name'] == institute]
    
    # Plot trends
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=institute_data, x='Year', y='Score', marker='o', ax=ax)
    plt.title(f"Score Trend for {institute}")
    ax.set_xticks(institute_data['Year'].unique())
    format_year_axis(ax)

    st.pyplot(fig)
    
    # Parameter comparison
    st.subheader("Parameter Comparison")
    params = ['TLR', 'RPC', 'GO', 'OI', 'PERCEPTION']
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    institute_data[params].mean().plot(kind='bar', ax=ax2)
    plt.title(f"Average Parameters for {institute}")
    st.pyplot(fig2)

with tab3:
    st.subheader("Top Performing Institutes")
    
    # Select year
    year = st.selectbox("Select Year", sorted(merged_df['Year'].unique(), reverse=True))
    
    # Get top N
    top_n = st.slider("Number of top institutes to show", 5, 50, 10)
    
    # Filter and display
    top_institutes = merged_df[merged_df['Year'] == year].nlargest(top_n, 'Score')
    st.dataframe(top_institutes[['Name', 'City', 'State', 'Score', 'Rank']])
    
    # Visualize
    fig3, ax3 = plt.subplots(figsize=(12, 8))
    sns.barplot(data=top_institutes, x='Score', y='Name', hue='State', dodge=False, ax=ax3)
    plt.title(f"Top {top_n} Institutes in {year}")
    st.pyplot(fig3)

# Save option
if st.sidebar.button("Save Merged Data"):
    save_path = r"U:\utkarsh ppt\pythonnew\venv\PROJECTNIFR\merged_data.csv"
    merged_df.to_csv(save_path, index=False)
    st.sidebar.success(f"Data saved to {save_path}")




tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🔍 Institute Search",
    "📊 Statistical Insights",
    "🔮 Predict Score",
    "📉 Institute Performance Insights",
    "🎯 Smart Suggestions by Year"
])





with tab4:
    st.subheader("Search Institute History (2017 - 2024)")

    # Ensure proper data types
    merged_df['Year'] = pd.to_numeric(merged_df['Year'], errors='coerce')
    merged_df['Score'] = pd.to_numeric(merged_df['Score'], errors='coerce')

    # Dropdown with all unique institute names sorted alphabetically
    institute_list = sorted(merged_df['Name'].dropna().unique())
    selected_institute = st.selectbox("Select Institute", institute_list, key="institute_search_dropdown")

    if selected_institute:
        # Filter the dataset for the selected institute
        search_results = merged_df[merged_df['Name'] == selected_institute].sort_values(by='Year')

        if not search_results.empty:
            st.success(f"Displaying {len(search_results)} records for '{selected_institute}'")

            # Display data
            st.dataframe(search_results)

            # Plot score trend
            if 'Score' in search_results.columns and not search_results['Score'].isnull().all():
                fig4, ax4 = plt.subplots(figsize=(10, 5))
                sns.lineplot(data=search_results, x='Year', y='Score', marker='o', ax=ax4)
                ax4.set_title(f"Score Trend for {selected_institute}")
                ax4.set_xticks(search_results['Year'].unique())
                format_year_axis(ax4)


# Add data labels
                for x, y in zip(search_results['Year'], search_results['Score']):
                   ax4.text(x, y + 0.5, f"{y:.2f}", ha='center', va='bottom', fontsize=9, color='black')

                st.pyplot(fig4)

            else:
                st.warning("Score data is missing or invalid for this institute.")

            # Plot parameter averages
            st.subheader("Average Scores of Key Parameters")
            params = ['TLR', 'RPC', 'GO', 'OI', 'PERCEPTION']
            available_params = [p for p in params if p in search_results.columns]

            if available_params:
                # Ensure numeric conversion
                param_data = search_results[available_params].apply(pd.to_numeric, errors='coerce')
                avg_params = param_data.mean()

                fig5, ax5 = plt.subplots(figsize=(10, 6))
                avg_params.plot(kind='bar', ax=ax5, color='skyblue')
                ax.set_title(f"Average Parameter Scores for {selected_institute}")
                st.pyplot(fig5)
            else:
                st.warning("Some parameter columns are missing in the dataset.")
        else:
            st.error("No data found for the selected institute.")


with tab5:
    st.subheader("📈 Statistical Insights on NIRF Parameters")
    
    numeric_df = merged_df.select_dtypes(include='number')  # Only numeric columns
    
    # Optional year filter
    selected_year = st.selectbox("Select Year for Analysis", sorted(merged_df['Year'].unique(), reverse=True), key="stat_year")
    year_df = merged_df[merged_df['Year'] == selected_year].select_dtypes(include='number')

    st.markdown("### 🔢 Correlation Matrix (Pearson)")
    corr_matrix = year_df.corr(numeric_only=True).round(2)
    st.dataframe(corr_matrix.style.background_gradient(cmap='coolwarm').format(precision=2))


    fig_corr, ax_corr = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax_corr)
    plt.title(f"Correlation Heatmap - {selected_year}")
    st.pyplot(fig_corr)

    st.markdown("### 🧮 Covariance Matrix")
    cov_matrix = year_df.cov().round(2)
    st.dataframe(cov_matrix)

    st.markdown("### 📊 Compare Two Parameters")
    cols = list(numeric_df.columns)
    param1 = st.selectbox("Select Parameter 1", cols, key="param1")
    param2 = st.selectbox("Select Parameter 2", cols, key="param2")

    if param1 and param2 and param1 != param2:
        fig_scatter, ax_scatter = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=year_df, x=param1, y=param2, ax=ax_scatter)
        plt.title(f"{param1} vs {param2} ({selected_year})")
        st.pyplot(fig_scatter)

        correlation_value = year_df[[param1, param2]].corr().iloc[0, 1]
        st.success(f"Pearson Correlation Coefficient between **{param1}** and **{param2}**: `{correlation_value:.2f}`")


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

with tab6:
    st.subheader("🔮 Predict Institute Score using Key Parameters")

    # Choose features
    features = ['TLR', 'RPC', 'GO', 'OI', 'PERCEPTION']
    available_features = [col for col in features if col in merged_df.columns]

    if len(available_features) < 3:
        st.warning("Not enough feature columns found in data to build a model.")
    else:
        df_model = merged_df.dropna(subset=available_features + ['Score'])
        X = df_model[available_features]
        y = df_model['Score']

        # Split and train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        st.success(f"Model Trained — R² Score: {r2:.2f}, MSE: {mse:.2f}")

        # User input for prediction
        st.markdown("### 🔢 Predict Score from Input Parameters")
        user_input = {}
        for feat in available_features:
            user_input[feat] = st.slider(f"{feat} Score", 0.0, 100.0, 50.0)

        input_df = pd.DataFrame([user_input])
        predicted_score = model.predict(input_df)[0]
        st.info(f"📌 Predicted Score: **{predicted_score:.2f}** based on input parameters")

with tab7:
    st.subheader("📉 Deep Dive: Why Did This Institute Get That Rank?")
    
    institute_list = sorted(merged_df['Name'].dropna().unique())
    selected = st.selectbox("Select Institute", institute_list, key="insights_institute")

    if selected:
        df_inst = merged_df[merged_df['Name'] == selected].sort_values(by="Year")

        if df_inst.empty:
            st.error("No data found for selected institute.")
        else:
            st.success(f"{len(df_inst)} records found for '{selected}'")

            for idx, row in df_inst.iterrows():
                st.markdown(f"### 📅 Year: {int(row['Year'])}")
                st.markdown(f"**Score**: `{row['Score']}` | **Rank**: `{row['Rank']}`")
                
                # Get scores for key parameters
                params = ['TLR', 'RPC', 'GO', 'OI', 'PERCEPTION']
                param_scores = {p: row.get(p, None) for p in params if not pd.isnull(row.get(p))}

                if param_scores:
                    avg_score = sum(param_scores.values()) / len(param_scores)

                    # Display parameter scores
                    st.markdown("**🧮 Parameter Scores:**")
                    st.write(param_scores)

                    # Plot bar
                    fig_bar, ax_bar = plt.subplots()
                    pd.Series(param_scores).plot(kind='bar', color='orange', ax=ax_bar)
                    ax_bar.set_title(f"Parameter Breakdown ({int(row['Year'])})")
                    format_year_axis(ax_bar)
                    st.pyplot(fig_bar)

                    # Identify weak areas
                    sorted_params = sorted(param_scores.items(), key=lambda x: x[1])
                    weakest = sorted_params[0]

                    st.markdown(f"**🚨 Weakest Parameter:** `{weakest[0]}` with score `{weakest[1]:.2f}`")

                    # Suggestion engine
                    suggestions = {
                        'TLR': "Improve faculty-student ratio, recruit PhD faculty, enhance online learning & regional language content.",
                        'RPC': "Increase research publications, patents, industry collaboration, and citation quality.",
                        'GO': "Boost graduation rates and encourage more Ph.D. completions.",
                        'OI': "Increase student diversity, support women and underprivileged students, and improve facilities for physically challenged.",
                        'PERCEPTION': "Enhance visibility through media, alumni success stories, and industry partnerships."
                    }

                    suggestion = suggestions.get(weakest[0], "Review all performance parameters and boost weakest areas.")
                    st.markdown(f"**💡 What Can Be Improved:** {suggestion}")
                else:
                    st.warning("No parameter data available for this year.")

with tab8:
    st.subheader("🎯 Smart Suggestions by Year")

    institute_list = sorted(merged_df['Name'].dropna().unique())
    selected = st.selectbox("Select Institute", institute_list, key="smart_suggestion_dropdown")

    if selected:
        df_inst = merged_df[merged_df['Name'] == selected].sort_values(by="Year")

        if df_inst.shape[0] < 2:
            st.warning("Need at least 2 years of data to show suggestions.")
        else:
            st.success(f"Tracking changes in parameters from year to year for '{selected}'")

            # Parameters and suggestions
            params = ['TLR', 'RPC', 'GO', 'OI', 'PERCEPTION']
            suggestions = {
                'TLR': "👨‍🏫 Focus on improving faculty resources and student-faculty ratio.",
                'RPC': "📚 Boost research output and patent filing.",
                'GO': "🎓 Work on graduation efficiency and Ph.D. output.",
                'OI': "🌍 Increase diversity, scholarships, and support systems.",
                'PERCEPTION': "📢 Improve brand image via outreach and employer engagement."
            }

            # Compare year-wise
            for i in range(1, df_inst.shape[0]):
                curr_year = int(df_inst.iloc[i]['Year'])
                prev_year = int(df_inst.iloc[i - 1]['Year'])
                
                st.markdown(f"### 📆 {prev_year} ➡️ {curr_year}")
                for param in params:
                    prev_val = df_inst.iloc[i - 1].get(param, None)
                    curr_val = df_inst.iloc[i].get(param, None)

                    if pd.notnull(prev_val) and pd.notnull(curr_val):
                        delta = curr_val - prev_val
                        trend = "👍 Improved" if delta > 0 else ("⚠️ Dropped" if delta < 0 else "➖ No Change")
                        st.markdown(f"**{param}**: {prev_val:.2f} → {curr_val:.2f} ({trend})")

                        if delta < 0:
                            st.markdown(f"💡 _Suggestion_: {suggestions.get(param)}")

                st.markdown("---")

