import requests
from lxml import etree

DICURL="http://youdao.com/w/eng/"
INURL="./txt/input.txt"
OUTURL="./txt/output.txt"
vocab={}

def search(word):
    url=DICURL+word
    res=requests.get(url)
    htm=res.text
    sel=etree.HTML(htm)
    ans=sel.xpath("//div[@id='phrsListTab']/div[@class='trans-container']/ul/li/text()")
    ret=""
    if ans==[]:
        print("cannot find the definition of the word "+word)
        return ret
    for itm in ans:
        ret+=itm.split("；")[0]+" "
    return ret

def engine():
    with open(INURL,"r") as f:
        for i in f:
            if(i=="\n" or i==""): continue
            i=i.strip("\n")
            vocab[i]=search(i)
    with open(OUTURL,"w") as f:
        for i in vocab:
            wr=i+" "+vocab[i]+"\n"
            f.write(wr)
    print("done. Program ends")

def live():
    try:
        while 1:
            word=input("please input a vocab word: ")
            defin=search(word)
            if defin=="": 
                print()
                continue
            print(defin)
            with open(OUTURL,"a") as f:
                f.write(word+" "+defin+"\n")
            print()
    except:
        print("Program ends")

def main():
    mod=input("please input a mode (1 for txt mode; 2 for live mode): ")
    if mod=="1":
        engine()
    elif mod=="2":
        live()
    else:
        print("input error. Program terminetes")

if __name__=="__main__":
    main()