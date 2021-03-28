# ergo_mdp
Ergodic economics simulations using MDP formalisms

![\lim_{T \to \inf} \frac{1}{T}\sum_{0}^TR_\pi(s,s') = \sum_{s,s' \in S}P(s,s')R(s,s')\pi(s,s')](https://latex.codecogs.com/svg.latex?%5Clim_%7BT%20%5Cto%20%5Cinf%7D%20%5Cfrac%7B1%7D%7BT%7D%5Csum_%7B0%7D%5ETR_%5Cpi%28s%2Cs%27%29%20%3D%20%5Csum_%7Bs%2Cs%27%20%5Cin%20S%7DP%28s%2Cs%27%29R%28s%2Cs%27%29%5Cpi%28s%2Cs%27%29)

![{{R(s,s')} = \left\{ {\begin{array}{*{20}{c}} {0.5s,\quad P_{s,s_h'} = \frac{1}{2}} \\ {- 0.4s,\quad P_{s,s_t'} = \frac{1}{2}} \end{array}} \right.](https://latex.codecogs.com/svg.latex?%7BR%28s%2Cs%27%29%7D%20%3D%20%5Cleft%5C%7B%20%7B%5Cbegin%7Barray%7D%7B*%7B20%7D%7Bc%7D%7D%20%7B0.5s%2C%5Cquad%20P_%7Bs%2Cs_h%27%7D%20%3D%20%5Cfrac%7B1%7D%7B2%7D%7D%20%5C%5C%20%7B-%200.4s%2C%5Cquad%20P_%7Bs%2Cs_t%27%7D%20%3D%20%5Cfrac%7B1%7D%7B2%7D%7D%20%5Cend%7Barray%7D%7D%20%5Cright.)

![Percentages of winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist.png?raw=true)

![Money made by winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist_means.png?raw=true)
