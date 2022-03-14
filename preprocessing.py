#Read about re library in python
#https://www.w3schools.com/python/python_regex.asp
#https://www.tutorialspoint.com/python/python_reg_expressions.htm
#https://github.com/adhaamehab/arabicnlp
def process(tweet):
    tweet = re.sub(r'https\S+', '', tweet)
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'[a-zA-Z]+', '', tweet, re.I)
    tweet = tweet.replace('"',' ')
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    tweet = re.sub(p_longation, subst,tweet)
    tweet = tweet.replace('_',' ')
    tweet = tweet.replace('@',' ')
    tweet = tweet.replace('#',' ')
    tweet = re.sub(r'[0-9]+', '', tweet, re.I)
    return(tweet.strip())
