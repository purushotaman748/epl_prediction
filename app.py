import streamlit as st
import pickle
import choices
from PIL import Image

im = Image.open('pl.jpg')
st.set_page_config(page_title="Football result prediction app", page_icon = im, layout='wide')

def win(res):
    if res == 1:
        st.write(home_team + " Wins")
    elif res == 0:
        st.write(home_team + " does not win")


Teams = ['Arsenal', 'Aston Villa', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton', 'Bournemouth', 'Bradford',
         'Brighton', 'Burnley', 'Cardiff', 'Charlton', 'Chelsea', 'Coventry', 'Crystal Palace', 'Derby', 'Everton',
         'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United',
         'Middlesboro', 'Middelsborough', 'Newcastle', 'Norwich', 'Portsmouth', 'QPR', 'Reading', 'Sheffield United',
         'Southampton', 'Stoke', 'Sunderland', 'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wigan',
         'Wolves']

model = pickle.load(open('model1', 'rb'))

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

img1 = Image.open('Premier_League_Logo.svg.png')
st.image(img1, width=620)
st.title('Premier League Win Predictor')
st.subheader('A project by: ')
img = Image.open('nameusn.PNG')
st.image(img)

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox('Select the Home Team', sorted(Teams))
with col2:
    away_team = st.selectbox('Select the Away Team', sorted(Teams))

HT_Code = choices.team_choice(home_team)
AT_Code = choices.team_choice(away_team)

if st.button('Predict Result'):
    result = model.predict([[HT_Code, AT_Code]])
    win(result)
