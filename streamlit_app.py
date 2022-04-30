import streamlit
import pandas

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
# let's pick a pick list for user to choose a fruit by themselve
fruit_selected = streamlit.multiselect("Pick fruits of your choice:" , list( my_fruit_list.index), ['Avocado','Strawberries'])
fruit_selected_loc = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_selected_loc)
