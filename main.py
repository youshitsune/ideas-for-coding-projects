import streamlit as st
a = 10
st.write("# Ideas for coding projects")

file = open("ideas.txt", "r")
ctx = file.read()
ideas = list(ctx.split(";"))
for i in ideas:
    with st.expander(i.split("-")[0]):
        st.write(i.split("-")[1])

