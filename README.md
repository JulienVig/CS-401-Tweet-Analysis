# Detecting Chilling Effects due to Online Surveillance through Tweets
## Abstract  
The paper we studied tried to detect Chilling Effects related to online surveillance by studying Wikipedia use. More precisely pageviews from specific privacy-sensitive keywords. We would like to extend this analysis to a different part of the Internet, namely the social network Twitter, and check if the results that were found on Wikipedia pageviews also apply there. Analyzing a social network may lead to some new insights as users may represent a different population from Wikipedia. Moreover users express their opinion through tweets and that is tightly linked to the free speech right, and so to a potential chilling effect. The reason we chose Twitter is because Tweets are a public form of Internet use that private Wikipedia searches, so users might think more carefully about what they express there. But at the same time it is completely legal to use those words in public so reservations that users may have to talk about these subjects are more likely due to a chilling effect, in other words to a feeling that the state might not protect their rights correctly.
To conduct this extension, we propose to use a new dataset that we will collect ourselves of all tweets containing one of the keywords from the list used in the paper. The time-frame will also be the same as the paper (January 2012 to August 2014) to get comparable results.

## Research Questions  
* Can we observe an immediate drop in Tweets on privacy-sensistive subjects after the Snowden revelations?
* Can we detect a long-lasting Chlling Effect on Twitter after the Snowden revelations?
* Is the Snowden revelations' effect significantly different on Twitter and Wikipedia?

## Proposed dataset  
For this extension, we will create our own dataset using both the [Twitter API](https://developer.twitter.com/en/docs/twitter-api) and the [Twint library](https://github.com/twintproject/twint). For the time period we are interested in, we will collect all Tweets containing one of the keywords from the U.S. Department of Homeland Security's list that is used in the paper such as "Al Qaeda" or "Terrorism. And at the same time, we will collect Tweets for some non-sensitive security-related keywords to have a basis for comparison with subjects that should not be affected by Chilling Effects. Finally we will also compare with the total number of Tweets per day over that period to analyse our results with respect to the general trend.

Here are some Tweets containing the word "Al-qaeda" that were scraped using Twint:
|id|conversation_id|created_at|date|time|timezone|user_id|username|name|place|tweet|language|mentions|urls|photos|replies_count|retweets_count|likes_count|hashtags|cashtags|link|retweet|quote_url|video|thumbnail|near|geo|source|user_rt_id|user_rt|retweet_id|reply_to|retweet_date|translate|trans_src|trans_dest|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: 
|494993531665014785|494993531665014785|2014-08-01 01:50:29 CEST|2014-08-01|01:50:29|+0100|24073158|harbert|Charles Harbert||Is this really a good idea to fly #Ebola infected humans back into the US? Who is making these decisions.... Al-Qaeda?|en||||0|0|0|['ebola']||https://twitter.com/Harbert/status/494993531665014785|False||0||||||||||||
|494992277618434049|494992277618434049|2014-08-01 01:45:30 CEST|2014-08-01|01:45:30|+0100|98233607|lobo823|Whiskey Rider||Al-Qaeda Has Received $125 Million In Ransom From Europe Since 2008  http://t.co/LC0CAApwE9 via @DailyCaller|en|"[{'screen_name': 'dailycaller','name': 'daily caller', 'id': '39308549'}]"|['http://dailycaller.com/2014/07/30/al-qaeda-has-received-125-million-in-ransom-from-europe-since-2008/']||0|0|0|||https://twitter.com/Lobo823/status/494992277618434049|False||0||||||||||||
|494991753502789632|494991753502789632|2014-08-01 01:43:25 CEST|2014-08-01|01:43:25|+0100|17027095|andrebranun|𝕋𝕠𝕞𝕞𝕪 𝕃𝕖𝕖 ℝô𝕝𝕒™||"Já tem o Califado no Iraque, agora um grupo ligado à Al-Qaeda decretou um Emirado Islâmico na Líbia.  http://t.co/jTIKqMiCZU"|pt||['http://ln.is/uol.com.br/DNq9o']||0|0|0|||https://twitter.com/andrebranun/status/494991753502789632|False||0||||||||||||
|494991555611336704|494986152718258176|2014-08-01 01:42:38 CEST|2014-08-01|01:42:38|+0100|27947724|bcwestmind|ArmandRichelieuofPoitou||"@TheTorontoSun @kinsellawarren #cdnpoli I'll say. Most don't know diff b/w Taliban/al-qaeda/jihadists/Saddam, war on terror fog reigns."|en|"[{'screen_name': 'kinsellawarren, 'name': 'warren kinsella', 'id': '16106522'}]"|||0|0|0|['cdnpoli']||https://twitter.com/bcwestmind/status/494991555611336704|False||0||||||||||||


## Methods  
We will try and replicate the analyses that were conducted in the paper on our new dataset, especially the Iterrupted Time Series analysis. Then we will be able to say if we get similar results than with Wikipedia and try to interpret the similarities and differences. In order to add some value to our analysis, we can leverage the different format of data that we have (text compared to pageviews). We will be able to perform some NLP on the Tweets (e.g., sentiment analysis) to assess if there is a chilling effect from a different perspective. For instance, the number of tweets may not decrease suddenly but opinions expressed may change and align with the government's ideas. 

## Organization within the team  
List of internal milestones :
- [x] 1/12 : Dataset has been collected and is ready for exploration (@Julien_Ben)
- [x] 5/12 : Data has been cleaned and explored to make sure there are no anomalies (@JulienVig, @hugolepeytre)
- [x] 9/12 : Rough analysis has been conducted and we have an idea of the final results (individually followed by a brainstorm) 
- [x] 13/12 : Analysis is finished, we know the results and only have to present them (@JulienVig)
- [x] 16/12 : Report is ready, results are presented in a clear and organized way (@Julien_Ben, @hugolepeytre)
- [ ] 18/12 : Submission date
