# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sqlite3

import streamlit as szar

#con = sqlite3.connect(':memory:')
con = sqlite3.connect('titkos69.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS titkos_adatok
    (nev        TEXT,
    jelszo       TEXT,
    e_mail       TEXT)
    """)


con.commit()

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
        if len(lista2) > 0:
            szar.error(f'Figyelem ez a név: "_{lista2[0][0]}_" vagy ez az emali: "_{lista2[0][2]}_" már használatban van!', icon="🚨")
        else:
            cur.execute("INSERT INTO titkos_adatok VALUES (?,?,?) ", ( reg_nev, reg_jel, reg_ema))
            con.commit()
            szar.success(f'"_{reg_nev}_" felhasználó sikeresen regisztrálva!', icon="✅")


            #for row in cur.execute("SELECT nev, jelszo, e_mail FROM titkos_adatok"):
                #szar.write(row)


szar.link_button("Go to galffffffffflery", "cuccmokos.py")

szar.write("sfsdfsdfs")


