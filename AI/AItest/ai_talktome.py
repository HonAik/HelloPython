import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

st.set_page_config(

    page_title ="Reynolds AI",
    page_icon ="🤖",
    
    # 布局
    layout="wide",
    
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#function session name
def session_name():
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S") #format of time
    return now
#function of save session information, good to use 
def save_session():
    #save current chat
        if st.session_state.currentsection:
            #create a new session object
            session_data = {
                "name": st.session_state.name,
                "character": st.session_state.character,
                "currentsection": st.session_state.currentsection,
                "messages": st.session_state.messages
            }

            #if session not exist
            if not os.path.exists("session"):
                os.mkdir("session")

            #save session
            with open(f"session/{st.session_state.currentsection}.json", "w",encoding="utf-8") as f:
                json.dump(session_data, f,ensure_ascii=False,indent=4)

#加载所有的列表会话信息
def load_sessions():
    sessionlist = [] 
    #load all session
    if os.path.exists("session"):
        for filename in os.listdir("session"):
            if filename.endswith(".json"):
                sessionlist.append(filename[:-5])
    sessionlist.sort(reverse=True)
    return sessionlist

#加载会话信息（选择的）
def load_session(session_name):
    
    try:
        if os.path.exists(f"session/{session_name}.json"):
            with open(f"session/{session_name}.json", "r",encoding="utf-8") as f:
                session_data = json.load(f)

            st.session_state.name = session_data["name"]
            st.session_state.character = session_data["character"]
            st.session_state.currentsection = session_name
            st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error(f"Error loading session: {e}")

#delete session
def delete_session(session_name):

    try:
        if os.path.exists(f"session/{session_name}.json"):
            os.remove(f"session/{session_name}.json")
            #if delete 要清空
            if session_name == st.session_state.currentsection: #if the session is the current session, clear the session
                st.session_state.messages = []
                st.session_state.currentsection = session_name()

    except Exception as e:
        st.error(f"Error loading session: {e}")

# Session State also supports attribute based syntax
if "messages" not in st.session_state:
    st.session_state.messages = []

#name
if "name" not in st.session_state:
    st.session_state.name = "Reynolds"

#character
if "character" not in st.session_state:
    st.session_state.character = "A helpful and friendly assistant"

#chat name
if "currentsection" not in st.session_state:
    st.session_state.currentsection = session_name()

#左侧的侧边栏.#没有用with
# st.sidebar.subheader("与Rey聊天")
# name = st.sidebar.text_input("Reynolds's AI name:")

# 侧边栏+ with 
with st.sidebar:

    #ai chat management
    st.subheader("AI chat management")

    # ai button
    if st.button("New chat",width = "stretch",icon="🙋‍♂️"):#stretch 宽度填满
        #save current chat
        save_session()

        #create a new chat
        if st.session_state.messages: #if there is a chat is empty, dont create a new one json file
            st.session_state.messages = []
            st.session_state.currentsection = session_name()
            save_session()
            st.rerun()
    
    #history chat:
    st.text("Chat's History")
    sessionlist = load_sessions()
    for session in sessionlist:
        col1,col2 = st.columns([4,1]) #宽度for每个column
        with col1:
            if st.button(session,width = "stretch",key = f"load_{session}",type="primary" if session == st.session_state.currentsection else "secondary"): #3元表达式：条件判断，如果session == st.session_state.currentsection，则返回True，否则返回False
                load_session(session)
                st.rerun()

        with col2:
            if st.button("",width = "stretch",icon="❌",key = f"delete_{session}"):
                delete_session(session)
                st.rerun()

    #divide
    st.divider(width = "stretch")

    # generate ai 
    st.subheader("Generate your Reynolds's AI")

    name = st.text_input("Reynolds's AI name:",placeholder = "Plese insert a name for RS AI",value = st.session_state.name)
    if name:
        st.session_state.name = name

    character = st.text_area("Reynolds's AI character:",placeholder = "Plese insert a description of character for RS AI",value = st.session_state.character)
    if character:
        st.session_state.character = character
    
#大标题
st.title("Talk to your Reynolds's AI")

# # #副标题,1级
# st.header("Let's start!!!!!!")

#写东西
st.write("Your question, my mission")

#logo
st.logo(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\whitecute9.png",size = "large")

#系统提示词
system_prompt = f"""
Your name is {st.session_state.name},
You character is {st.session_state.character}.
"""

#   聊天框
st.text(f"Chat: {st.session_state.currentsection}")
for message in st.session_state.messages:
    # st.chat_message("role").write(message["content"])
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# 客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#输入框
prompt = st.chat_input("Feel free to ask me anything!")

if prompt: #str automaticcaly become bool
    st.chat_message("user").write(prompt)
    print(">调用AI大模型,提示词:",prompt)
    #save user input
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用ai模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    #输出结果，非流式输出
    # print("<=AI结果", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #输出结果，流式输出
    response_message = st.empty()

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    #添加到会话
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    #保存会话信息
    save_session()