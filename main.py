import streamlit as st
import api_bank as api
import datetime as dt
import calculator as ca


now = dt.datetime.now()
st.title("Giá tiền USD")
st.write("Xin chào đã đến, mình xin giới thiệu về app")
st.write("mình xem giá thị trường tiền USD né !!!")
rate_USD = api.get_usd_rate()
rate_USE_clear = rate_USD.replace(",", "")
rate_USE_float = float(rate_USE_clear)


st.write(now.strftime("%d-%m-%Y %H:%M:%S"))
st.write("giá USD : ", f"{rate_USE_float:,.2f}")
usd_6 = rate_USE_float * 1.06
st.write("giá USD x 6% : ", f"{usd_6:,.2f}")

number_VN = st.number_input("Nhập số VND bạn muốn : ", min_value = 1, step = 1)
if st.button("kết quả"):
    st.success(f"{ca.amount_USD(number_VN):,.0f}")