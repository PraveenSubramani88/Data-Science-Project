import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from rag.generate import generate_answer

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

user_history = {}

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/ask <question>\n/help"
    )


async def ask_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = " ".join(context.args)

    if not question:
        await update.message.reply_text(
            "Usage: /ask <question>"
        )
        return

    user_id = update.effective_user.id

    if user_id not in user_history:
        user_history[user_id] = []

    answer, retrieved_docs = generate_answer(question)

    # Store interaction
    user_history[user_id].append(
        {
            "question": question,
            "answer": answer
        }
    )

    # Keep only last 3
    user_history[user_id] = user_history[user_id][-3:]

    # DEBUG MEMORY
    print("\n=== USER HISTORY ===")

    for item in user_history[user_id]:
        print(item)

    print("====================\n")

    # Build response
    response = f"📌 Answer\n{answer}\n\n"

    response += "📚 Sources\n"

    sources = list(
        set(
            [doc["source"] for doc in retrieved_docs]
        )
    )

    for source in sources:
        response += f"• {source}\n"

    await update.message.reply_text(response)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ask", ask_command))

print("Bot running...")

app.run_polling()