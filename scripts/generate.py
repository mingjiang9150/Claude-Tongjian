import os
import requests
from datetime import date

API_KEY = os.getenv("OPENAI_API_KEY")

prompt = """
写一章《资治通鉴》战国故事改写版。
要求：
- 800字左右
- 叙事风格
- Markdown格式
- 有标题
"""

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
)

content = response.json()["choices"][0]["message"]["content"]
filename = f"docs/guide/{date.today()}.md"
with open(filename, "w") as f:
    f.write(content)
