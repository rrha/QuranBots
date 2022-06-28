from PIL import Image, ImageDraw, ImageFont
import textwrap
import arabic_reshaper
from bidi.algorithm import get_display
from arabic_reshaper import ArabicReshaper
from time import sleep
from threading import Thread
import time
import tweepy

cfile = open("resources/Counter.txt")
all_lines_variable_cfile = cfile.readlines()

increamentedValue = int(all_lines_variable_cfile[0])

y = 0
configuration = {
    'delete_harakat': False,
    'support_ligatures': True,
    'use_unshaped_instead_of_isolated ':True
}
reshaper = ArabicReshaper(configuration=configuration)

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    y = 0
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height 
    lines = textwrap.wrap(text, width=140)
    for line in lines:
        y = y+1
      
    if y==1:
        y_text = 320
    if y==2:
        y_text = 320
    if y==3:
        y_text = 320
    if y==4:
        y_text = 400    
    if y==5:
        y_text = 420 
    if y==6:
        y_text = 450
    if y==7:
        y_text = 500
    if y==8:
        y_text = 520    
    if y==9:
        y_text = 550
        
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text -= line_height
    

def draw_multiple_line_text_second(image, text, font, text_color, text_start_height):
    
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height 
    lines = textwrap.wrap(text, width=140)
    for line in lines:
        
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text -= line_height
   
def main():
    image = Image.open("resources/images/background.png")  
    fontsize = 30
    font = ImageFont.truetype("resources/fonts/Amiri-Regular.ttf", fontsize) 
    fileone = open("resources/Title.txt", encoding="utf8") 
    filetwo = open("resources/PostBodyAR.txt", encoding="utf8") 
    all_lines_variable_fileone = fileone.readlines()
    all_lines_variable_filetwo = filetwo.readlines()
    text_one = all_lines_variable_fileone[increamentedValue]
    text_two = all_lines_variable_filetwo[increamentedValue]
    reshaped_text_one = arabic_reshaper.reshape(text_one)
    bidi_text_one = get_display(reshaped_text_one )
    reshaped_text_two = reshaper.reshape(text_two)
    bidi_text_two = get_display(reshaped_text_two)
    text_color = (0, 0, 0)
    text_start_height = 550
    font_sura = ImageFont.truetype("resources/fonts/Amiri-Bold.ttf", 30)
    
    draw_multiple_line_text_second(image,bidi_text_one , font=font_sura,text_color=(255,255,255), text_start_height=642)
    draw_multiple_line_text(image, "\ufd3e " + bidi_text_two + "\ufd3f", font, text_color, text_start_height)
    image.save('resources/images/Output.png') 

    
def func():
 fileone = open("resources/PostTitle.txt", encoding="utf8")
 all_lines_variable_fileone = fileone.readlines()  
 # Authenticate to Twitter
 auth = tweepy.OAuthHandler("", "")
 auth.set_access_token("", "")
  
 # Create API object
 api = tweepy.API(auth)

 imagePath = "resources/images/Output.png"
 status = all_lines_variable_fileone[increamentedValue] + "#quran #قرآن"

 # Send the tweet.
 api.update_with_media(imagePath, status)
    
if __name__ == "__main__":
    main()
    func()
    
increamentedValue+=1
Cfile = open("resources/Counter.txt","w").write("%d" %increamentedValue)
    
