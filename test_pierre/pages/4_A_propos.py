#===============================================================================

import streamlit as st

# html_title = "<h1 style='color:#FF036A'>À propos</h1>"
html_title = "<h2 style='color:#FF036A'>Une application proposée par la Chifouteam</h2>"
st.markdown(html_title, unsafe_allow_html=True)

html_text = """
<div style='color:#44B7E3;font-size:30px'>
Une application proposée par la Chifouteam :
<ul>
<li style='color:#44B7E3;font-size:30px'>
Claire
</li>
<li style='color:#44B7E3;font-size:30px'>
David
</li>
<li style='color:#44B7E3;font-size:30px'>
Pierre
</li>
<li style='color:#44B7E3;font-size:30px'>
Stéphanie
</li>
</ul>
</div>
"""

#st.markdown(html_text, unsafe_allow_html=True)

html_code = """
<meta charset="UTF-8">
<div style="zoom: 20%; text-align: center">
<img src="https://www.bejian.fr/images/the_team.png" usemap="#image-map">
<map name="image-map">
    <area target="_blank" alt="Sheldon" title="Sheldon" href="https://the-big-bang-theory.com" coords="958,2171,541" shape="circle">
    <area target="_blank" alt="Claire" title="Claire" href="https://www.linkedin.com/in/claire-lemaitre-a1322014b/" coords="2182,2178,529" shape="circle">
    <area target="_blank" alt="Pierre" title="Pierre" href="https://www.linkedin.com/in/pbejian/" coords="2587,1131,515" shape="circle">
    <area target="_blank" alt="Stéphanie" title="Stéphanie" href="https://www.linkedin.com/in/stephanie-gentil/" coords="1549,550,516" shape="circle">
    <area target="_blank" alt="David" title="David" href="https://www.linkedin.com/in/david-rengifo-a5a4b5b5/" coords="538,1129,516" shape="circle">
</map>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
