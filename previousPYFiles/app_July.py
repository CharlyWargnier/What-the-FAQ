import streamlit as st
import pandas as pd
from annotated_text import annotated_text


# To interate through results
from collections import Counter
from pipelines import pipeline
import nltk

nltk.download("popular")

# For Download button (Johannes)
from functionforDownloadButtons import download_button

from requests_html import HTMLSession

session = HTMLSession()


st.set_page_config(page_title="WhatTheFAQ?", page_icon="❓")


def _max_width_():
    max_width_str = f"max-width: 1700px;"
    # max_width_str = f"max-width: 1550px;"
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

# endregion Layout size ####################################################################################

# region Top area ############################################################

c30, c31, c32, c33 = st.beta_columns(4)

with c30:
    st.image("WhatTheFaq.png", width=520)

st.header("")

with c33:
    st.header("")
    st.header("")
    st.subheader("")
    st.markdown(
        "###### Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://twitter.com/DataChaz) &nbsp [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)"
    )

# with st.beta_expander("ℹ️ - To-do ", expanded=False):
#    st.write(
#        """
#
# -   Do more tests
#
# 	    """
#    )
#
# with st.beta_expander("ℹ️ - Done ", expanded=False):
#    st.write(
#        """
#
# -   Change streamlit logo + add title
# -   Change column order in dataframe
# -   Fix - Invalid URL! Please ensure you blah, blah
# -   Add button from Johannes
# -   Un-hash set_page_config to display favicon
# -   Ensure 'Made in Streamlit is realigned
#
# 	    """
#    )

with st.beta_expander("ℹ️ - About this app ", expanded=False):
    st.write(
        """
	    
-   WTFaq? leverages the power of [Google T5 Transformer](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) to generate quality question/answer pairs from content fetched from URLs!
-   Here’s a [good explanation] (https://github.com/patil-suraj/question_generation#multitask-qa-qg) of how Google's T5-Based model generates these FAQs
-   This app is still in Beta. Feedback & bug spotting are welcome! DM me on [Twitter](https://twitter.com/DataChaz) :)
-   This app is also free. If it's useful to you, you can [buy me a coffee](https://www.buymeacoffee.com/cwar05) to support my work! 😊🙏


	    """
    )

    st.header("")

st.markdown(
    "## **① Input a URL **",
)  #########

c3, c4, c5 = st.beta_columns([1, 6, 1])

with c4:

    with st.form("Form1"):

        URLBox = st.text_input("", help="e.g. 'https://www.google.com/'")
        cap = 2000

        submitted1 = st.form_submit_button("Get your Q&A pairs! ✨")

    c = st.beta_container()

    if not submitted1 and not URLBox:
        # st.warning("Please add a valid URL ☝️")
        st.stop()

    if submitted1 and not URLBox:
        st.warning("☝️ Please add a URL")
        st.stop()

selector = "p"

try:
    with session.get(URLBox) as r:
        paragraph = r.html.find(selector, first=False)
        text = " ".join([p.text for p in paragraph])

except:
    c.error(
        "🚫 The URL seems invalid. Please ensure you've added 'https://' or 'http://' at the start of the URL!"
    )
    st.stop()


# text2 = (text[:2000] + "..") if len(text) > 2000 else text
# lenText = len(text2)

text2 = (text[:cap] + "..") if len(text) > cap else text
lenText = len(text2)

if lenText > cap:
    # st.warning('⚠️ The extracted text is ' + str(len(text)) + " characters, that's " + str(len(text)- 30000) + " #characters above the 30K limit! Stay tuned as we may increase that limit soon! 😉")
    c.warning(
        "⚠️ As we're still in early BETA, we will build the Q&A pairs based on the first 2,000 characters. Stay tuned as we may increase that limit soon! 😉"
    )
    pass
    # st.stop()
else:
    pass

# ↕️ Toggle activation details

with st.beta_expander(" ↕️ Toggle to check extracted text ", expanded=False):
    st.header("")

    # if lenText > 2000:
    a = "The full text extraction is " + str(len(text)) + " characters long"
    # else:
    #    a = "The extracted text is " + str(len(text)) + " characters long. As we're still in BETA, we will build the Q&A pairs based on the first 2,000 characters"

    st.header("")
    st.write(text2)
    st.header("")
    annotated_text(
        (a, "", "#8ef"),
    )

nlp = pipeline("multitask-qa-qg")
faqs = nlp(text2)

st.markdown("## **② Select your favourite Q&A pairs **")
st.header("")


from collections import Counter

k = [x["answer"] for x in faqs]

new_faqs = []

for i in Counter(k):
    all = [x for x in faqs if x["answer"] == i]
    new_faqs.append(max(all, key=lambda x: x["answer"]))

# new_faqs

c19, c20 = st.beta_columns([3, 1.8])

a_list = []

with c19:
    # c1, c2 = st.beta_columns(columns or [1, 4])
    filtered_Qs = [item for item in new_faqs if st.checkbox(item["question"], key=100)]
    # st.markdown("######")

with c20:
    # c1, c2 = st.beta_columns(columns or [1, 4])
    filtered_As = [
        itemw for itemw in new_faqs if st.checkbox(itemw["answer"], key=1000)
    ]
    # st.markdown("######")


df = pd.DataFrame(filtered_Qs)
df2 = pd.DataFrame(filtered_As)

# cols
# Out[13]: ['mean', 0L, 1L, 2L, 3L, 4L]

frames = [df, df2]
result = pd.concat(frames)
# result = result.drop_duplicates(subset=["question", "answer"])
result = result.drop_duplicates(subset=["question", "answer"])
# cols = ["question", "answer"]
# result.columns


# df = df[["C", "A", "B"]]
# result = result[cols]

# df = df[["C", "A", "B"]]


# result = result["question", "answer"]
result.index += 1

st.header("")

st.markdown("## **③ Download your selected Q&A pairs! **")  ### https://docs.
st.header("")


if result.empty:
    b = "To download your Q&A's you need to start selecting them! ☝️"
    annotated_text(
        (b, "", "#faa"),
    )

else:
    result = result[["question", "answer"]]
    CSVButton2 = download_button(result, "Downloaded_Q&As.csv", "🎁 Download your Q&As")
    st.table(result)
