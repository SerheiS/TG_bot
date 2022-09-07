from PIL import Image
import pytesseract
import telebot
import time
import re

TOKEN = "YOUR TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def all_command(message):
    bot.send_message(message.chat.id, text="Hello!")

    time.sleep(1)
    bot.send_message(message.chat.id, 
                    text="I'm able to recognize text from img. It works not perfect 😁")
    
    time.sleep(1)
    bot.send_message(message.chat.id, 
                    text="To get text send me some image (not file!) as a photo.")

    time.sleep(2)
    bot.send_message(
        message.chat.id, 
        text="ADVISE: to get high-quality recognition, send me images with good quality and plain background!")


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    bot.send_message(message.chat.id, text="Working on it...")
    """
    There are 3 elements in 'message.photo' array. 
    The last one holds data with the highest file resolution, what is 
    very important for really goog img to text recognition (is corresponds to tessaract)
    that's why we use the last element (photo[-1]) of this array
    """
    fileID = message.photo[-1].file_id

    # bot.get_file method prepares file for downlonding under the hood
    file_info = bot.get_file(fileID)

    downloaded_file = bot.download_file(file_info.file_path)
    img_name = "saved_img.jpg"
    with open(img_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    img_data = img_to_txt(img_name)
    if re.search("^\s", img_data):
        bot.send_message(
            message.chat.id, 
            text="I can't find any text here, sorry 😞\n\n" + 
            "ADVISE: try to send img with higher quality and plain background 🙃"
            )
    else:
        bot.send_message(message.chat.id, text=img_data) 


@bot.message_handler(content_types=['document'])
def photo_id(message):
    bot.send_message(message.chat.id, text="You've sent a file/document 😵‍💫")
    time.sleep(1)
    
    bot.send_message(message.chat.id, text="Please, send me a photo 🙃\n" +
    "(use '☑️ send compressed' if proposed)")


@bot.message_handler(func=lambda message: True)


def chating(message):
    bot.send_message(message.chat.id, text="Sorry, I'm not able to chat 😞")


# Transform img to string
def img_to_txt(img):
    data = pytesseract.image_to_string(Image.open(img))
    return data


bot.infinity_polling()
