import streamlit as st  # Importing the Streamlit library

# Title of the app
st.title("Machine Learning Project")

# Headers to organize the content
st.header("This is header")  # Main section header
st.subheader("This is subheader")  # Subsection header (similar to h2-h3)

# Displaying plain text
st.text("Hello Streamlit")  # Simple text display

# Markdown examples
st.markdown(" # This is our first markdown")  # Level 1 Markdown heading
st.markdown(" ##### This is our first markdown")  # Level 5 Markdown heading

# Color-coded message displays
st.success("Successfuk Done")  # Green success message
st.info("Information")  # Blue info message
st.warning("This is a warning")  # Yellow warning message

# Displaying an exception (useful for debugging)
st.exception("NameError('name od is not defined')")

# Displaying help documentation for a module and function
import pandas
st.help(pandas)  # Shows help for the pandas module

st.help(range)  # Shows help for the built-in range function

# Writing output using st.write (handles text, data, and other objects)
st.write("Text with Write")  # Displaying text
st.write(range(10))  # Displaying a range object (0 to 9)

# Displaying an image using PIL
from PIL import Image

img = Image.open("1.jpeg")  # Opening an image file
st.image(img)  # Displaying the image in the Streamlit app
