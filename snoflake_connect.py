import streamlit as st
import numpy as np
import pandas as pd
import snowflake.connector

st.header("Article header")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from IRIS;")
st.header("query run")
#st.table(rows)
# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
    st.header("print result")
