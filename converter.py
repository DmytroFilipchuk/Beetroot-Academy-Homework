# з модулю converter.py


def converter_voice_msg(audio):
    import subprocess

    CurrentFileName = audio
    FinalFileName = 'here_you_go' + '.mp3'

    try:
        subprocess.call(['ffmpeg', '-i', f'{CurrentFileName}', f'{FinalFileName}'])

    except Exception as e:
        print(e)
        print('Error While Converting Audio')

    return FinalFileName
  
  # з модулю main.py
  
  
@bot.message_handler(content_types=['voice'])
def voice_processing(message):

    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path
                                        
    with open('voice_message.m4a', 'wb') as new_file:
        new_file.write(downloaded_file)

    converted = converter_voice_msg("voice_message.m4a")
    os.remove("voice_message.m4a")

    bot.send_audio(message.chat.id, converted)
