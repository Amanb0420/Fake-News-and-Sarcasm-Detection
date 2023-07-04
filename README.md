# Fake-News-and-Sarcasm-Detection
A Machine Learning approach to detect fake news from article links and calculate percentage of sarcasm and print sarcastic lines.
This Project is written in Python and uses the sklearn, BeautifulSoup(BS4) and numpy libraries.

The datasets used in the repo are:

1) Fake and Real news : https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=True.csv
2) Sarcasm detection :  https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection?select=Sarcasm_Headlines_Dataset.json

Steps to execute:
1) Download the datasets from the links above

2)Run the model_training.ipynb file to build and train the model which will be stored in a pickle(.pkl) file

3)Run the main.py file to integrate the model with Streamlit for building a locally hosted web based application 
