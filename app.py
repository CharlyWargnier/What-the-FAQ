import os
import base64

import nltk
nltk.download('punkt')

import pandas as pd
import streamlit as st
#from pyinstrument import Profiler
#from ansi2html import Ansi2HTMLConverter
import streamlit.components.v1 as components


import streamlit as st
from pipelines import pipeline
from requests_html import HTMLSession
session = HTMLSession()


#profiler = Profiler()
#profiler.start()


####################################################################################

# ... your code ...


st.beta_set_page_config(
page_title="Ex-stream-ly Cool App",
page_icon="🧊")


#region Layout size ####################################################################################

def _max_width_():
    max_width_str = f"max-width: 1300px;"
    #max_width_str = f"max-width: 1550px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

#endregion Layout size ####################################################################################

#region Top area ############################################################

c30, c31, c32 = st.beta_columns(3)

with c30:
  st.image('WhatTheFaq.png', width = 420 )


with c32:
  #st.image('streamEASmaller2.jpg', width = 275 )
  #st.markdown("---")
  st.header('')
  st.header('')
  st.markdown('###### Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://twitter.com/DataChaz) &nbsp [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)')

#endregion End ####################################################################################

# #endregion Top area ############################################################

#region About the app ############################################################

with st.beta_expander("ℹ️ - About this app ", expanded=False):
  st.write("""
	    
-   WTFaq? leverages the power of [Google T5 Transformer](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) to generate quality question/answer pairs from content fetched from URLs!
-   Here’s a [good explanation] (https://github.com/patil-suraj/question_generation#multitask-qa-qg) of how Google's T5-Based model generates these FAQs
-   This app is still in Beta. Feedback & bug spotting are welcome! DM me on [Twitter](https://twitter.com/DataChaz) :)
-   This app is also free. If it's useful to you, you can [buy me a coffee](https://www.buymeacoffee.com/cwar05) to support my work! 😊🙏

	    """)
      
st.markdown('## **① Paste a URL **') #########

URLBox = st.text_input('')

if not URLBox:
  st.warning('Please add a valid URL ☝️')
  st.stop()

selector = "p"

try:
  with session.get(URLBox) as r:
    paragraph = r.html.find(selector, first=False)
    text = " ".join([ p.text for p in paragraph])
except:
  st.error('🚫 Invalid URL!')
  st.stop()

lenText = len(text)

if lenText > 30000:
  st.warning('⚠️ The extracted text is ' + str(len(text)) + " characters, that's " + str(len(text)- 30000) + " characters above the 30K limit! Stay tuned as we may increase that limit soon! 😉")
  st.stop()
  
else:
  with st.beta_expander("Toggle to check extracted text ⯈", expanded=False):
    st.warning("Extracted text is " + str(len(text)) + " characters long")
    st.write(text)


####################################

nlp = pipeline("multitask-qa-qg")
faqs = nlp(text)

####################################
faqs

c19, c20 = st.beta_columns(2)

a_list = []

with c19:
    filtered_faqs = [item for item in faqs if st.checkbox(item["question"], key = 1)]

with c20:
    for d in faqs:
       st.write(d['answer'])

df = pd.DataFrame(filtered_faqs) 
df

###################

import streamlit as st
import pandas as pd


st.header('FAQs')

faqs = [
{ "question": "How old is Tom?", "answer": "10 year old" },
{ "question": "How old is Mark?", "answer": "5 year old" },
{ "question": "How old is Pam?", "answer": "7 year old" },
{ "question": "How old is Dick?", "answer": "12 year old" }
]

faqs

c19, c20 = st.beta_columns(2)

a_list = []

with c19:
    filtered_faqs = [item for item in faqs if st.checkbox(item["question"], key = 1)]

with c20:
    for d in faqs:
       st.write(d['answer'])

df = pd.DataFrame(filtered_faqs) 
df

st.stop()