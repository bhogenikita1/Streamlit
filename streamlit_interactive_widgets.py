import streamlit as st  # Importing Streamlit for UI components

# Title of the application
st.title("Machine Learning Project")

# Image display using PIL
from PIL import Image
img = Image.open("1.jpeg")  # Opening the image file
# st.image(img)  # Optionally display image (commented out)
st.image(img, width=300, caption="Machine Learning Image")  # Display image with width and caption

# Adding a video file
vid_file = open("large.mp4", "rb")  # Opening video file in binary read mode
vid_bytes = vid_file.read()  # Reading video bytes
st.video(vid_bytes)  # Displaying the video

# Adding audio file
audio_file = open("pop.mp3", "rb").read()  # Opening and reading audio file
st.audio(audio_file)  # Playing the audio

# Checkbox example to show/hide widget
if st.checkbox("Show/Hide"):
    st.text("Showing or hiding Widgets")

# Radio button example
status = st.radio("What is your status", ("Active", "Inactive"))  # Single selection
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Try To Activate it")

# SelectBox - single selection dropdown
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor", "BusinessMan"])
st.write("You selected option: ", occupation)

# Multiselect - allows multiple selections
location = st.multiselect("Where do you work", ("Karnataka", "Mumbai", "Pune", "Delhi"))
st.write("You Selected", len(location), "location(s)")

# Slider - select a value in a range
level = st.slider("What is your level", 1, 5)

# Button examples
st.button("Single Button")

if st.button("About"):
    st.text("Streamlit is cool")

if st.button("Submit"):
    st.text("Successfully Submitted")

# Text input
first_name = st.text_input("Enter your first name", "Type Here..")
if st.button("Submit", key="1"):
    result = first_name.title()  # Capitalizing the name
    st.success(result)

# Text area input
message = st.text_area("Enter your msg", "Type here..")
if st.button("Submit", key="2"):
    result = message.title()  # Capitalizing the message
    st.success(result)

# Date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())  # Default to current date

# Time input
the_time = st.time_input("The time is: ", datetime.time())  # Default to current time

# Displaying JSON data
st.text("Display JSON Data")
st.json({
    "Name": "Nikita",
    "Gender": "female"
})

# Displaying raw code
st.text("Display Raw Code")
st.code("import numpy as np")  # Code snippet display

# Display code and run it
with st.echo():
    import pandas as pd
    df = pd.DataFrame()  # Creates and displays code block

# Progress bar example
import time
my_bar = st.progress(0)  # Initialize progress bar
for p in range(10):
    my_bar.progress(p + 10)  # Updating progress bar

# Spinner example (loading animation)
with st.spinner("Waiting...."):
    time.sleep(5)  # Simulate long computation
st.success("Finished")  # Display success message
