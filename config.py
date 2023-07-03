import os

#API ID & API Hash -----> my.telegram.org
api_id = 1111111
api_hash = 'ab140e34c15shdjs250a548984612f7'

#Bot Token -----> @BotFather
token = '6170271129:AAHfL7udSjkdhskdhasjdasdasldsd'

#Session Name -----> optional
session_name = 'FTP_Uploader'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [175701213]

# Chat id to send technical logs
dev = 175701213

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/Upload/'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = ''
ftp_username = ''
ftp_password = ''
ftp_domain = ''
