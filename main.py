import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

text = ["This is your first text book", "This is the third text for analysis", "This is another text"]

s.translate(None, string.punctuation)


s.translate(str.maketrans('', '', string.punctuation))


exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)


import re, string, timeit

s = "string. With. Punctuation"
exclude = set(string.punctuation)
table = string.maketrans("","")
regex = re.compile('[%s]' % re.escape(string.punctuation))

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

def test_re(s):  # From Vinko's solution, with fix.
    return regex.sub('', s)

def test_trans(s):
    return s.translate(table, string.punctuation)

def test_repl(s):  # From S.Lott's solution
    for c in string.punctuation:
        s=s.replace(c,"")
    return s

print "sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(1000000)
print "regex     :",timeit.Timer('f(s)', 'from __main__ import s,test_re as f').timeit(1000000)
print "translate :",timeit.Timer('f(s)', 'from __main__ import s,test_trans as f').timeit(1000000)
print "replace   :",timeit.Timer('f(s)', 'from __main__ import s,test_repl as f').timeit(1000000)

if "a" in line:
    line = line.replace("a","")
if "an" in line:
    line = line.replace("an","")
if "the" in line:
    line = line.replace("the","")s


for word in refIDarr:
    line = line.replace(word,'')


refIDarr = ["hello", "world", "lol"]

with open('mytext.txt', "r") as f:
    data = f.readlines()
    for word in refIDarr:
        data = [line.replace(word, "") for line in data]

with open("mytext.txt", "w") as newf:
    newf.writelines(data)



def tokenize(text):
    tokens = word_tokenize(text)
    stems = []
    for item in tokens: stems.append(PorterStemmer().stem(item))
    return stems


# corpus
# word tokenize and stem
text = [" ".join(tokenize(txt.lower())) for txt in text]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(text).todense()
# transform the matrix to a pandas df
matrix = pd.DataFrame(matrix, columns=vectorizer.get_feature_names())
# sum over each document (axis=0)
top_words = matrix.sum(axis=0).sort_values(ascending=False)
