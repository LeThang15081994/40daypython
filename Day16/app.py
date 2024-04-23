#Sử dụng thư biện Streamlit xây dựng ứng dụng trên wed
from dequy import dequy_calculation
import streamlit as st

def app_cal():
    st.title("Tính toán đệ quy")
    num = st.number_input("Vui lòng nhập số vào ô:",0,1000)
    if st.button("Calculate"):
        result = dequy_calculation(num)
        st.write(f"Đệ quy của số {num} là {result}")

if __name__ == "__main__":
    app_cal()
