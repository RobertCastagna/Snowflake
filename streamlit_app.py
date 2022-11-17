import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

## snowflake data

## temporary break
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_fruit = streamlit.multiselect("Add a fruit: ", list(fruit_list.index))
my_cur.execute("insert into fruit_load_list values ('from Streamlit')")
