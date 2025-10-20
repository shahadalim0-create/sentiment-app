import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# عنوان الصفحة
st.title("🪄 تحليل مشاعر التعليقات")

# تحميل البيانات
df = pd.read_excel("SaudiBERT_FinalResults_Cleaned.xlsx")

# عرض أول البيانات
st.write("نظرة عامة على البيانات:")
st.dataframe(df.head())

# حساب عدد كل نوع من المشاعر
sentiment_counts = df["التصنيف_النهائي"].value_counts()

# عرض مخطط بياني
st.write("### توزيع المشاعر")
fig, ax = plt.subplots()
sentiment_counts.plot(kind="bar", color=["#66bb6a", "#ef5350", "#ffa726"], ax=ax)
plt.xlabel("نوع المشاعر")
plt.ylabel("عدد التعليقات")
plt.title("توزيع المشاعر الإيجابية والسلبية والمحايدة")
st.pyplot(fig)

# خاصية البحث
st.write("### 🔍 البحث في التعليقات")
keyword = st.text_input("أدخل كلمة للبحث:")
if keyword:
    filtered = df[df["التعليق"].str.contains(keyword, case=False, na=False)]
    st.dataframe(filtered)
