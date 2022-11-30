import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bf = pd.read_csv('./data/train.csv')

st.title('Ánalise de dados com o dataset Car-Insurance')
st.write('Fonte: https://www.kaggle.com/datasets/ifteshanajnin/carinsuranceclaimprediction-classification')

segment_a = bf.fuel_type.loc[bf.segment == "A"].value_counts()
segment_b1 = bf.fuel_type.loc[bf.segment == "B1"].value_counts()
segment_b2 = bf.fuel_type.loc[bf.segment == "B2"].value_counts()
segment_c1 = bf.fuel_type.loc[bf.segment == "C1"].value_counts()
segment_c2 = bf.fuel_type.loc[bf.segment == "C2"].value_counts()

x1 = segment_a.index
y1 = segment_a.values

x2 = segment_b1.index
y2 = segment_b1.values

x3 = segment_b2.index
y3 = segment_b2.values

x4 = segment_c1.index
y4 = segment_c1.values

x5 = segment_c2.index
y5 = segment_c2.values

plt.bar(x1,y1, label="Segmento A", width=0.4, align='edge')
plt.bar(x2,y2, label="Segmento B1", width=-0.4, align='edge')
plt.bar(x3,y3, label="Segmento B2", width=0.4, align='edge')
plt.bar(x4,y4, label="Segmento C1", width=-0.4, align='edge')
plt.bar(x5,y5, label="Segmento C2", width=0.4, align='edge')
plt.legend()
plt.title('Tipos de combustível por Segmento de carro')

st.pyplot(plt)

plt.clf()
#___________________________________________#


claim = bf.age_of_policyholder.loc[bf.is_claim == 1].value_counts()

x1 = claim.index
y1 = claim.values

plt.bar(x1,y1, width=0.4, align='edge')

plt.legend()
plt.title('Idades com grandes chances de reivindicar o seguro')

st.pyplot(plt)

plt.clf()

notClaim = bf.age_of_policyholder.loc[bf.is_claim == 0].value_counts()

x1 = notClaim.index
y1 = notClaim.values

plt.bar(x1,y1, width=-0.4, align='edge')

plt.legend()
plt.title('Idades com poucas chances de reivindicar o seguro')

st.pyplot(plt)

plt.clf()
#___________________________________________#
claimChance = bf.model.loc[bf.is_claim == 1].value_counts(normalize=True)

x = claimChance.values
plt.title('Dentre todos os carros que tem grande chance de solicitar seguro dentro dos próximos 6 meses, qual é o modelo mais provável?')
plt.pie(x, labels=["M6", "M1","M4","M8","M7","M9","M3","M5","M2","M10","M11"], autopct='%1.1f%%')

st.pyplot(plt)