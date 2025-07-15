# app.py
import gradio as gr
import random

def omikuji():
    """おみくじを引く関数"""
    fortunes = [
        "大吉 - 素晴らしい一日になるでしょう！",
        "中吉 - 良いことが起こりそうです",
        "小吉 - ちょっとした幸運があるかも",
        "吉 - 平穏な一日を過ごせそうです",
        "末吉 - 後半に良いことがありそう",
        "凶 - 注意深く行動しましょう",
        "大凶 - 今日は慎重に過ごしましょう"
    ]
    
    return random.choice(fortunes)

# おみくじアプリのインターフェース
demo = gr.Interface(
    fn=omikuji,
    inputs=None,  # 入力なし
    outputs=gr.Textbox(label="今日の運勢"),
    title="🎋 おみくじアプリ",
    description="ボタンを押しておみくじを引いてください！",
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # 外部からアクセス可能にする
        server_port=7860,       # ポート指定
        share=False             # 本番環境ではFalse
    )
