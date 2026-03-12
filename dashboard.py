import streamlit as st
import pandas as pd
import numpy as np

# כותרת הדאשבורד
st.title("noga's Dashboard")

# יצירת נתונים מדומים
data = {
    "שם": ["דני", "רות", "מאיה", "משה", "אור"],
    "גיל": [28, 34, 23, 40, 31],
    "מחלקה": ["פיתוח", "שיווק", "פיתוח", "כספים", "פיתוח"],
    "ציון": np.random.randint(60, 100, 5)
}
df = pd.DataFrame(data)

# הצגת טבלה
st.subheader("נתונים כלליים")
st.dataframe(df)

# פילוח לפי מחלקה
st.subheader("פילוח מחלקות")
department_counts = df['מחלקה'].value_counts()
st.bar_chart(department_counts)

# ממוצע גיל
st.subheader("גיל ממוצע")
st.metric("גיל ממוצע לעובד", round(df['גיל'].mean(), 1))