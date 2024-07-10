# Anti-conformists catalyze societal transitions and facilitate the expression of evolving preferences

This repository contains Python code for ABM simulations of collective decision-making dynamics in heterogeneous populations with (evolving) preferences and differing conforming tendencies on networks. The code implements a model where individuals make choices influenced by their preferences and the choices of their neighbors in a network. 

## Abstract
The world is grappling with emerging, urgent, large-scale problems such as climate change, pollution, biodiversity loss, and pandemics, which demand immediate and coordinated action. Social processes like conformity and social norms can either help maintain behaviors (e.g., cooperation in groups) or drive rapid societal change (e.g., rapid rooftop solar uptake), even without comprehensive policy measures. 
While the role of individual heterogeneity in such processes is well-studied, there is limited work on the expression of individuals’ preferences and the role of anti-conformists---individuals who value acting differently from others---especially in dynamic environments. We introduce anti-conformists into a game-theoretical collective decision-making framework that includes a complex network of agents with heterogeneous preferences about two alternative options. We study how anti-conformists’ presence changes the population’s ability to express evolving personal preferences. We find that anti-conformists facilitate the expression of preferences, even when they diverge from prevailing norms, breaking the “spiral of silence” whereby individuals do not act on their preferences when they believe others disapprove. Centrally placed anti-conformists reduce by 5-fold the number of anti-conformists needed for a population to express its preferences. In dynamic environments where a previously unpopular choice becomes preferred, anti-conformists catalyze social tipping and reduce the ‘cultural lag,’ even beyond the role of committed minorities---that is, individuals with a commitment to a specific cause. This research highlights the role of dissenting voices in shaping collective behavior, including their potential to catalyze the adoption of new technologies as they become favorable and to enrich democracy by facilitating the expression of views.

## Code Overview

The repository includes the following Python scripts:

1. `one_run_network.py`: This script simulates population dynamics with heterogenous preferences on networks. It implements a model where individuals update their choices based on their preferences and the choices of their neighbors on a fixed graph.

2. `one_run_well_mixed.py`: This script simulates population dynamics with heterogenous preferences connected probabilistically, mimicking a well-mixed limit. It models a scenario where individuals' choices are influenced by their preferences, the choices of randomly sampled neighbors.

3. `one_run_net_dynamic.py`: This script simulates population dynamics with evolving preferences on networks. It implements a model where individuals update their choices based on their evolving preferences (which are shared by all agents) and the choices of their neighbors on a fixed graph.

4. `adjacency_matrix_generator.py`: This function returns the adjacency matrix of the required graph (Barabasi-Albert or Erdos Renyi)

5. `conformity_placement_on_network.py`: This function assigns conformity to the nodes of a given network to achieve the required correlation between anti-conformity(non-conformity) and node degree.

6. `Manuscript_figures.ipynb`: This notebook can be used to generate figures from the main text. This notebook uses the above scripts to initialize and run simulations.

## Usage

To use the code:

1. Ensure you have Python installed on your system.
2. These scripts are completely based on Numpy. 


## Output of simulation scripts

`one_run_network.py` and `one_run_well_mixed.py` have the following output:

- Equilibrium fraction of choice A in the population
- Equilibrium alignment of choice and preference for the entire population.
- Volatility in choices at the end of the simulation

  
`one_run_net_dynamic.py` has the following output: 

- Time series of the fraction of individuals choosing option A in the conforming and the anti-conforming subpopulations, as well as the entire population.
- Average alignment of choice and preference for the conforming and the anti-conforming subpopulations.

## License

This GUI is distributed under the Creative Commons Attribution 4.0 International license. The DOI of the project is https://doi.org/10.5281/zenodo.12707358


## Acknowledgments

This code was developed by Dhruv Mittal.
