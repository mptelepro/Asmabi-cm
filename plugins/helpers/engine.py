import openai
from info import OPENAI
async def ai(query):
    
    openai.api_key = OPENAI #Your openai api key
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"user: {message.from_user.mention} \n{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
    else:
        await message.reply_text(😥 Sᴏʀʀʏ {message.from_user.mention}, \nYᴏᴜ Cᴀɴ'ᴛ Aꜱᴋ Qᴜᴇꜱᴛɪᴏɴꜱ Hᴇʀᴇ !!!\n/openai Cᴏᴍᴍᴀɴᴅ Oɴʟʏ Wᴏʀᴋ Oɴ Mʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ♨️
