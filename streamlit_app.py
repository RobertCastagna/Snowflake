import streamlit
import pandas as pd
import requests

streamlit.title("My parent's new diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")

fruit_list = pd.read_csv("fruit_macros.csv")
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvoce Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice).json()

fruityvice_normalized = pd.json_normalize(fruityvice_response)
streamlit.dataframe(fruityvice_normalized)
