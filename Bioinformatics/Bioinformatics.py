import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

img = Image.open('pic.png')
st.image(img,use_container_width=True)

st.header("Dna nucleotide count web app")
st.write("""
This app counts the nucleotide composition of query dna!
***

""")
st.markdown ("### Enter Dna Sequence:")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=150)
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)
st.write("""***""")

st.header('Input (Data query)')
sequence

st.header('Output (DNA nucleotide count)')
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
    return d
X=DNA_nucleotide_count(sequence)
X
st.subheader('2. Print text')
df =pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
plt.hist(X,5)
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)