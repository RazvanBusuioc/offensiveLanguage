from ast import Constant
from fileinput import filename
from time import sleep
from pyrsistent import b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains     
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from broadcastArhitecture import Comment, FacebookBroadcast

import sys
import signal
import os
import csv

facebookBroadcast = FacebookBroadcast()
now = datetime.now()

def handler(signum, frame):
    storeComments()
    exit(1)

signal.signal(signal.SIGINT, handler)

def exists_by_xpath(xpath, browser):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def isLiveBroadCast(browser):
    liveButtonClassIdentifier = "//div[@class='bp9cbjyn jk6sbkaj kdgqqoy6 ihh4hy1g qttc61fc rq0escxv pq6dq46d datstx6m jb3vyjys p8fzw8mz qt6c0cv9 pcp91wgn afxn4irw m8weaby5 ee40wjg4 q1gqmpn5 jbu8tgem l44iypv3']"
    if len(browser.find_elements(By.XPATH, liveButtonClassIdentifier)) == 0:
        return False
    return True

def getNumberOfReactsFromText(text):
    if text.isnumeric():
        return int(text)
    
    if "K" in text:
        partition = text.partition("K")[0]
        return int(float(partition) * 1000)
    
    return 0

def gatherComments(browser):
    global facebookBroadcast
    titleSet = False
    descriptionSet = False

    acceptCookiesButtonXPath = "//*[@id=\"facebook\"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div"
    broadcastTitleIdentifier = "//div[@class='ihqw7lf3 discj3wi tw6a2znq d1544ag0 stjgntxs ni8dbmo4 cwj9ozl2']"
    commentDivIdentifier = "//div[@class='rj1gh0hx buofh1pr ni8dbmo4 stjgntxs hv4rvrfc']"
    commentSenderIdentifier = ".//div[@class='btwxx1t3 nc684nl6 bp9cbjyn']"
    commentTextIdentifier = ".//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']"
    commentReactionsIdentifier = ".//div[@class='du4w35lb pmk7jnqg lthxh50u ox23h4wi kr9hpln1']"
    commentNumberOfReactionsIdentifier = ".//span[@class='g0qnabr5 hyh9befq qt6c0cv9 n8tt0mok jb3vyjys j5wam9gi knj5qynh e9vueds3 m9osqain']"
    broadcastReactionsIdentifier = "//span[@class='ni8dbmo4 stjgntxs ltmttdrg']"
    commentSeeMoreActionIdentifier = ".//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p']"
    notLoggedInIdentifier = "//div[@class='l9j0dhe7 du4w35lb cjfnh4rs j83agx80 cbu4d94t lzcic4wl ni8dbmo4 stjgntxs oqq733wu cwj9ozl2 io0zqebd m5lcvass fbipl8qg nwvqtn77 nwpbqux9 iy3k6uwz e9a99x49 g8p4j16d bv25afu3 gc7gaz0o k4urcfbm']"
    notLoggedInButton = ".//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu tv7at329']"
    shortDescriptionIdentifier = "//div[@class='n1l5q3vz']"
    descriptionSeeMoreButtonIdentifier = "//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p']"
    fullDescriptionIdentifier = "//div[@class='e5nlhep0 nu4hu5il eg9m0zos']"

    idx = 0

    while True: 
        browser.get(facebookBroadcast.URL)

        if (exists_by_xpath(acceptCookiesButtonXPath, browser)):
            acceptCookiesButton = browser.find_element(By.XPATH, acceptCookiesButtonXPath)
            acceptCookiesButton.click()

        sleep(2) # wait for html content to load
        
        if (exists_by_xpath(notLoggedInIdentifier, browser)):
            notLoggedInDialog = browser.find_element(By.XPATH, notLoggedInIdentifier)
            if (exists_by_xpath(notLoggedInButton, notLoggedInDialog)):
                notLoggedInButton = notLoggedInDialog.find_element(By.XPATH, notLoggedInButton)
                try:
                    notLoggedInButton.click()
                except Exception:
                    continue
                
        if titleSet == False and exists_by_xpath(broadcastTitleIdentifier, browser):
            titleSet = True
            liveTitle = (browser.find_element(By.XPATH, broadcastTitleIdentifier)).text.replace("\n", " ").replace('\r', '')
            facebookBroadcast.setTitle(liveTitle)

        
        if descriptionSet == False:
            if (exists_by_xpath(descriptionSeeMoreButtonIdentifier, browser)):    
                seeMoreButton = browser.find_element(By.XPATH, descriptionSeeMoreButtonIdentifier)
                try:
                    seeMoreButton.click()
                except Exception:
                    continue
                

                if exists_by_xpath(fullDescriptionIdentifier, browser):
                    description = browser.find_element(By.XPATH, fullDescriptionIdentifier).text.replace("\n", " ").replace('\r', '')
                    facebookBroadcast.setDescription(description)
                    descriptionSet = True
                else:
                    facebookBroadcast.setDescription("")

            else: #short description
                if exists_by_xpath(shortDescriptionIdentifier, browser):
                    description = browser.find_element(By.XPATH, shortDescriptionIdentifier).text.replace("\n", " ").replace('\r', '')
                    facebookBroadcast.setDescription(description)
                    descriptionSet = True
                else:
                    facebookBroadcast.setDescription("")
        
        # number of reacts
        if (exists_by_xpath(broadcastReactionsIdentifier, browser)):
            numberOfReacts = getNumberOfReactsFromText(browser.find_element(By.XPATH, broadcastReactionsIdentifier).text)
            facebookBroadcast.setNumberOfReacts(numberOfReacts)

        if not isLiveBroadCast(browser): 
            print(datetime.now().strftime("%H:%M:%S") + ": Live broadcast has stopped. Exiting...")
            break

        #comments
        comments = browser.find_elements(By.XPATH, commentDivIdentifier)
        for comment in comments:
            children = comment.find_elements(By.XPATH ,"*")

            if (len(children) == 2):
                # children[0] -> sender and text divs
                # children[1] -> time elapsed since the comment was sent

                # timeElapsed = children[1].text # NOT USED
                commentText = ""
                commentSender = ""

                # some comments are too long and need a see more action click
                if (exists_by_xpath(commentSeeMoreActionIdentifier, children[0])):
                    try:
                        children[0].find_element(By.XPATH, commentSeeMoreActionIdentifier).click()
                    except Exception:
                        continue

                if exists_by_xpath(commentTextIdentifier, children[0]):
                    commentText = children[0].find_element(By.XPATH, commentTextIdentifier).text.replace("\n", " ").replace('\r', '')
                
                if exists_by_xpath(commentSenderIdentifier, children[0]):
                    commentSender = children[0].find_element(By.XPATH, commentSenderIdentifier).text

                # if len(commentText) == 0 or len(commentSender) == 0:
                #     continue

                noReacts = 0

                if (exists_by_xpath(commentReactionsIdentifier, children[0])):
                    reacts = children[0].find_element(By.XPATH, commentReactionsIdentifier)

                    if (exists_by_xpath(commentNumberOfReactionsIdentifier, reacts)):
                        noReacts = getNumberOfReactsFromText(reacts.find_element(By.XPATH, commentNumberOfReactionsIdentifier).get_attribute("innerHTML"))
                
                comment = Comment(commentSender, commentText, 0, noReacts)
                facebookBroadcast.addComment(comment)

            if (len(children) == 3):
                # do nothing. it s a sticker
                continue

        print(datetime.now().strftime("%H:%M:%S") + ": Added a set of comments! Total number of comments gathered = " + str(len(facebookBroadcast.comments)))

        idx += 1
        if idx % 5 == 0:
            storeComments()

        sleep(5) # time between refreshes

    browser.close()

