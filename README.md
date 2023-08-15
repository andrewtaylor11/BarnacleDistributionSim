# BarnacleDistributionSim
A generative algorithm to model the influence of barnacle basal width on population density, with no other factors considered.
To model the distribution of barnacles, a 10cm x 10cm square was simulated and partitioned into 0.1cm x 0.1cm squares, with circles of specified diameter range being placed on each grid vertex in a random order. Collision detection was used to avoid overlap of circles, and 16 iterations were undertaken to maximize space filling. Size and placement data was exported as a CSV file and analyzed to provide density and average diameter information.
<figure>
  <img width="637" alt="Sample output" src="https://github.com/andrewtaylor11/BarnacleDistributionSim/assets/103282704/85820173-8ac9-4846-9920-44c732c6a5c3">
<br>
  <figcaption>Figure 1: Sample output of barnacle distribution simulation, with circle radii ranging from 0.08cm to 0.22cm.</figcaption>
</figure>
<br>
