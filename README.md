# Detecting Chilling Effects due to Online Surveillance through Tweets
## Abstract  
The paper we studied tried to detect Chilling Effects related to online surveillance by studying Wikipedia use. More precisely pageviews from specific privacy-sensitive keywords. We would like to extend this analysis to a different part of the Internet, namely the social network Twitter, and check if the results that were found on Wikipedia pageviews also apply there. Analyzing a social network may lead to some new insights as users may represent a different population from Wikipedia. Moreover users express their opinion through tweets and that is tightly linked to the free speech right, and so to a potential chilling effect. The reason we chose Twitter is because Tweets are a public form of Internet use that private Wikipedia searches, so users might think more carefully about what they express there. But at the same time it is completely legal to use those words in public so reservations that users may have to talk about these subjects are more likely due to a chilling effect, in other words to a feeling that the state might not protect their rights correctly.
To conduct this extension, we propose to use a new dataset that we will collect ourselves of all tweets containing one of the keywords from the list used in the paper. The time-frame will also be the same as the paper (January 2012 to August 2014) to get comparable results.

## Research Questions  
Can we observe an immediate drop in Tweets on privacy-sensistive subjects after the Snowden revelations?
Can we detect a long-lasting Chlling Effect on Twitter after the Snowden revelations?

## Proposed dataset  
For this extension, we will create our own dataset using the TODO Twitter API, which allows us to scrape every Tweet without limitations on the publication date. For the time period we are interested in, we will collect all Tweets containing one of the keywords from the U.S. Department of Homeland Security's list (the one that is also used in the paper). And at the same time, we will collect a sample of random Tweets for some non-sensitive keywords to have a basis for comparison with subjects that should not be affected by Chilling Effects. And finally we will also compare with the total number of Tweets over that period to get an idea of the general trend in Twitter use over that period.
## Methods  
We will try and replicate the analyses that were conducted in the paper on our new dataset, especially the Iterrupted Time Series analysis. Then we will be able to say if we get similar results than with Wikipedia and try to interpret the similarities and differences.
## Organization within the team  
List of internal milestones :
- [ ] 1/12 : Dataset has been collected and is ready for exploration
- [ ] 5/12 : Data has been cleaned and explored to make sure there are no anomalies
- [ ] 9/12 : Rough analysis has been conducted and we have an idea of the final results
- [ ] 13/12 : Analysis is finished, we know the results and only have to present them
- [ ] 16/12 : Report is ready, results are presented in a clear and organized way
- [ ] 18/12 : Submission date
