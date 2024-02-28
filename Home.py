import streamlit as st

st.set_page_config(
    page_title="HomeFindr : Real Estate Analytics App",
    page_icon="🏠",
)

st.write("# Welcome to HomeFindr: Your Dream Home🏠 ")

#st.sidebar.success("Select a demo above.")

# Adding an image
image = st.image("_b1938dcf-838e-4e56-a063-19ed4ec20ada.jpg", use_column_width=True)

# Writing detailed information about the app
st.write("""
HomeFindr is a real estate analytics app designed to help you find your dream home with ease. 
Our app provides powerful tools and insights to streamline your home search process.

### Key Features:
- **Interactive Maps:** Explore neighborhoods and property locations with interactive maps.
- **Advanced Search:** Filter properties based on your specific criteria, such as price, location, size, and more.
- **Real-time Analytics:** Access up-to-date market trends and analytics to make informed decisions.
- **Save Favorites:** Save your favorite listings to revisit later or share with others.
- **Personalized Recommendations:** Receive personalized recommendations based on your preferences and browsing history.

### How to Use:
1. **Select a Demo:** Use the sidebar to select a demo and explore the app's features.
2. **Explore Properties:** Browse through available properties using the interactive map or advanced search.
3. **Save Favorites:** Save your favorite listings by clicking on the heart icon.
4. **Get Insights:** Dive into real-time analytics to gain insights into the housing market.

### About Us:
HomeFindr is dedicated to simplifying the home search process and empowering users with data-driven insights. 
We strive to provide the best tools and resources to help you find your dream home effortlessly.

Get started today and find the perfect home for you!
""")
