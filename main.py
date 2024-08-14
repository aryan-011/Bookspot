def countWords(book):
    return len(book.split())

def countChars(book):
    mydict={}
    lower=book.lower()

    for ch in lower:
        if ch.isalpha():
            if ch in mydict:
                mydict[ch]+=1
            else :
                mydict[ch]=1
    return mydict
def sort_on(dict):
    return dict['count']
def main():
    with open('books/Frankenstein.txt') as f:
        file_contents=f.read()
        print("--.Begin Report of Frankenstein.txt.--")
        print(countWords(file_contents),"words found in the text")
        charCOunt = countChars(file_contents)
        listCnt = [{"char":key,"count":value} for key,value in charCOunt.items()]
        listCnt.sort(reverse=True,key=sort_on)
        for dic in listCnt:
            print("The", dic["char"] ,"was found ",dic["count"] ,"times")

main()
