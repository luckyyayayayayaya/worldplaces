import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

st.title('World Cities')
df = pd.read_csv('worldcities.csv')

# Minimal Population slider (unit: millions)
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)

# Capital multi-select, default empty
capital_filter = st.sidebar.multiselect(
    'Capital Selector',
    df.capital.unique(),
    []
)

# Country input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
submit_pressed = form.form_submit_button("Apply")

# Filter population
df = df[df.population >= population_filter * 1_000_000]
# Filter capital
df = df[df.capital.isin(capital_filter)]

# Country filter only triggers when Apply button is clicked
if submit_pressed:
    if country_filter != 'ALL':
        df = df[df.country == country_filter]

# Render map and table
st.map(df)
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

# Plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20,5))
city_count = df.groupby('country')['population'].sum().sort_values(ascending=False)
city_count.plot(kind='bar', ax=ax)
st.pyplot(fig)
