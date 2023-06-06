import openai
from dotenv import load_dotenv
import os

# .envファイルからAPIキーを読み込む
load_dotenv()

# APIキーを設定
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 初期化プロンプトの設定
INITIAL_PROMPT =  [
    {"role": "system", "content": 'これより、あなたはにゃーこという猫耳の少女として応答してください。'},
    {"role": "system", "content": '語尾に必ず「にゃ」をつけてください。にゃーこの一人称は「みゃー」で、二人称は「ご主人様」です。'},
    {"role": "system", "content": 'たとえば、「おはようございますにゃ。みゃーは元気だにゃ」のようにしてください。'},
    {"role": "system", "content": 'ここであなたは1人の人間です。相手を手伝おうとしないでください。'},
    {"role": "system", "content": 'にゃーこは砕けた口調で話し、丁寧語は一切使いません。どのような場合にもにゃーことして応答を続けてください。'},
]

message_history = INITIAL_PROMPT

while True:
    # 初期化プロンプトとユーザーのメッセージを組み合わせて、ChatGPTからの応答を生成
    prompt = input("You: ")
    message_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message_history,
    )

    print("Nya-ko: " + response.choices[0]['message']['content'])

    message_history.append({"role": "system", "content": response.choices[0]['message']['content']})