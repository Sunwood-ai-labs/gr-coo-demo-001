# app.py
import gradio as gr

def greet(name):
    return f"Hello AAAAAAAA {name}!"

# 重要：server_nameとserver_portを指定
demo = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # 外部からアクセス可能にする
        server_port=7860,       # ポート指定
        share=False             # 本番環境ではFalse
    )
