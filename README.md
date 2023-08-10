# Yelp-Analysis
Here are some Interesting Findings from the Yelp Dataset

- Considering the star rating range from 1-5 the mean or average of star ratings is 3.83 which is above average meaning around 78% of the restaurants in America are considered decent by the customers. 

<img width="715" alt="matrix (1)" src="https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/bcae2ae1-2614-4d3d-bdce-8969f98f978b">

- the below GEO-MAP shows the location of all the restaurants and their ratings

<img width="1285" alt="map" src="https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/e1ca51d9-7b54-409d-9276-e2e7bb1edca8">

- The whole dataset was filtered and a subset of the original dataset was created consisting of only the business reviews of the restaurants. with Numpy and sklearn libraries, used vectorization and Countvectorizer to parse through the user reviews and made a list of the possible words to search for in the reviews
- Concluding with the pie chart the majority of reviewers had experience with the chicken dishes. This supports the fact that chicken is the most consumed meat in the US which goes up to 8 billion chickens per year. The chart below also adheres to the fact that burgers and pizza are the top two foods ordered in restaurants. The Indian food reviewers are in less proportion than the population in major cities with restaurants in no more than 5% of the city population

 ![Pie Chart](https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/a3930ef8-4769-4424-becf-3a0d188bfd69)

- created the below bar chart using matplotlib and pyplot. It shows the number of business in a city.
- Philadelphia remains the city with the most businesses with almost 500 businesses in the city, trailed by tucson and tampa with just over 300 businesses. Cherry hill and west chester appear to have the least number of businesses.

![Most_businesses](https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/42931da1-a1c9-43a7-93ca-8b6712f6a6d6)

- The Below line chart shows the number of reviews over the course of time and between 2006 to 2018. It can be seen that till 2007 it appears to have almost zero reviews, a possible reason can be the minimal internet usage by people and fewer influencers.
- Between 2007 to 2010 it seems to start getting reviews to around 250. The reviews start flooding in starting from 2010. Around 2015 it appears to reach a plateau till 2016. The reviews reach it's peak mark of 1600 in around 2017. The reviews start to slowly decline after 2017 till 2018

  ![No_reviews](https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/d86b0fe4-8abf-4071-b513-36dedf5c8735)

- The below bar chart shows the star ratings of the businesses, around 50 businesses got 1 star reviews and over 1000 businesses recieved 4 stars.

![star_rating](https://github.com/LowFasT9/Yelp-Analysis/assets/74370261/fd7d70fe-5574-4599-973a-0cca1e3252f7)
