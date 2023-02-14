import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError


# import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale ,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled egg')
streamlit.text('🥑🍞 avacado_toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected =streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Cantaloupe','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# upto lesson 12 time to tidy up ues this

# streamlit.header("Fruityvice Fruit Advice!")
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# # import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# # streamlit.text(fruityvice_response.json())

# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)

# at lesson 12 try except use below codes


def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+'this_fruit_choice')
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information')
  else:
   back_from_function=get_fruity_vice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# streamlit.stop()

streamlit.header('The fruit load list contains:')
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()
    
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('jackfruit'),('papaya'),('guava'),('kiwi') ")
        return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input( 'What fruit would you like to add?' )
if streamlit.button('Add a Fruit to the List'):
  my_cnx  = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function= insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
    
    
    
    

# fruit_choice = streamlit.text_input('What fruit would you like to add ?','kiwi')
# streamlit.write('The user entered ', fruit_choice)

# # my_cur.execute("insert into fruit_load_list vallues('from streamlit')")



