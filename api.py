# import pandas as pd
# import requests
# import streamlit as st
#
#
# st.title('weather Analysis')


import streamlit as st
import json
import pandas as pd

# تنظیم API Key

# بارگذاری فایل JSON
uploaded_file = st.file_uploader("weather_dataset.json", type=["json"])
if uploaded_file:
    data = json.load(uploaded_file)
    st.write("دیتای شما:", data)

    # نمایش دیتا به صورت جدول
    df = pd.DataFrame(data)
    st.dataframe(df)