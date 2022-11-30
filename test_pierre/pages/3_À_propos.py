#===============================================================================

import streamlit as st

html_title = "<h2 style='color:red'>À propos</h2>"
st.markdown(html_title, unsafe_allow_html=True)

html_text = """
<div style='color:blue'>
Une application proposée par la Chifouteam :
<ul>
<li>
Claire
</li>
<li>
David
</li>
<li>
Pierre
</li>
<li>
Stéphanie
</li>
</ul>
</div>
"""

st.markdown(html_text, unsafe_allow_html=True)

#st.markdown("""
#- Claire
#- David
#- Pierre
#- Stéphanie
#
#""")
