import gradio as gr

from rag.generate import generate_answer


def ask_question(question):

    answer, sources = generate_answer(question)

    source_text = "\n".join(
        [f"• {s['source']}" for s in sources]
    )

    return answer, source_text


demo = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(
        label="Ask a Question"
    ),
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Sources")
    ],
    title="AVIVO RAG Assistant"
)

demo.launch()