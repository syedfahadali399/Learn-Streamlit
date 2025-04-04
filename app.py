import streamlit as st

# Displays a large title at the top of your app.
st.title("Hello World")

# Renders a header that’s slightly smaller than the title.
st.header("Header Text")

# Creates a subheader for additional emphasis.
st.subheader("Subheader Text")

# A catch-all command that intelligently displays various types of content, from text to data frames.
st.write("Hello World")

# Lets you use Markdown formatting for richer text.
st.markdown("Markdown supports formatting like bold or italics.")

# Outputs simple text.
st.text("Plain text")

# Show a success message.
st.success("Data saved successfully!")

# Show like a dark color message
st.caption("Hello")

# Show a error message.
st.error("Error Spotted")

# Show a warning message.
st.warning("Warning!")

# Show a pop Message
st.popover("Pop")

# st.form(
#    st.form_submit_button("Submit Here")
# )

# For Slider
# value = st.slider("Pick a number", 0, 100, 50)

# For Image
# st.video("demo.mp4")

# Play audio.
# st.audio("sound.mp3", format="audio/mp3")

# Display an image.
# st.image("logo.png", caption="My Logo")

# Shows formatted code blocks.
st.code("print('Hello, world!')", language="python")

# Renders mathematical equations using LaTeX.
st.latex(r"e^{i\pi} + 1 = 0")

# Wrap UI elements inside st.sidebar to place them in the sidebar (e.g., st.sidebar.button("Click me!")).
st.sidebar.button("CLick Me")
st.sidebar.code("print('Hello World!')", language="python")

# Creates a clickable button.
st.button("Click Me")

# Adds a checkbox widget for binary options
st.checkbox("Check this out")

# Presents radio buttons for selecting one option.
st.radio("Choose one", options=["Option 1", "Option 2"])

# Allows users to select multiple options.
st.multiselect("Select multiple", options=["A", "B", "C"])

# Displays a slider for numerical input.
st.slider("Pick a number", min_value=0, max_value=100, value=50)

# A single-line text input field.
st.text_input("Your name")

# A multi-line text input for longer responses.
st.text_area("Comments")

# Accepts numeric input with options for min, max, and step.
st.number_input("Enter a number")

# Provides a calendar widget for date selection.
st.date_input("Pick a date")

# Lets users choose a specific time.
st.time_input("Select a time")

# Enables file uploads from the local machine.
st.file_uploader("Upload a file")

# Opens a color selection tool.
st.color_picker("Pick a color")

# Shows a metric with a delta indicator.
st.metric(label="Temperature", value="70°F", delta="2°F")

# Creates a progress bar (0-100).
st.progress(50)

# Displays a spinner while code runs.
st.spinner("Loading...")

# Collapsible container for hiding/showing content.
st.expander("More info")

# A block for grouping multiple elements together.
st.container(
    # st.write("Hello"),
    # st.text("Hello 2")
)

# Splits the page layout into columns for side-by-side display.
st.columns([1, 2])

# A placeholder container that can later be filled with elements.
st.empty()

# Visualizes geospatial data on a map.
# st.map(data)

# Renders an interactive table for pandas DataFrames.
# st.dataframe(your_dataframe)

# Displays static tabular data.
# st.table(data)

# Renders JSON data in a nicely formatted view.
# st.json(your_json_data)

st.sidebar