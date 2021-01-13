#import os
import base64
import nltk
nltk.download('popular')

import pandas as pd
import streamlit as st

from pipelines import pipeline
from requests_html import HTMLSession
session = HTMLSession()

st.beta_set_page_config(
#page_title="Ex-stream-ly Cool App",
page_icon="😊")


#region Layout size ####################################################################################

def _max_width_():
    max_width_str = f"max-width: 1300;"
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
      
st.markdown('## **① Paste a URL**') #########

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

#text
#st.write(type(text))

text2 = (text[:3000] + '..') if len(text) > 3000 else text
text2
lenText2 = len(text2)
lenText2

#st.stop()

#if lenText > 30000:
#  st.warning('⚠️ The extracted text is ' + str(len(text)) + " characters, that's " + str(len(text)- 30000) + " #characters above the 30K limit! Stay tuned as we may increase that limit soon! 😉")
#  st.stop()
#else:


with st.beta_expander("Toggle to check extracted text ⯈", expanded=False):
    st.warning("Extracted text is " + str(len(text)) + " characters long")
    st.write(text)


####################################

nlp = pipeline("multitask-qa-qg")
faqs = nlp(text)

####################################
#faqs

from collections import Counter

k = [x['answer'] for x in faqs]

new_faqs=[]

for i in Counter(k):
    all = [x for x in faqs if x['answer']==i]
    new_faqs.append(max(all, key=lambda x: x['answer']))

#new_faqs

c19, c20 = st.beta_columns([3, 1])

a_list = []

with c19:
    #c1, c2 = st.beta_columns(columns or [1, 4])
    filtered_Qs = [item for item in new_faqs if st.checkbox(item["question"], key = 100)]
    #st.markdown("######")

with c20:
    #c1, c2 = st.beta_columns(columns or [1, 4])
    filtered_As = [itemw for itemw in new_faqs if st.checkbox(itemw["answer"], key = 1000)]
    #st.markdown("######")

#filtered_Qs
#filtered_As

#with c22:
#    for d in faqs:
#        a = st.checkbox(d['answer'])
#        #st.text("")
#        #st.markdown("######")
#        if a == True:
#            a_list.append(['answer'], key = 2) 
#
#with c22:
#    for d in faqs:
#        st.write(d['answer'])
#        #st.markdown("######")

df = pd.DataFrame(filtered_Qs) 
#df

df2 = pd.DataFrame(filtered_As) 
#df2

###################

import streamlit as st
import pandas as pd


#st.header('FAQs')
#
#faqs = [
#{ "question": "How old is Tom?", "answer": "10 year old" },
#{ "question": "How old is Mark?", "answer": "5 year old" },
#{ "question": "How old is Pam?", "answer": "7 year old" },
#{ "question": "How old is Dick?", "answer": "12 year old" }
#]
#
#faqs
#
#c19, c20 = st.beta_columns(2)
#
#a_list = []
#
#with c19:
#    filtered_faqs = [item for item in faqs if st.checkbox(item["question"], key = 1)]
#
#with c20:
#    for d in faqs:
#       st.write(d['answer'])
#
#df = pd.DataFrame(filtered_faqs) 
#df

frames = [df, df2]
result = pd.concat(frames)
result = result.drop_duplicates(subset=['answer', 'question'])


#st.stop()

###################

st.markdown('## **③ Check your selection **')
st.table(result)

#######################################################

st.markdown('## **🎁 Download your selected Q/A pairs! **') ### https://docs.
st.header("")

csvLeft = result.to_csv()
b642 = base64.b64encode(csvLeft.encode()).decode()
href = f'<a href="data:file/csvLeft;base64,{b642}" download="SelectedFAQs.csv">** ⯈ Download your Q&As**</a>'
st.markdown(href, unsafe_allow_html=True)



