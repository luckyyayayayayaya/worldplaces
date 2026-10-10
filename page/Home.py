import streamlit as st

st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 World Cities Explorer")
st.subheader("Welcome to the World Cities Data Application")

st.write("""
This app lets you explore global city data with interactive filters:
- Filter cities by population
- Select capital cities
- Search by country
- Visualize locations on an interactive map
""")

st.divider()
st.markdown("### Go to the City Explorer Page")
if st.button("Open City Data App", type="primary"):
    st.switch_page("pages/app.py")
