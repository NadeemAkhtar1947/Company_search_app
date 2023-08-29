import streamlit as st
import pandas as pd
import pickle
#import plotly.express as px
#import plotly
st.title("Company Search App")

data = pickle.load(open('company.pkl','rb'))

company_name = st.selectbox(
'Enter  Company  Name',
data['Company'].values)

def get_company_details(company_name):
    # Filter data based on the input company name
    filtered_data = data[data['Company'] == company_name]

    if not filtered_data.empty:
        # Extract the row of company data
        company_row = filtered_data.iloc[0]

        # Display company details
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"Company Name : {company_row['Company']}")
        with col2:
            st.success(f"Global Rank : {company_row['Global Rank']}")
        with col1:
            st.success(f"Sales ($billion) : {company_row['Sales ($billion)']}")
        with col2:
            st.success(f"Profit ($billion) : {company_row['Profits ($billion)']}")
        with col1:
            st.success(f"Assets ($billion) : {company_row['Assets ($billion)']}")
        with col2:
            st.success(f"Market Value ($billion) : {company_row['Market Value ($billion)']}")
        with col1:
            st.success(f"Country : {company_row['Country']}")
        with col2:
            st.success(f"Continent : {company_row['Continent']}")
        with col1:
            st.success(f"Latitude : {company_row['Latitude']}")
        with col2:
            st.success(f"Longitude : {company_row['Longitude']}")
    else:
        st.error(f"No details found for company: {company_name}")

if st.button('Search'):
    get_company_details(company_name)

# Create a Plotly scatter_geo figure
#fig = px.scatter_geo(data, lat='Latitude', lon='Longitude', color='Company', title='Companies Across the World')

# Display the Plotly figure using Streamlit
#st.plotly_chart(fig)

# Add custom text at the bottom using Markdown
st.markdown("---")
st.markdown("Copyright @Nadeem")







