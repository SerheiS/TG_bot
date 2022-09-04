# One more telegram bot...

# Description:

This small 'script' that launches telegram bot. This bot can get an image and recognize the text on it.

# How to use:

1. Press start
2. Send image
3. Bot will reply to you with result (will send text from the img)

# How to run

1. This script uses 'pytesseract' for text recognition. You have to find on the Internet how to install it on you machine's OS, cause there is difference.

2. Create your own telegram bot with @BotFather and get the token

3. Paste the token of your bot to the ```main.py``` file

4. create virtual environment

5. Install all necessary libraries ```pip install -r pass/to/requirements.txt```

6. Run ```python main.py```:
 - in terminal you'll see logs of your bot
 - in Telegramm find your bot with @botname and start it

# If you forget smth:

 - @BotFather - official TG bot, that helps you to create/control/set/delete/see_info_about any of your TG bot

 - this script uses --pyTelegramBotAPI-- for bot code and --pytesseract-- for image recognition
 
 - quality of the img influences much on the quality of text recognition!

