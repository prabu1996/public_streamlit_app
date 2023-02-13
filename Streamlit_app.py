import streamlit

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
