import streamlit as st
import pandas as pd
import pickle
#import plotly.express as px
#import plotly

# Add a Markdown component to display the greeting
st.markdown("### Hi, My name is Nadeem and this app is developed by me")

links_row = "<a href='https://www.linkedin.com/in/nadeem-akhtar-/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>" \
            " | " \
            "<a href='https://github.com/NadeemAkhtar1947' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/github.png' width='30'></a>" \
            " | " \
            "<a href='https://www.kaggle.com/mdnadeemakhtar/code' target='_blank'>" \
            "<img src='https://www.kaggle.com/static/images/site-logo.png' width='30'></a>" \
            " | " \
            "<a href='https://tyrex.netlify.app/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/globe--v1.png' width='30'></a>"

# Display the links row using Markdown
st.markdown(links_row, unsafe_allow_html=True)


# Function to increment view count
def increment_views():
    # Read current view count from file
    try:
        with open("view_count.txt", "r") as file:
            views = int(file.read())
    except FileNotFoundError:
        # If file doesn't exist, initialize view count to 0
        views = 0

    # Increment view count
    views += 1

    # Write updated view count to file
    with open("view_count.txt", "w") as file:
        file.write(str(views))

    return views

# Increment view count only once per user visit
if not st.session_state.get("view_counted", False):
    total_views = increment_views()
    st.session_state.view_counted = True
else:
    total_views = int(open("view_count.txt", "r").read())

# Display total views
st.write("Total Views:", total_views)

# Your Streamlit app code goes here...



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







