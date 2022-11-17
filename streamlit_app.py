import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


def get_fruityvice_data(choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice).json()
  return pd.json_normalize(fruityvice_response)


def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  

streamlit.title("My parent's new diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")

fruit_list = pd.read_csv("fruit_macros.csv")
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvoce Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
    streamlit.error("Please select a fruit to get informaton.")
  else:
    function_data = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(function_data)
    
except URLError as e:
  streamlit.error()
  
my_cur = my_cnx.cursor() 

my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  data_rows = get_fruit_load_list()
  streamlit.dataframe(data_rows)
 
## temporary break
streamlit.stop()

my_cur.execute("insert into fruit_load_list values ('from Streamlit')")
