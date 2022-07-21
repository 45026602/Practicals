import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_hearder(dataframe):
    st.header('Header of Dataframe')
    st.write(df.head())

def plot(dataframe):
    st.header('Plot of Data')
    fig, ax = plt.subplots(1,1)
    ax.plot(df['DATE'], df['PD'])
    ax.set_xlabel('Date')
    ax.set_ylabel('PD')
    st.pyplot(fig)

def interactive_plot(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.multiselect('Select Y-Axis Value', options=df.columns, )

    plot = px.line(dataframe, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)
    
# Add a title and intro text
st.title('ABSA Data Exploration')
st.markdown('This is a web app to allow exploration of ABSA Data')

st.sidebar.title('Navigation')

# Create file uploader object
upload_file = st.sidebar.file_uploader('Upload data file')

options = st.sidebar.radio('Pages', options=['Home','Data Statistics', 'Header of Dataframe', 'Plot of Data','Interactive Plot'])

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)

    # Create a section for matplotlib figure


    

if options == 'Data Statistics':
    stats(df)
elif options =='Header of Dataframe':
    data_hearder(df)
elif options == 'Plot of Data':
    plot(df)
elif options == 'Interactive Plot':
    interactive_plot(df)