
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(layout="wide")
st.header("NORTH ACADEMY")

with st.sidebar:
 tabs = on_hover_tabs(tabName=['menu utama', 'kegiatan', 'laporan keuangan'],
                      iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='menu utama':
    st.title("SEJARAH SINGKAT")
    st.write('North merupakan komunitas pemuda yang berdiri tahun 2024'.format(tabs))
elif tabs == 'kegiatan':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))
elif tabs == 'laporan keuangan':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))

from st_social_media_links import SocialMediaIcons

social_media_links = [
  "https://www.facebook.com/ThisIsAnExampleLink",
  "https://www.youtube.com/ThisIsAnExampleLink",
  "https://www.instagram.com/https://www.instagram.com/fauziladhim1453?igsh=MTkxbjZ2bmM1ZWhhdw%3D%3D&utm_source=qr",
  "https://www.github.com/jlnetosci/st-social-media-links",
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()



