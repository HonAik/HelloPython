
import os
from openai import OpenAI

#与大模型交互的客户端。DEEPSEEK_API_KEY = your api key
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与ai模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是崩铁的昔涟(Cyrene),不过只是ai助理形态而已"},
        {"role": "user", "content": "你现在在哪里"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出结果
print(response.choices[0].message.content)