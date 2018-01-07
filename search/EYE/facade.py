import mysql.connector
import operator

import string, re
from nltk import PorterStemmer

def tokenize(inputStr):
    #remove non-alphanumeric characters
    pattern = re.compile('[\W_]+')
    reducedStr = inputStr
    reducedStr = pattern.sub(' ', reducedStr)
    print("-----tokenizer--------")
    print(reducedStr.split())
    print("----end tokenizer-----")
    return reducedStr.split()

def addWordToToken(tokenList, word):
    if len(word) > 1:
        tokenList.append(word)

def stem(word):
    word = PorterStemmer().stem(word)
    return word

def removeStopWords(stemmedList):
    stop_words=(
            'am', 'ii', 'iii', 'per', 'po', 're', 'a', 'about', 'above', 'across',
            'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone',
            'along', 'already', 'also', 'although', 'always', 'am', 'among',
            'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any',
            'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around',
            'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes',
            'becoming', 'been', 'before', 'beforehand', 'behind', 'being',
            'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both',
            'bottom', 'but', 'by', 'can', 'cannot', 'cant', 'con', 'could',
            'couldnt', 'cry', 'describe', 'detail', 'do', 'done', 'down', 'due',
            'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else',
            'elsewhere', 'empty', 'enough', 'even', 'ever', 'every', 'everyone',
            'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty',
            'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly',
            'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get',
            'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her',
            'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers',
            'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i',
            'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it',
            'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least',
            'less', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill',
            'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must',
            'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless',
            'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not',
            'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',
            'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our',
            'ours', 'ourselves', 'out', 'over', 'own', 'per', 'perhaps',
            'please', 'pre', 'put', 'rather', 're', 'same', 'see', 'seem',
            'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should',
            'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some',
            'somehow', 'someone', 'something', 'sometime', 'sometimes',
            'somewhere', 'still', 'such', 'take', 'ten', 'than', 'that', 'the',
            'their', 'them', 'themselves', 'then', 'thence', 'there',
            'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these',
            'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three',
            'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too',
            'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under',
            'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well',
            'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where',
            'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon',
            'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever',
            'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without',
            'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves',
            )

def find(query):
    
    #create indexes first
    wordDic = {} #this is a dictionary of dictionaries
    cnx = mysql.connector.connect(user='search',password='search@123',database='searchEngine')
    cursor = cnx.cursor()
    cursor.execute("select * from info")
    for (ID, main, additional, url) in cursor:
        print(ID, main, additional, url)
        
        #tokenize all details
        tokenList = []
        tMain = tokenize(main)
        tAdditional = tokenize(additional)

        for word in tMain:
            addWordToToken(tokenList, word)
        for word in tAdditional:
            addWordToToken(tokenList, word)
        
        #stemmer
        stemmedTokenList = []
        for token in tokenList:
            stemmedTokenList.append(stem(token))
        
        #remove stop words
        removeStopWords(stemmedTokenList)

        #add words from list to dictionary
        entry = {} #entry is dictionary of url(as key) and count(as value)
        for token in stemmedTokenList:
            if token in wordDic:
                entry = wordDic[token]
            
                if url in entry:
                    count = wordDic[token][url] + 1
                    wordDic[token][url] = count
                else:
                    wordDic[token][url]=1
            else:
                wordDic[token] = {url:1}

    #Now that the indexes have been created...perform search operation using indexes.
    #tokenize input first
    tokenList = []
    tQuery = tokenize(query)
    for word in tQuery:
        addWordToToken(tokenList, word)
        
    #stemmer
    stemmedTokenList = []
    for token in tokenList:
        stemmedTokenList.append(stem(token))

    #remove stop words
    removeStopWords(stemmedTokenList)

    #calculate score
    
    queryLen = len(stemmedTokenList)
    multiplier = [1]*queryLen #this is the score multiplier(useful for increasing priority of certain keywords in query)
    scoreDic = {} #this is a dictionary of url(key) and score(value)
    
    #print(queryLen)
    for i in range(queryLen):
        word=stemmedTokenList[i]
        #print(word)

        if word in wordDic:
            entry = wordDic[word]
            
            for url in entry:
                if url in scoreDic:
                    scoreDic[url] = scoreDic[url] + (entry[url] * multiplier[i])
                else:
                    scoreDic[url] = (entry[url] * multiplier[i])
        else:
            pass #do nothing right now. Maybe we will add some code here in future.

    print("Stemmed token list")
    print(stemmedTokenList)
    print("--------word dic-------")
    print(wordDic)
    print("-----------scoreDic----------")
    print(scoreDic)

    #now sort the scoreDic and return results sorted by non-decreasing score value
    sortedScoreDic = sorted(scoreDic.items(), key=operator.itemgetter(1), reverse=True)
    
    resultStr = ""
    
    for entry in sortedScoreDic:
       resultStr = resultStr + str(entry[0]) + "," + str(entry[1]) + ","

    print(resultStr+"Rohit")
    return resultStr


