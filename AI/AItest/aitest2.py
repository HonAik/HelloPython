import streamlit as st

#大标题
st.title("streamlit beginner")

#副标题,1级
st.header("Just a beginner, what do u expect?")

#副标题,2级
st.subheader("Let's start!!!!!!")

#写段落,一段落的形式print
st.write("My name is Reynolds, glad to see you guys! Now I am typing something bullshit inside bibobibobibobibo")

#图片
st.image(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\whitecute9.png")

#logo
st.logo(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\bili1.png")

#table
students ={
    "名" : ["Dorcas","Ray","Reynolds","Nelson"],
    "sex" : ["女","男","男","男"],
    "birth":["0802","0809","0814","0000"]
}
st.table(students)

#input
name = st.text_input("Insert your name")
st.write(f"Your name is {name}")

password1 = st.text_input("Insert you password", type = "password")
st.write(f"Your password is {password1}")

#button
gender = st.radio("你的性别是：",["男","女","未知"])
st.write(f"Your gender is {gender}")
# genre = st.radio(
#     "What's your favorite movie genre",
#     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
#     captions=[
#         "Laugh out loud.",
#         "Get the popcorn.",
#         "Never stop learning.",
#     ],
# )