import sqlite3

import streamlit as szar

import time 

placeholder = szar.empty()

placeholder.text("Hello")
    

#con = sqlite3.connect(':memory:')
con = sqlite3.connect('titkos78.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS titkos_adatok
    (nev        TEXT,
    jelszo       TEXT,
    e_mail       TEXT)
    """)


con.commit()

amig = False
with placeholder.container():
    opcio = szar.radio(
        "Van már fiókod :thinking_face:?",
        [":rainbow[Van]", "***Nincs***"],
        index=None,
    )

    if opcio == ':rainbow[Van]':
        szar.title('Bejelentkezés')
        be_nev = szar.text_input('Név', placeholder="kattints ide...", type="default")
        be_jel = szar.text_input('jelszó', placeholder="kattints ide...", type="password")
        kereso = cur.execute(" SELECT * FROM titkos_adatok WHERE nev =? AND jelszo =?",(be_nev, be_jel))
        lista1 = []
        for sor in kereso:
            lista1.append(sor)
        if szar.button('Bejelentkezés',type="secondary"):
            amig = True
            if len(lista1) > 0:
                szar.title(f'{be_nev} sikeresen :blue[bejelentkezet] :sunglasses:!')
                szar.balloons()

            else:
                szar.title(f'Ilyen felhasználó: "_{be_nev}_" :red[NEM] létezik!')

    elif opcio == '***Nincs***':
        szar.title("Regisztráció")
        reg_nev = szar.text_input('Név', placeholder="kattints ide...", type="default")
        reg_jel = szar.text_input('jelszó', placeholder="kattints ide...", type="password")
        reg_ema = szar.text_input('e-mail', placeholder="kattints ide...", type="default")
        kereso2 = cur.execute(" SELECT * FROM titkos_adatok WHERE nev =? OR e_mail =?",(reg_nev, reg_ema))
        lista2 = []
        for sor in kereso2:
            lista2.append(sor)

        if szar.button('Regisztrálás',type="primary"):
            if len(reg_nev) > 6 or len(reg_jel) > 6:
                if len(reg_ema) > 0:
                    if len(lista2) > 0:
                        szar.error(f'Figyelem ez a név: "_{lista2[0][0]}_" vagy ez az emali: "_{lista2[0][2]}_" már használatban van!', icon="🚨")
                    else:
                        cur.execute("INSERT INTO titkos_adatok VALUES (?,?,?) ", ( reg_nev, reg_jel, reg_ema))
                        con.commit()
                        szar.success(f'"_{reg_nev}_" felhasználó sikeresen regisztrálva!', icon="✅")

                else:
                    szar.error("Az e-mail eléggé rövid let! :thinking_face:", icon="🚨")
            else:
                szar.error("A  felhasználónak és a jelszónak minimum 6 karakterből kell állnia!", icon="🚨")
                    


                


if amig:
    szar.balloons()
    placeholder.empty()
    with szar.empty():
            for seconds in range(2):
                szar.title(f'{be_nev} sikeresen :blue[bejelentkezet] :sunglasses:!!!!')
                time.sleep(2)

if amig:
    import yfinance as yf
    import streamlit as st

    st.write("""
    # Adattudományi alkalmazás Python (***Pithon***) és Streamlit segítségével

    ## E fennkölt, teátrális alkalmazás megmutatja a ***:red[FÉLELMETES]*** :rainbow[Microsoft] cég részvény árainak grafikonját 2010-től 2020-ig!! :sunglasses:

    """)
    st.success(f'Az Adatfeldolgozás sikeres!', icon="✅")
    st.balloons()

    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    tickerSymbol = 'MSFT'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("""
    ## Árfolyam
    """)
    st.line_chart(tickerDf.Close)
    st.write("""
    ## Mennyiség
    """)
    st.line_chart(tickerDf.Volume)
    st.write("""
    ## Árfolyam
    """)
    st.line_chart(tickerDf.Open)
    st.write("""
    ## Árfolyam
    """)
    st.line_chart(tickerDf.Dividends)
          
