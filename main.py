import requests
from lxml import etree
import time
from tqdm import tqdm

DICURL="http://youdao.com/w/eng/"
INURL="./txt/input.txt"
OUTURL="./txt/output.txt"
vocab={}

def search(word):
    if word=="":
        print("No input is detected, try to input again")
        return ""
    url=DICURL+word
    res=requests.get(url)
    htm=res.text
    sel=etree.HTML(htm)
    ans=sel.xpath("//div[@id='phrsListTab']/div[@class='trans-container']/ul/li/text()")
    ret=""
    if ans==[]:
        print("cannot find the definition of the word "+word)
        return ""
    for itm in ans:
        ret+=itm.split("；")[0]+" "
    return ret

def txtMode():
    print("="*52)
    print("|  Welcome to TxtMode. Make sure you have created  |")
    print("|  a txt file in the path './txt/input.txt'\t   |")
    print("="*52)
    with open(INURL,"r") as f:
        voc=f.readlines()
        print("|  There are totally "+str(len(voc))+" vocabulary words \t   |")
        print("="*52)
        for i in tqdm(voc):
            if(i=="\n" or i==""): continue
            i=i.strip("\n")
            vocab[i]=search(i)

    with open(OUTURL,"w") as f:
        for i in vocab:
            wr=i+"\t"+vocab[i]+"\n"
            f.write(wr)
    print("done. Program ends in 3 seconds...")
    time.sleep(3)

def liveMode():
    try:
        print("="*73)
        print("|    Welcome to LiveMode. In here, you can type any vocabulary word.\t|")
        print("|    They will be saved into the output txt unless you type in 'b' \t|")
        print("|    and 'entr' to cancel it. You can type 'z' and 'etr' to exit\t\t|")
        print("="*73)
        word=input("Please input a vocab word: ")
        las_word=word
        while 1:
            
            defin=search(word)
            if defin=="":   #no result is gained, denoting error in input
                pass
            else:
                print(defin)
            print()
            
            word=input("Please input a vocab word: ")
            if word=="b":
                print("Cancel the saving process\n")
                word=input("Please input a vocab word: ")
                las_word=word
                continue
            elif word=="z":
                with open(OUTURL,"a") as f:
                    f.write(las_word+"\t"+defin+"\n")
                exit()

            if defin!="":
                with open(OUTURL,"a") as f:
                    f.write(las_word+"\t"+defin+"\n")
            las_word=word

            
    except SystemExit:
        print ("All work is saved.\nBye~")
    else:
        print("Error occurs. Program ends in 3 seconds... ")
        time.sleep(3)

def main():
    print("="*33)
    print("|  Welcome!\t\t\t|")
    print("|  Author: Charlie\t\t|")
    print("|  Email: hi@smscharlie.com\t|")
    print("="*33)
    mod=0
    while mod!="1" and mod!="2":
        mod=input("Please input a mode (1 for txt mode; 2 for live mode): ")
    if mod=="1":
        txtMode()
    elif mod=="2":
        liveMode()

if __name__=="__main__":
    main()