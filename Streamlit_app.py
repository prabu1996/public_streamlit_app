import streamlit
# import snowflake.connector
import streamlit
import pandas
import requests
# import snowflake.connector
from urllib.error import URLError

# streamlit.title("Surya Kumar yadav")
# streamlit.header("Indian cricketer")
# streamlit.text("Surya is also called by 'Mr.360 of India'")

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 and blueberry oatmeal')
streamlit.text('kale ,spinach & rocket smoothie')
streamlit.text('hard-boiled egg')
streamlit.text('chocolates')
streamlit.header('🍇build your 🍌🥭first smoothie🍇')

import pandas as pd

my_object=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_object=my_object.set_index('Fruit')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:",list(my_object.index))
streamlit.multiselect("pick some fruits:",list(my_object.index),['Cantaloupe','Grapes'])
streamlit.dataframe(my_object)

fruits_selected=streamlit.multiselect("pick some fruits:",list(my_object.index),['Cantaloupe','Grapes'])
fruits_to_show =my_object.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


# import requests
# # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# # streamlit.text(fruityvice_response)


# def get_fruityvice_data(this_fruit_choice):
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     return fruityvice_normalized
  
  
# # streamlit.header("Fruityvice Fruit Advice!")
# # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # # write your own comment - what does this do?
# # streamlit.dataframe(fruityvice_normalized)
# # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# # streamlit.write('The user entered ', fruit_choice)


# try:
#    fruit_choice = streamlit.text_input('What fruit would you like information about?')
#    if not fruit_choice:
#         streamlit.error("please select a fruit to get information.")
#    else:
#       back_from_function=get_fruityvice_data(fruit_choice)
#       streamlit.dataframe(back_from_function)

# except URLError as e:
#   streamlit.error()
# # streamlit.stop()
# # import snowflake.connector
# streamlit.header("The fruit load list contains:")
# #Snowflake-related functions
# def get_fruit_load_list():
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("select * from fruit_load_list")
#         return my_cur.fetchall()
# #Add a button to load the fruit
# if streamlit.button('Get Fruit Load List'):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     my_data_rows = get_fruit_load_list()
#     streamlit.dataframe(my_data_rows) 
# ##my_cur = my_cnx.cursor()
# ##my_cur.execute("SELECT * from fruit_load_list")
# ##my_data_rows= my_cur.fetchall()
# ## streamlit.header("The fruit Load List contains:")
# ##streamlit.dataframe(my_data_rows)
# #allow the end user to add a fruit to the list
# def insert_row_snowflake(new_fruit):
#     with my_cnx.cursor() as my_cur:
#          my_cur.execute("insert into fruit_load_list values('from streamlit')") 
#          return "Thanks for adding"+new_fruit
# add_my_fruit = streamlit.text_input('What Fruit Would You Like To Add?')
# if streamlit.button('Add a fruit to the list'):
#      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#      back_from_function=insert_row_snowflake(add_my_fruit)
#      streamlit.text(back_from_function)
# streamlit.write('Thanks For Adding',add_my_fruit)
# # my_cur.execute("insert into fruit_load_list values('from streamlit')")

# streamlit.stop()
