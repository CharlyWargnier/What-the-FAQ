import os
import base64

import nltk
nltk.download('popular')

import pandas as pd
import streamlit as st
from pyinstrument import Profiler
from ansi2html import Ansi2HTMLConverter
import streamlit.components.v1 as components


import streamlit as st
from pipelines import pipeline
from requests_html import HTMLSession
session = HTMLSession()


profiler = Profiler()
profiler.start()

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


st.stop()

c13, c14 = st.beta_columns(2)

with c13:
    st.markdown('## **② Select your favourite Question/Answer pairs**')

with c14:
    st.markdown('###### ')
    st.markdown('###### ')
    st.markdown('######  &nbsp 👇 &nbsp Tick/untick these pink boxes to select/discard!')
#    st.markdown('###### (Tick or untick these pink boxes! on the right to select/discard #Question/Answer pairs')
    #st.text('Select your favourite Question/Answer pairs')

try:
  dict0 = faqs[0]
  dict_items0 = dict0.items()
  question0 =  list(dict0.values())[1]
  answer0 = list(dict0.values())[0]
except IndexError:
  pass

try:
  dict1 = faqs[1]
  dict_items1 = dict1.items()
  question1 =  list(dict1.values())[1]
  answer1 = list(dict1.values())[0]
except IndexError:
  pass

try:
  dict2 = faqs[2]
  dict_items2 = dict2.items()
  question2 =  list(dict2.values())[1]
  answer2 = list(dict2.values())[0]
except IndexError:
  pass

try:
  dict3 = faqs[3]
  dict_items3 = dict3.items()
  question3 =  list(dict3.values())[1]
  answer3 = list(dict3.values())[0]
except IndexError:
  pass

try:
  dict4 = faqs[4]
  dict_items4 = dict4.items()
  question4 =  list(dict4.values())[1]
  answer4 = list(dict4.values())[0]
except IndexError:
  pass

try:
  dict5 = faqs[5]
  dict_items5 = dict5.items()
  question5 =  list(dict5.values())[1]
  answer5 = list(dict5.values())[0]
except IndexError:
  pass

try:
  dict6 = faqs[6]
  dict_items6 = dict6.items()
  question6 =  list(dict6.values())[1]
  answer6 = list(dict6.values())[0]
except IndexError:
  pass

try:
  dict7 = faqs[7]
  dict_items7 = dict7.items()
  question7 =  list(dict7.values())[1]
  answer7 = list(dict7.values())[0]
except IndexError:
  pass

try:  
  dict8 = faqs[8]
  dict_items8 = dict8.items()
  question8 =  list(dict8.values())[1]
  answer8 = list(dict8.values())[0]
except IndexError:
  pass

try:
  dict9 = faqs[9]
  dict_items9 = dict9.items()
  question9 =  list(dict9.values())[1]
  answer9 = list(dict9.values())[0]
except IndexError:
  pass

try:
  dict10 = faqs[10]
  dict_items10 = dict10.items()
  question10 =  list(dict10.values())[1]
  answer10 = list(dict10.values())[0]
except IndexError:
  pass

#region column 0 ###################################################################################

c13, c14 = st.beta_columns(2)

with c13:
  try:    
    st.markdown('### **Questions**')
    st.markdown('')
    st.markdown('')
    st.write("3️⃣ - " + question0)   
  except NameError:
    pass

with c14:
  try:
    st.markdown('### **Answers**')
    st.markdown('')
    st.markdown('')
    answer0Box = st.checkbox(answer0, 'I agree', key=0)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 1 ###################################################################################



st.stop()

c15, c16 = st.beta_columns(2)

with c15:
  try:
    st.write("1️⃣ - " + question1)
  except NameError:
    pass
 
with c16:
  try:
    answer1Box = st.checkbox(answer1, 'I agree', key=1)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 2 ###################################################################################

c15, c16 = st.beta_columns(2)

with c15:
  try:
    st.write("2️⃣ - " + question2)
  except NameError:
    pass
 
with c16:
  try:
    answer2Box = st.checkbox(answer2, 'I agree', key=2)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 3 ###################################################################################

c17, c18 = st.beta_columns(2)

with c17:
  try:
    st.write("3️⃣ - " + question3)
  except NameError:
    pass

with c18:
  try:
    answer3Box = st.checkbox(answer3, 'I agree', key=3)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 4 ###################################################################################

c19, c20 = st.beta_columns(2)

with c19:
  try:
    st.write("4️⃣ - " + question4)
  except NameError:
    pass

with c20:
  try:
    answer4Box = st.checkbox(answer4, 'I agree', key=4)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 5 ###################################################################################

c21, c22 = st.beta_columns(2)

with c21:
  try:
    st.write("5️⃣ - " + question5)
  except NameError:
    pass

with c22:
  try:
    answer5Box = st.checkbox(answer5, 'I agree', key=5)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 6 ###################################################################################

