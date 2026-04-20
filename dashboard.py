import streamlit as st
import json

st.title("NinjaScanner Advanced Dashboard")

try:
    data = json.load(open("report.json"))

    for d in data:
        st.subheader(d["ip"])
        st.write("Ports:", d["ports"])
        st.write("Risk:", d["risk"])
        st.write("AI Analysis:", d["analysis"])
        st.markdown("---")

except:
    st.error("Run scan first")
