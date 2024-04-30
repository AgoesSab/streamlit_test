import streamlit as st
import pandas as pd
import numpy as np

st.header ('Indikator Perubahan Iklim')
df =  pd.DataFrame (np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