c23, c24 = st.beta_columns(2)

with c23:
  try:
    st.write("6️⃣ - " + question6)
  except NameError:
    pass

with c24:
  try:
    answer6Box = st.checkbox(answer6, 'I agree', key=6)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 7 ###################################################################################

c25, c26 = st.beta_columns(2)

with c25:
  try:
    st.write("7️⃣ - " + question7)
  except NameError:
    pass

with c26:
  try:
    answer7Box = st.checkbox(answer7, 'I agree', key=7)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 8 ###################################################################################

c25, c26 = st.beta_columns(2)

with c25:
  try:
    st.write("8️⃣ - " + question8)
  except NameError:
    pass

with c26:
  try:
    answer8Box = st.checkbox(answer8, 'I agree', key=8)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 9 ###################################################################################

c25, c26 = st.beta_columns(2)

with c25:
  try:
    st.write("9️⃣ - " + question9)
  except NameError:
    pass

with c26:
  try:
    answer9Box = st.checkbox(answer9, 'I agree', key=9)
  except NameError:
    pass

#endregion  ###################################################################################

#region column 10 ###################################################################################

c25, c26 = st.beta_columns(2)

with c25:
  try:
    st.write("🔟 - " + question10)
  except NameError:
    pass

with c26:
  try:
    answer10Box = st.checkbox(answer10, 'I agree', key=10)
  except NameError:
    pass

#endregion  ###################################################################################


q =[]

try:
  if question0:
    q.append(question0)
  else:
    pass
except NameError:
  pass

try:
  if question1:
    q.append(question1)
  else:
    pass
except NameError:
  pass

try:
  if question2:
    q.append(question2)
  else:
    pass
except NameError:
  pass

try:
  if question3:
    q.append(question3)
  else:
    pass
except NameError:
  pass

try:
  if question4:
    q.append(question4)
  else:
    pass
except NameError:
  pass

try:
  if question5:
    q.append(question5)
  else:
    pass
except NameError:
  pass

try:
  if question6:
    q.append(question6)
  else:
    pass
except NameError:
  pass


try:
  if question7:
    q.append(question7)
  else:
    pass
except NameError:
  pass
          
try:
  if question8:
    q.append(question8)
  else:
    pass
except NameError:
  pass

try:
  if question9:
    q.append(question9)
  else:
    pass
except NameError:
  pass

try:
  if question10:
    q.append(question10)
  else:
    pass
except NameError:
  pass

a =[]

try:
  if answer0Box:
    a.append(answer0)
  else:
    pass
except NameError:
  pass

try:
  if answer1Box:
    a.append(answer1)
  else:
    pass
except NameError:
  pass


try:
  if answer2Box:
    a.append(answer2)
  else:
    pass
except NameError:
  pass

try:
  if answer3Box:
    a.append(answer3)
  else:
    pass
except NameError:
  pass

try:
  if answer4Box:
    a.append(answer4)
  else:
    pass
except NameError:
  pass

try:
  if answer5Box:
    a.append(answer5)
  else:
    pass
except NameError:
  pass

try:
  if answer6Box:
    a.append(answer6)
  else:
    pass
except NameError:
  pass

try:
  if answer7Box:
    a.append(answer7)
  else:
    pass
except NameError:
  pass

try:
  if answer8Box:
    a.append(answer8)
  else:
    pass
except NameError:
  pass

try:
  if answer9Box:
    a.append(answer9)
  else:
    pass
except NameError:
  pass

try:
  if answer10Box:
    a.append(answer10)
  else:
    pass
except NameError:
  pass


from pandas import DataFrame

dfQuestions = DataFrame (q,columns=['Questions'])
dfQuestions = dfQuestions.reset_index() 
#st.table(dfQuestions)

dfAnswers = DataFrame (a,columns=['Answers'])
dfAnswers = dfAnswers.reset_index() 
#st.table(dfAnswers)

dfBoth = dfQuestions.merge(dfAnswers, on = 'index')
dfBoth = dfBoth.drop(columns='index' )

st.markdown('## **③ Check your selection **')
st.table(dfBoth)

#######################################################

st.markdown('## **🎁 Download your selected Q/A pairs! **') ### https://docs.
st.header("")

csvLeft = dfBoth.to_csv()
b642 = base64.b64encode(csvLeft.encode()).decode()
href = f'<a href="data:file/csvLeft;base64,{b642}" download="SelectedFAQs.csv">** ⯈ Download your Q&As**</a>'
st.markdown(href, unsafe_allow_html=True)

profiler.stop()

values = st.slider('Select a range of values', 300, 1000)
#st.write('Values:', values)

profiler_output = profiler.output_text(unicode=True, color=True)
ansi_converter = Ansi2HTMLConverter()
html_output = ansi_converter.convert(profiler_output)
components.html(html_output, height=values, scrolling=True)

