import streamlit as st

st.set_page_config(
    page_title="HomeFindr : Real Estate Analytics App",
    page_icon="🏠",
)

st.write("# Welcome to HomeFindr: Your Dream Home🏠 ")

#st.sidebar.success("Select a demo above.")

# Adding an image
image = st.image("Homefindr icon.png", use_column_width=True)

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
- **Chatbot:** Have questions? Our chatbot is here to help! Simply navigate to the chatbot section and ask any queries you have about real estate.

### How to Use:
1. **Select a Demo:** Use the sidebar to select a demo and explore the app's features.
2. **Explore Properties:** Browse through available properties using the interactive map or advanced search.
3. **Save Favorites:** Save your favorite listings by clicking on the heart icon.
4. **Get Insights:** Dive into real-time analytics to gain insights into the housing market.
5. **Chatbot:** Navigate to the chatbot section and ask any questions you have about real estate.

### About Us:
HomeFindr is dedicated to simplifying the home search process and empowering users with data-driven insights. 
We strive to provide the best tools and resources to help you find your dream home effortlessly.

Get started today and find the perfect home for you!
""")

# Adding personal information
st.write("""
### About the Developer:
- **Name:** Dishant Kharkar
- **LinkedIn:** [Dishant Kharkar](https://www.linkedin.com/in/dishant-kharkar-17b508273/)
- **GitHub:** [Dishantkharkar](https://github.com/Dishantkharkar)
- **Email:** dishantkharkar9@gmail.com
""")