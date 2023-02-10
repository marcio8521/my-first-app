import streamlit as st

a = st.number_input('Insert the first number')
b = st.number_input('Insert the second number')

if st.button('Calcular'):
    c = a+b
    st.write("The sum result is, %f." % c)
else:
    st.write('Aguardando as informações')