# make dir path a global variable!
def storeComments():
    print(datetime.now().strftime("%H:%M:%S") + ": Storing gathered comments")

    liveTitleString = "Unnamed"
    if len(facebookBroadcast.title) > 0:
        liveTitleString = "_".join(str.split(facebookBroadcast.title)[:10])

    dirName = liveTitleString + "@" + now.strftime("%d_%m_%Y_%H_%M_%S")
    
    dirPath = os.path.join("facebookData", dirName)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    commentsFileName = os.path.join(dirPath, "comments.csv")
    broadcastFileName = os.path.join(dirPath, "broadcast.csv")

    # write in comments.csv file - info about all comments of the broadcast
    f = open (commentsFileName, "w")
    writer = csv.writer(f)
    writer.writerow(["Sender", "Text", "NumberOfReacts"])
    for comment in facebookBroadcast.comments:
        writer.writerow([comment.sender, comment.text, str(comment.numberOfReacts)])
    f.close()

    # write in broadcast.csv file - info about the broadcast
    f = open (broadcastFileName, "w")
    writer = csv.writer(f)
    writer.writerow(["Title", "Description", "URL", "NumberOfReacts"])
    writer.writerow([facebookBroadcast.title, facebookBroadcast.description, facebookBroadcast.URL, str(facebookBroadcast.numberOfReacts)])
    f.close()

def main():
    global facebookBroadcast
    
    if (len(sys.argv) < 2):
        print("No URL provided")
        exit()

    liveBroadcastURL = sys.argv[1]
    facebookBroadcast.setURL(liveBroadcastURL)

    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
        
    s=Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=option)
    browser.maximize_window()

    gatherComments(browser)

    storeComments()

if __name__ == "__main__":
    main()
