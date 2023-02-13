import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale ,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled egg')
streamlit.text('🥑🍞 avacado_toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected =streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Cantaloupe','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


