import streamlit
import pandas as pd

streamlit.title("My parent's new diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")

fruit_list = pd.read_csv("fruit_macros.csv")
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(fruit_list.index))
#fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_list)
