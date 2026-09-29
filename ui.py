import streamlit as st    
from youtube_analyzer import build_youtube_agent 

st.set_page_config(
    page_title="Youtube video Analyzer",
    layout="centered"
)

st.title("📽️AI Youtube Video Analayzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent() 


agent = get_agent() 

#input box
video_url=st.text_input("Enter youtube video Link") #str
button=st.button("Analyze Video") #True/False 

if video_url and button:
    with st.spinner("Analyzing Video...."):
       response=agent.run(
        f"Analyze this video: {video_url}"
       )

    st.markdown("Analysis report of the video: ")
    st.markdown(response.content)