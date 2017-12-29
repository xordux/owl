import mysql.connector

def addWordToToken(tokenList, word):

    pass

def stem(word):
    pass

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
        for word in main:
            addWordToToken(tokenList, )
        for word in additional:
            addWordToToken(tokenList)
        
        #stemmer
        stemmedTokenList = []
        for token in tokenList:
            stemmedTokenList.append(stem(token))
        
        #remove stop words
        removeStopWords(stemmedTokenList)

        #add words from list to dictionary
        entry = {}
        for token in stemmedTokenList:
            if wordDic.has_key(token):
                entry = wordDic[word]
    
    return "Good morning"+query


