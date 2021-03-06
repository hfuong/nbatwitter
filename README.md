# NBA Twitter

## Objective
**Goal:** Scrape followers and tweets from the official Twitter accounts of current NBA players to identify which other current NBA players they interact with and whether these interactions are consistent with current/past teams.

**Questions:**  
1. Do all NBA players follow each other? If not, are there certain clusters of players?
2. Who do current NBA players interact with most?  
3. Is there a clustering of interactions within teams or among certain players?  
4. Do certain players act as an in-between or connection to other players?  


## To-do list  
- [x] Obtain a list of current NBA players and their Twitter handles  
  - [x] Use [Basketball Reference](https://www.basketball-reference.com/friv/twitter.html) to obtain list of all NBA players and their Twitter handles  
  - [x] Use the official site for the [NBA](https://nba.com/players/) to obtain a list of all active players 
  - [x] Compare list of all NBA Twitter handles and list of active players to compile a list where they overlap 
- [x] Remove Twitter screen names (handles) that do not exist
- [x] Scrape followers/friendships from current NBA players to identify a basic network
- [x] Produce edge lists based on followers to calculate the social network position of each player  
- [ ] Scrape tweets (mentions/tags, retweets, likes) from current NBA players to identify interactions  
- [ ] Produce social networks using Twitter interactions  
- [ ] Use social network metrics to identify possible trends by teams or players  

## Bugs to fix: 
- [ ] Names with accents not listed in currenttwitter.csv
- [ ] Check errors from followers.csv (nonexistent screen names still searched, some pairs didn't search)
