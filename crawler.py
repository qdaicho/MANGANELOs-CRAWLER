# import necessary libraries
import pprint
from math import ceil
import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import filedialog
import re
import os
import time
import sys

#this function removes all downloaded pictures from a folder
def remove_pictures(a, b, fullpath):
    total = (a + b) // 2
    for i in range(a, b + 1):
        if os.path.exists(fullpath + "/pg" + str(i) + ".png"):

            bar(i, total, 50, 1, 'deleting page')

            os.remove(fullpath + "/pg" + str(i) + ".png")
        elif os.path.exists(fullpath + "/pg" + str(i) + ".jpg"):

            bar(i, total, 50, 1, 'deleting page')

            os.remove(fullpath + "/pg" + str(i) + ".jpg")

    print("finished deleting everything")

#this function returns a list of all the image urls of any webpage
def get_img_links(link_to_images):
    # create response object
    response = requests.get(link_to_images)

    # create beautiful-soup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all links on web-page
    img_tag = soup.findAll('img')
    type(img_tag)
    # filter the img tags with only the link to images
    links = [img['src'] for img in img_tag]
    return links

# this function downloads all the images from a webpage into a specified directory
def download_img_to_dir(image_list, fullpath):
    filetype = ""
    total = len(image_list)
    for i in range(0, total):

        if image_list[i][-4:] == ".jpg":
            filetype = ".jpg"
        else:
            filetype = ".png"

        pic = requests.get(image_list[i],
                           stream=True, headers={'User-agent': 'Mozilla/5.0'})

        if pic.status_code == 200:
            with open(fullpath + "/pg" + str(i) + filetype, 'wb') as f:
                f.write(pic.content)

                bar(i, total, 50, 1, 'downloaded page')

# this function clears the terminal in windows or mac/linux
def clear():
    os.system('cls') if (os.name == 'nt') else os.system('clear')

counter = 0
# this function prints a progress bar to the terminal
def bar(progress, total, bar_length, sleep_time, message):
        if message is not None:
            n = ceil(bar_length * (progress / total))
            a = int((progress / total)*100)
            print(message + ' ' + str(progress) + '/' + str(total) + " ...\n" + '[' + format(a, '02d') + "%] |" + ('█'*n), end="")
            print("░"*(bar_length-(n+1)) + " |")
            time.sleep(sleep_time)
            # clear()
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
        else:
            n = ceil(bar_length * (progress / total))
            a = int((progress / total)*100)
            print('[' + format(a, '02d') + "%] |" + ('█'*n), end="")
            print("░"*(bar_length-(n+1)) + " |")
            time.sleep(sleep_time)
            # clear()
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line

#####################################################################################################
######################################THIS IS THE MAIN CODE #########################################
#####################################################################################################
previous_chap = ''
next_chap = ''
current_chap = ''
manga_title = ''
url = ''
directory = ''

throw_table = "(╯°□ °）╯︵ ┻━┻"
putting_table_back = '┬──┬◡ﾉ(° -°ﾉ)'
shrug = '¯\\_(ツ)_/¯'
lenny = '( ͡° ͜ʖ ͡°)'
icu = '┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴'
angry = '(ノಠ益ಠ)ノ'
disapproval = '( ͡° ʖ̯ ͡°)'
confused = '(゜。゜)'
worried = '⊙ ﹏⊙'

counter = 0
j = 0

print('███'*26)
print("""
\t\t    ****************** ******************
\t\t    ****************** ******************
\t\t    ****************** ******************
\t\t    ****************** ******************
\t\t    ********* ******** ******** *********
\t\t    ******* *********   ******** ********
\t\t    ****** *********     ********* ******
\t\t    ***** ********         ******** *****
\t\t    ***** *******            ****** *****
\t\t    ***** ******             ****** *****
\t\t    * **** ****               **** **** *
\t\t    ** **** ***               *** **** **
\t\t    **** **** **             ** **** ****
\t\t    * ****  *** *    * *    * ***  **** *
\t\t    ** ****** ****  *   *  **** ****** **
\t\t    *** **** *****         ***** **** ***
\t\t    *****  ********  * *  ********  *****
\t\t    *****************   *****************
\t\t    *************************************
\t\t    *************************************
    """)
