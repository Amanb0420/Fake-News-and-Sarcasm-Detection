import streamlit as st
import pandas as pd
import pickle
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
import requests
import regex as re
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\fake.pkl', 'rb') as f:
    svclf=pickle.load(f)
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\sarc3.pkl','rb') as g:
    sarcsvc=pickle.load(g)
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\vec.pkl','rb') as h:
    vec=pickle.load(h)
with open('C:\\Users\\amanb\\OneDrive\\Desktop\\Coding\\Pyfiles\\ipynbs\\vec2.pkl','rb') as x:
    vec2=pickle.load(x)

def WebScrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') 
    listOfParas=[]
    for i in soup.find_all('p'):
        listOfParas.append(i.text.strip())
    listOfSentences=[]
    for i in listOfParas:
        for sentence in i.split('.'):
            if sentence == "":
                continue
            listOfSentences.append(sentence)
    if " All rights reserved" in listOfSentences:
        listOfSentences.remove(" All rights reserved")
    return listOfSentences,listOfParas

def clean(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    # text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text
# svclf=LinearSVC(dual=0,random_state=42)

def isReal(url):
    los,lop=WebScrape(url)
    testing_news = {"text":[''.join(los)]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(clean) 
    new_x_test = new_def_test["text"]
    new_xv_test = vec.transform(new_x_test)
    ans=svclf.predict(new_xv_test)
    return ans

def CalcSarcasmPercentage(los):
    los,lop=WebScrape(url)
    res=[]
    for x in los:       
        new=vec2.transform([x]).toarray()
        ans=sarcsvc.predict(new)
        res.append(ans[0])
        if ans[0]==1:
            sarclines=[]
            # if x==" All rights reserved":
            #     continue
            sarclines.append(x)
    count=0
    for y in res:
        if y==1:
            count+=1
    percsarc=round(((count/len(res))*100),2)
    return percsarc,sarclines

url= st.text_input('News Article URL',"https://www.theonion.com/man-returns-to-work-after-vacation-with-fresh-reenergi-1819574342")
if st.button('Analyze'):
    per,sarc=CalcSarcasmPercentage(url)
    if isReal(url)==0 or per>30.00:
        st.write("Fake News!")
        st.write("Sarcasm percentage:",per,"%")
        st.write("Sarcastic lines:")
        for j in range(len(sarc)):
            st.write(j+1,sarc[j])
    else:
        st.write("Real News!")
        st.write("Sarcasm percentage:",per,"%")
        # st.write("Sarcastic lines:")
        # for k in range(len(sarc)):
        #     st.write(k+1,sarc[k])
# print(CalcSarcasmPercentage(url))
# isReal(url)
