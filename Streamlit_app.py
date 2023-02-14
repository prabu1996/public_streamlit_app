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


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# # streamlit.text("Hello from Snowflake:")
# # streamlit.text("The fruit load list contains")
# streamlit.header("The fruit load list contains")
# # streamlit.text(my_data_row)
# streamlit.dataframe(my_data_row)

my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)


fruit_choice = streamlit.text_input('What fruit would you like to add ?','kiwi')
streamlit.write('The user entered ', fruit_choice)

my_cur.execute("insert into fruit load list vallues('from streamlit')")
