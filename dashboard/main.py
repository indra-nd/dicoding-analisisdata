import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write(
    """
    # Analisis Dashboard
    ## Banyaknya yang :blue[meminjam] sepeda ketika weekday
    """
)

with st.sidebar:
    
    st.write(
    """
    # Indra Risqiawan

    # Submission :blue[Dicoding] Analisis Data
    ## 1. Berapa banyaknya yang meminjam sepeda ketika weekday?
    ##  2. Berapa banyaknya sepeda yang dipinjam selama 5 jam ketika weekday?


    """
)

#menginput data
df = pd.read_csv("dashboard/hour.csv")

weekday = df['weekday'].sum()
weekday
workingday = df['workingday'].sum()
holiday = df['holiday'].sum()
day =('Holiday', 'Weekday', 'Workingday')
peminjam = (holiday, weekday, workingday)

fig = plt.figure()
cl = ['gray','blue','gray']
plt.title('Peminjam Sepeda ketika Holiday, Weekday, dan Workingday\n')
plt.ylabel('Banyak Sepeda')
plt.bar(x=day,height=peminjam,color=cl)

st.pyplot(fig)

st.write(
    """
    ## Banyaknya :blue[sepeda] yang dipinjam selama 5 jam ketika weekday
    """
)

hour_one = df[df['hr'] == 1]['weekday'].sum()

hour_two = df[df['hr'] == 2]['weekday'].sum()

hour_three = df[df['hr'] == 3]['weekday'].sum()

hour_four = df[df['hr'] == 4]['weekday'].sum()

#banyaknya sepeda yang dipinjam selama 5 jam ketika weekday
hour_five = df[df['hr'] == 5]['weekday'].sum()
hour_five

hour_six = df[df['hr'] == 6]['weekday'].sum()

hour_seven = df[df['hr'] == 7]['weekday'].sum()

hour_eight = df[df['hr'] == 8]['weekday'].sum()

hour_nine = df[df['hr'] == 9]['weekday'].sum()

hour_ten = df[df['hr'] == 10]['weekday'].sum()

hour= ('1','2','3','4','5','6','7','8','9','10')
banyak = (hour_one,hour_two,hour_three,hour_four,hour_five,hour_six,hour_seven,hour_eight,hour_nine,hour_ten)

figg = plt.figure()
clr = ['gray','gray','gray','gray','blue','gray','gray','gray','gray','gray' ]
plt.title('Banyaknya Sepeda yang dipinjam mulai 1 jam sampai 10 jam\n')
plt.xlabel('Jam')
plt.ylabel('Banyak Sepeda')
plt.bar(x=hour, height=banyak,color=clr)

st.pyplot(figg)
