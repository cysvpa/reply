"""
    텍스트 파일을 형태소 별로 분류하여 cvs파일 형식으로 제공하기
    입력 : txt파일
    출력 : 가중치를 고려한 단어(원형)

"""


READ_TXT = open("comment.txt",'r',encoding="UTF-8")
text= READ_TXT.read()

#1. 정규화
import re
# 소문자와 대문자가 아닌 것은 공백으로 대체한다.
letters_only = re.sub('[^a-zA-Z]', ' ', text)
letters_only[:700]

# 모두 소문자로 변환한다.
lower_case = letters_only.lower()
# 문자를 나눈다. => 토큰화
words = lower_case.split()
print(len(words))
print(words)


#2. 불용어 제거
import nltk
from nltk.corpus import stopwords
stopwords.words('english')[:10]

words = [w for w in words if not w in stopwords.words('english')]
print(len(words))
print(words)

#3. 스테밍 어간, 어미 분석기

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')
words = [stemmer.stem(w) for w in words]
print(len(words))
print(words)

#4 단어 빈도수 체크하기
from collections import Counter
print(Counter(words).most_common())

