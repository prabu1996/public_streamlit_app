import streamlit
import snowflake.connector

streamlit.title("Surya Kumar yadav")
streamlit.header("Indian cricketer")
streamlit.text("Surya is also called by 'Mr.360 of India'")

import pandas as pd

my_object=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_object=my_object.set_index('Fruit')

# streamlit.multiselect("pick some fruits:",list(my_object.index))
# streamlit.multiselect("pick some fruits:",list(my_object.index),['Cantaloupe','Grapes'])
# streamlit.dataframe(my_object)

fruits_selected=streamlit.multiselect("pick some fruits:",list(my_object.index),['Cantaloupe','Grapes'])
fruits_to_show =my_object.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