print('\t\t\t Designed and Programmed by\n\t\t\t   Mahir Daian Chowdhury\n')
print('███'*26 + '\n\t\t       WELCOME TO MANGANELO\'s CRAWLER\n' + '███'*26)

manga_title = input('\nWhat is the title of the manga you want to download?\t' + icu + '\n>>>\t')
print('\nThank you, now please enter the url to the page of the manga\nfrom www.mangakakalot.com where you want to start downloading from')
url = input('>>>\t')
j = int(input('\nThank you, how many chapters do you want to download?\n>>>\t'))
print('\nThank you, now we will install the manga to a local directory on your computer...')
print('\nPlease choose whether you want to enter\nyour chosen directory or use our file browser' + worried)
print('[keep in mind that we will handle the making of the actual folder for the manga]\n\n')

if input("FOLDER BROWSER = 'FB'\nENTER DIRECTORY = 'ED'\n>>>\t").upper() == "FB":
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    directory = "" + filedialog.askdirectory(title='SELECT DIRECTORY TO DOWNLOAD MANGA')
else:
    directory = input("\nPlease enter the absolute path to where you want to install the manga:\n==>\t")

print('\n')

directory = directory + '/' + manga_title
# print('your chosen directory is: ' + directory)

for i in range(20):
    bar(i,20, 50, 1, 'Crawling through the code')

try:
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print('The directory already exists!\t' + angry)
except OSError:
    print("Creation of the directory %s failed" % directory)
else:
    print("Successfully created the directory %s " % directory)


while True:
    # print(url)
    sauce = BeautifulSoup(requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'}).text, "html.parser")
    info = str(sauce.find_all('div', class_="btn-navigation-chap")[0])

    current_chap = re.findall(r'chapter_\d*\.?\d*', url)[0]

    if current_chap == 'chapter_1':
        next_chap = re.findall(r'chapter_\d*\.?\d*', info)[0]
        cwd = directory + "/" + current_chap
        try:
            os.mkdir(cwd)
        except OSError:
            print("Creation of the directory %s failed" % cwd)
        else:
            print("Successfully created the directory %s " % cwd)

        images = get_img_links(url)
        download_img_to_dir(images, cwd)
    else:
        previous_chap = re.findall(r'chapter_\d*\.?\d*', info)[0]

        try:
            next_chap = re.findall(r'chapter_\d*\.?\d*', info)[1]
        except IndexError:
            next_chap = ''

        cwd = directory + "/" + current_chap
      
        try:
            os.mkdir(cwd)
        except OSError:
            print("Creation of the directory %s failed" % cwd)
        else:
            print("Successfully created the directory %s " % cwd)

        images = get_img_links(url)
        download_img_to_dir(images, cwd)
        counter+=1
        
        if counter == j:
            break

        if len(re.findall(r'chapter_\d*\.?\d*', info)) is 1:
            break

    url = re.sub(r'chapter_\d*\.?\d*', next_chap, url)

print('███'*26 + '\n\t\t    THANKS FOR USING MANGANELO\'s CRAWLER\n' + '███'*26)
time.sleep(5)
clear()
exit()

#####################################################################################################
# OVER HERE ARE ALL OF THE DEBUG CODE THAT WILL BE USEFULL FOR DEBUGGING
#####################################################################################################

# print(os.getcwd())

# images = get_img_links(url)
# pprint.pprint(images)

# download_img_to_dir(images, directory)
# remove_pictures(0, 50, directory)
#         print("IM IN THE ELSE! " + cwd)

# print('\n\n\n' + str(info) + '\n\n\n')
#
    # print("previous! " + previous_chap)
    # print("current! " + current_chap)
    # print("next! " + next_chap)
#https://mangakakalot.com/chapter/lw921425/chapter_4
