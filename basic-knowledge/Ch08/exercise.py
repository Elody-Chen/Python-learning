# ex 8.25
class Textfile:

    def __init__(self, filename:str):
        self.infile = open(filename)
        self.wholeStr = self.infile.read()
        self.wordList = []
        self.lineList = self.wholeStr.split("\n")


    def read(self) -> str:
        '将整个文件读取为一个字符串'
        return self.wholeStr
    

    def readlines(self) -> list:
        '读取文件的所有行'
        return self.lineList


    def nchars(self) -> int:
        '返回文件的字符数'
        return len(self.wholeStr)
    

    def nwords(self) -> int:
        '返回文件的单词数'
        return len(self.wholeStr.split())


    def nlines(self) -> int:
        '返回文件的行数'
        return len(self.lineList)


    def grep(self, targetStr:str) -> int:
        '输出目标字符串在文件中出现的行号以及行'
        targetLineList = []
        for line in range(self.nlines()):
            if targetStr in self.lineList[line]:
                targetLineList.append(line)
                print("{}:{}".format(line, self.lineList[line]))
    

    def words(self):
        '返回文件中不重复单词的列表'
        newS = self.wholeStr.replace("."," ")
        newS = newS.replace(","," ")
        newS = newS.replace(";"," ")
        newS = newS.replace("!", " ")
        newS = newS.replace("\n"," ")
        newS = newS.replace("\'"," ")
        newS = newS.replace("\""," ")

        self.wordList = newS.split()

        return list(set(self.wordList))


    def occurrence(self):
        '统计每个单词在文件中出现的次数'
        myDict = {}
        for curWord in self.words():
            curCount = self.wordList.count(curWord)
            myDict.update({curWord : curCount})

        return myDict


    def average(self):
        wordCountList = []
        for curLine in self.lineList:
            newLine = curLine.replace("!", " ")
            newLine = newLine.replace("?", " ")
            newLine = newLine.replace(".", " ")
            curWordList = newLine.split()
            wordCountList.append(len(curWordList))

        aveWordCount = sum(wordCountList) / len(wordCountList)
        maxWordCount = max(wordCountList)
        minWordCount = min(wordCountList)

        return tuple((aveWordCount, maxWordCount, minWordCount))