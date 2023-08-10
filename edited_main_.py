# access dataset from google drive
from google.colab import drive

drive.mount("/content/drive")

# imports
import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from sklearn.feature_extraction import _stop_words
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# open and read dataset files
# custome subset we made out of bussiness and reviews dataset
df_restaurant_review = open(
    "/content/drive/MyDrive/yelp_data/business_reviews_restaurants.csv", "r"
)
df_restaurant_review = pd.read_csv(
    "/content/drive/MyDrive/yelp_data/business_reviews_restaurants.csv"
)

# business data
df_business = open(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_business.csv", "r"
)
df_business = pd.read_csv(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_business.csv"
)

# checkins data
df_checkin = open(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_checkin.csv", "r"
)
df_checkin = pd.read_csv(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_checkin.csv"
)

# review data
df_review = open(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_review.csv", "r"
)
df_review = pd.read_csv(
    "/content/drive/MyDrive/yelp_data/yelp_academic_dataset_review.csv"
)

# tip data
df_tip = open("/content/drive/MyDrive/yelp_data/yelp_academic_dataset_tip.csv", "r")
df_tip = pd.read_csv("/content/drive/MyDrive/yelp_data/yelp_academic_dataset_tip.csv")

# user data
df_user = open("/content/drive/MyDrive/yelp_data/yelp_academic_dataset_user.csv", "r")
df_user = pd.read_csv("/content/drive/MyDrive/yelp_data/yelp_academic_dataset_user.csv")
# data_busi.head()

plt.style.use("ggplot")

"""
Data Analysis
"""
# initializer for Analysis table
# find mean for all attributes
star_rating_mean = df_review.mean()[0]
useful_review_mean = df_review.mean()[1]
funny_review_mean = df_review.mean()[2]
cool_review_mean = df_review.mean()[3]
review_year_mean = df_review.mean()[4]
# make a list of review mean
review_mean = [
    star_rating_mean,
    useful_review_mean,
    funny_review_mean,
    cool_review_mean,
    review_year_mean,
]

# find minimum and maximum value for all attributes
star_rating_range = [df_review.min()[3], df_review.max()[3]]
useful_review_range = [df_review.min()[4], df_review.max()[4]]
funny_review_range = [df_review.min()[5], df_review.max()[5]]
cool_review_range = [df_review.min()[6], df_review.max()[6]]
review_year_range = [df_review.min()[8], df_review.max()[8]]
# make a list of review range with all attributes's min and max value list
review_range = [
    star_rating_range,
    useful_review_range,
    funny_review_range,
    cool_review_range,
    review_year_range,
]

# temp_mode will find mode for review dataframe on axis 0 and we convert the result in np.array for ease of use
temp_mode = df_review.mode(axis=0)
temp_mode_list = np.array(temp_mode)

# find mode for all attributes
star_rating_mode = temp_mode_list[0][3]
useful_review_mode = temp_mode_list[0][4]
funny_review_mode = temp_mode_list[0][5]
cool_review_mode = temp_mode_list[0][6]
review_year_mode = temp_mode_list[0][8]
# make a list of review mode
review_mode = [
    star_rating_mode,
    useful_review_mode,
    funny_review_mode,
    cool_review_mode,
    review_year_mode,
]

# make analysis dataframe
# temp_index= ['Range','Mean','Mode']

# set column names and values for data frames with the list generated before for range, mean and mode
df_analysis = pd.DataFrame(
    {
        "Star rating": [star_rating_range, star_rating_mean, star_rating_mode],
        "Useful Review": [useful_review_range, useful_review_mean, useful_review_mode],
        "Funny Review": [funny_review_range, funny_review_mean, funny_review_mode],
        "Cool Review": [cool_review_range, cool_review_mean, cool_review_mode],
        "Review Year": [review_year_range, review_year_mean, review_year_mode],
        "index": ["Range", "Mean", "Mode"],
    }
)
# df = pd.DataFrame(review_range, review_mean, review_mode,index=index)
df_analysis = df_analysis.set_index("index")
df_analysis


"""
Data visulization

use this weblink to enhance the results
https://towardsdatascience.com/text-mining-and-sentiment-analysis-for-yelp-reviews-of-a-burger-chain-6d3bcfcab17b 
2.2 Exploratory Data Analysis
"""

# made a new column name "year" derived from "date" attribute available in "df_review"
df_review["year"] = pd.DatetimeIndex(df_review["date"]).year

df_review.head()

# make a custome dataframe "df_review_count" which shows the count of reviews per year
df_review_count = df_review.groupby(["year"]).agg({"review_id": "count"})

df_review["date"] = pd.to_datetime(df_review["date"])
df_review = df_review.set_index("date")
# df_review
# df_restaurant_review
# df_restaurant_review.info()

# number of reviews vs year plot
plt.plot(df_review_count["review_id"])
plt.xlabel("year", fontsize=12)
plt.ylabel("No. of reviews", fontsize=12)
plt.title("No. of reviews per month", fontsize=16)
plt.show()

"""
use this weblink to enhance the results
https://www.kaggle.com/code/jagangupta/what-s-in-a-review-yelp-ratings-eda#7.-User-networks:
3. rating distribution 
rating distribution over various business
"""

temp_business = df_business["stars"].value_counts()
temp_business = temp_business.sort_index()

# plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(temp_business.index, temp_business.values, alpha=0.9)
plt.title("Distribution of star ratings", fontsize=16)
plt.ylabel("No. of businesses", fontsize=12)
plt.xlabel("Star Ratings ", fontsize=12)

# rating distribution of reviews get by per city
city_review = df_business["city"].value_counts()
city_review = city_review.sort_values(ascending=False)
city_review = city_review.iloc[0:20]
plt.figure(figsize=(16, 4))
ax = sns.barplot(city_review.index, city_review.values, alpha=0.8)
plt.title("Which city has the most reviews?", fontsize=16)
locs, labels = plt.xticks()
plt.setp(labels, rotation=50)
plt.ylabel("no. of businesses", fontsize=12)
plt.xlabel("City", fontsize=12)

# pie chart plot

df_ph = pd.DataFrame(df_restaurant_review)
s_words = ['pizza','burger','chinese','fries','chicken','indian']
s_words
from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer(vocabulary=s_words,lowercase=False)

word_count = vec.fit_transform(df_ph['text'].values.astype('U'))
vec.get_feature_names()

word_array = word_count.toarray()
word_array.shape

word_array.sum(axis=0)

t_df = pd.DataFrame(index=vec.get_feature_names(),data=word_array.sum(axis=0)).rename(columns={0:'Word Count'})

plt.pie(word_array.sum(axis=0),labels=vec.get_feature_names(),explode=(0.1,0.1,0.1,0.1,0.1,0.1))
plt.title('Distribution of Food Related Words in User Reviews')
fig = plt.figure(figsize=(15,10))
plt.show