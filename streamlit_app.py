import streamlit
import pandas as pd

streamlit.title("My Parent's New Healthy Diner")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

selected_fruit = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruit_to_show = my_fruit_list.loc[selected_fruit]

streamlit.dataframe(fruit_to_show)
