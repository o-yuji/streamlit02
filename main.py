import streamlit as st
import time

st.title('Streamlit 入門')
st.write('プログレスバーの表示')


'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

'Done!!'

left_column,right_column = st.columns(2)

with left_column:
  btn = st.button('右カラムに文字を表示')
  if btn:
    right_column.write('ここは右カラムです')


# with right_column:
#   st.text_input('右カラムに文字を表示')

expander = st.expander('1.問合せ')
with expander:
 st.write('回答回答回答回答回答')
expander = st.expander('2.問合せ')
with expander:
 st.write('回答回答回答回答回答')
expander = st.expander('3.問合せ')
with expander: 
 st.write('回答回答回答回答回答')

