# McHacks9 - RailVision Project

This repository contains the code for the data analysis and the CSV generation. The visualization tool is not in this repo, but is available upon further request.

![](Dragster.jpg)


## Inspiration
After years of taking the STM and having one too many experiences of waiting in the freezing weather for a bus that would never come, the problem proposed by the RailVision challenge was one that was close to our hearts. Having a better organized public transit system and minimizing wait times are keys to a better and greener future in the transportation world.

## What it does
Long gone are the days where, after running — no, sprinting — from your bus stop to metro station, only to find out that you just missed it and that the next one is 30 minutes away.  _Bummer._ With our project solution, this situation will (hopefully) be left in the past!
Given a database with times that passengers arrive at each station, using a local beam search heuristic, our code finds the optimal time to deploy the trains such that the average wait time for each passenger is minimized. Then the solution can be visualized  through an animation which displays each train and station and concisely shows the time, number of passengers and other relevant information. 

## How we built it
The first step we took to better understand the challenge domain was to think about additional constraints, namely the start times for the first and last train routes. Furthermore, there were better starting times than others (e.g. ending with 7 or 8) that allowed us to "time" the trains' arrival at a station with those of the passengers. These heuristics helped us form a good first "guess", which we would later use to find an optimal one. But before that, we coded a helper function that computed the wait time of the passengers. This function is crucial to solving the problem, as it is what we are trying to minimize. The optimization code was built using python and a variation on a genetic search algorithm. At each iteration, we generate k slightly differing train schedules using our input one, and keeping the n most optimal. After a number of iterations, we return the converged result.

## Challenges we ran into
At first, it was difficult to figure out how to go about this problem since there are so many varying factors we needed to take into account. At first, we contemplated using other algorithms such as network flows or an instance of dynamic programming. We decided to go with an AI based search because with a good enough tentative schedule and enough iterations, then with an optimization algorithm, we would eventually converge to a point that minimizes the average wait times. Another challenge was coding the optimization, as libraries like numpy/scipy did not behave the way we wanted them to (e.g. not returning integer values). 
Despite the logic behind the challenge itself that had to be tested via different algorithms, designing such systems can be tricky as well. It was important to spend the first few hours understanding what exactly we're trying to achieve as well as checking similar products and interfaces to design something "intuitive" and "straightforward" so we can represent to any kind of user. 
On the visualization side, there were a good amount of issues. We initially decided to code the project in JS using React. However, after many hours of development, this turned to be problematic due to the complexity of the visualization and the multiple different instances of objects spawning at different times. In the end, we chose to use a more flexible and robust software to develop these almost game-like visualization:  Unity.  While needing to essentially restart, it was very worth-while.


_Finally, the consequences of sleep-deprivation might be apparent, as I forgot to save this draft the first time I wrote it, which makes me very sad._

## Accomplishments that we're proud of
After all the efforts poured into this and great team work we had, it was nice to piece the code together to see it running and successfully finding solutions that were considerably better than what we had found by hand. 
Learning how to work effectively as a team might be undoubtedly the most vital accomplishment for all of us. Joining as total strangers and ending up working through the same vision is something I'm truly proud of.

## What we learned
**Teamwork makes the dream work!**
Collaboration was crucial to allow the progress of this challenge. We all had different strengths that complemented each other. Everybody pulling their own weight ensured that no one broke their back having to carry all the load!
As this was my very first hackathon and it happened to be online, I managed to learn as much as I could. One of the most important things that I learned was the importance of Networking. Trying to match with other students and finding a team based on a different skill set was one of the challenges. Breaking down the problem, brainstorming with team members, and defining our roles was the other challenge I faced throughout the hackathon. 


## What's next for RailVision 
With our proposed solution, the next words you will hear from the STM lady will be:
_"Prochaine station, RailVision!"_


