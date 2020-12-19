# Slowest Fastest

> Points: 457 [500]

## Description

> Hey, we've got a problem at the factory! As you well know we have N rooms in our factory, and in the i-th room we have v[i] gifts that have to be built.
> Also, at the factory we have N mechagnomes of two possible types:
>         K of them are the Fast-O-Bot type, which can build P gifts in a single day
>         The rest of N - K bots are the Speed-O-Tron type which can build Q gifts in a single day.
> Each day a mechagnome is assigned to a room, and that day it'll work all by itself in that room, building as many gifts as it can.
> If there are no gifts to be built or he finishes all of them before the end of the day, the mechagnome goes idle. There cannot be two mechagnomes in the same room in the same day.
> Since we're in a hurry, we need the minimum number of days we can build all gifts. Can you help us?
> Just to be safe, we have to solve 100 such scenarios. We don't want to waste any time so we'll give you 60 seconds to solve everything.
> Ah, and since our connection is so slow, we'll define v in the following way: v[i] = (a * v[i - 1] + c) % mod for all i = 2, n

## Solution

This was interesting problem that I have somewhat stumbled before in the past. The ideal algorithm is somewhat similar to the one in this [geeksforgeeks article](https://www.geeksforgeeks.org/find-minimum-time-to-finish-all-jobs-with-given-constraints/), which was to find the minimum amount of time to finish all jobs with the given constraints.

The algorithm takes a rather interesting approach. Rather than sorting the array at each iteration to find the smallest few elements, it would use binary search to find the number of days, and checks whether it is possible, then determine whether to increase or decrease the number days. This essentially sped up the solving to reach a O(logn) solution.

** PS: I did not manage to implement this during the competition as I was too caught up on other challenges. I only implemented the naive solution which only got me to test 16/100 :(

## Flag
`X-MAS{}`