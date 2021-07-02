# Election analysis

## Overview of Election Audit

  The purpose of this analysis is to detemine the outcome of the elections based on data collected from over 300,000 votes from different counties to know which candidate was the the winner by number of votes and percentage of total votes.

## Election-Audit Results

The results of the election are summarized in the image below:

![Command line result](https://user-images.githubusercontent.com/83261520/124203323-106bf600-daa2-11eb-9373-df51375f7714.png)

***Election Results***
- How many votes were cast in this congressional election?

The total number of votes were: 369,711. 

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

The number of votes from each county from lowest to highest are: Araphoe with 24,801 votes which represetns 6.7% of the total number of votes, Jefferson with 38,855 votes which represents 10.5% of the total number of votes and lastly Denver with 306,055 votes which is 82.8% of the total number of votes.

- Which county had the largest number of votes?

The county with the largest number of votes was Denver.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

There were 3 candidates running on this election, the outcome was the following: In 3rd place with 11,606 votes (3.1%) is Raymon Anthoiny Doane, in 2nd place with 85,213 votes (23.0%) is Charles Casper Stockham and in 1st place with 272,892 votes (73.8%) is Diana DeGette

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The winner of this election was Diana DeGette with a total of 272,892 votes which represents the 73.8% of the total number of votes.


## Election-Audit Summary

This script can be modified to analyse the results of elections that take place not only on the precint but also on the rest of the state or even nationwide.
To achieve such thing the script has to be modified and also the information given (csv) has to include additional data.

For example if we wanted to analyse the results of the elections from the other disctricts in the state and by party we will need to have the information of the number of districts in the state and also the party from wich the canddidate belongs and the information given throu the csv would have to be delivered in the following way: **Ballot ID, County, Candidate,** ***District number, Party*** 

From there the script will be modified to create new dicctionaries and indexes in addition to new loops to get the results for each district and party, that way we could know wich party has more districts an therefore know which party "controls" the state.


