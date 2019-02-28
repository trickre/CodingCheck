#coding:utf8
import sys

def main():
    args = sys.argv
    file = args[1]
    lines = []
    with open(file,mode="r",encoding="utf-8") as f:
        lines = f.readlines()
    cnt_line = 1
    for l in lines:
        tf,text = check_zen_space(l)
        if(tf == True):#全角スペースが見つかった
            print("Line{}  : yous'ld -->{}".format(cnt_line,text),end="")
        cnt_line += 1

"""
check_zen_space()
input:(string)text 1 line
output:(T/F,全角スペースを半角スペースで置き換えたテキスト)
    True:全角含む,False:全角含まない
"""
def check_zen_space(text):
    if(text.find("　") != -1):
        text_return = text.replace("　"," ")
        return(True,text_return)
    else:
        return(False,text)

if __name__ =="__main__":
    main()