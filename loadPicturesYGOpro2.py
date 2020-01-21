# -*- coding: utf-8 -*-
"""
credits:
    
Federico Ribaldi
Emanuele Volanti
"""
import os
import urllib

imagePath = 'https://storage.googleapis.com/ygoprodeck.com/pics/'

def loadPictures(cardId):
    cardExist = False
    path="picture/card"
    for roots,dirs,files in os.walk(path):
        for f in files:
            if f==cardId+'.jpg':
                cardExist = True
                break
    if(not cardExist):            
        print("i'm downloading: "+cardId)
        try:
            urllib.request.urlretrieve(imagePath+cardId+'.jpg',path+'/'+cardId+'.jpg')
        except:
            print("check your network connection or retry later")

def checkCards(deck):
    path='deck'
    with open( path +'/'+deck) as cardsInADeck:
        for f in cardsInADeck:
            f = f.replace("\n","")
            if f.isdigit():
                loadPictures(f)
            
def main(): 
    print("start downloading cards")
    for roots,dirs,files in os.walk('deck'):
        for deck in files:
            checkCards(deck)

main()
print("all cards are been downloaded")
