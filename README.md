# eloF1

eloF1 is a simple engine designed to compute [ELO ratings](https://youtu.be/AsYfbmp0To0) for Formula 1 drivers. A substantial portion of the code is adapted from the [F1 bot](https://github.com/Shuvam586/F1-Bot).

All drivers start with a base rating of 1000, and each driver is associated with an average race finish position.

A driver's rating changes after each race using the following equation. 

```Δrating = 100 * ( raceFinishCoeff - avgFinishCoeff)```

The original equation multiplies the difference by a factor of 32. 32 is a bit too less for my liking tho. ;)

`raceFinishCoeff` and `avgFinishCoeff` are defined as:

```raceFinishCoeff = 1 - ( finishingPosition / totalEntrants )```

`avgFinishCoeff` is given as the mean of `raceFinishCoeffs` from all the races the driver has entered.

I havent figured out how to plot graphs just yet. Also, this is NOT a perfect implementation of the [ELO Rating System](https://en.wikipedia.org/wiki/Elo_rating_system).
