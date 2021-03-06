# ergo_mdp
Ergodic economics simulations using MDP formalisms

# This needs a bit of work, it's still broken

"...Apparently so, but suppose you throw a coin enough times... suppose one day, it lands on its edge."

Legacy of Kain: Soul Reaver II

Episodic MDPs, unlike their non-episodic counterparts, have proven ergodic properties

[Bojun, Huang. "Steady State Analysis of Episodic Reinforcement Learning." Advances in Neural Information Processing Systems 33 (2020).](https://proceedings.neurips.cc//paper/2020/hash/69bfa2aa2b7b139ff581a806abf0a886-Abstract.html)

[Peters, Ole. "The ergodicity problem in economics." Nature Physics 15.12 (2019): 1216-1221.](https://www.nature.com/articles/s41567-019-0732-0)

[Moldovan, Teodor Mihai, and Pieter Abbeel. "Safe exploration in Markov decision processes." Proceedings of the 29th International Coference on International Conference on Machine Learning. 2012.](https://icml.cc/2012/papers/838.pdf)

![\lim_{T \to \inf} \frac{1}{T}\mathop{\mathbb{E}}\sum_{t = 1}^TR(s_t,a_t) = V_\pi(s_0)](https://latex.codecogs.com/svg.latex?%5Clim_%7BT%20%5Cto%20%5Cinf%7D%20%5Cfrac%7B1%7D%7BT%7D%5Csum_%7Bt%20%3D%201%7D%5ETR%28s_t%2Ca_t%29%20%3D%20V_%5Cpi%28s_0%29)

![x' = \left\{ {\begin{array}{*{20}{c}} {x + 0.5x,\quad p = \frac{1}{2}} \\ {x- 0.4x,\quad p = \frac{1}{2}} \end{array}} \right\}](https://latex.codecogs.com/svg.latex?x%27%20%3D%20%5Cleft%5C%7B%20%7B%5Cbegin%7Barray%7D%7B*%7B20%7D%7Bc%7D%7D%20%7Bx%20+%200.5x%2C%5Cquad%20p%20%3D%20%5Cfrac%7B1%7D%7B2%7D%7D%20%5C%5C%20%7Bx-%200.4x%2C%5Cquad%20p%20%3D%20%5Cfrac%7B1%7D%7B2%7D%7D%20%5Cend%7Barray%7D%7D%20%5Cright%5C%7D)


![\lim_{T \to\inf}\frac{1}{T}\mathop{\mathbb{E}}\left[\sum_{t = 1}^TR(s_t,a_t) \right] = V_\pi(s_)](https://latex.codecogs.com/svg.download?%5Clim_%7BT%20%5Cto%20%5Cinf%7D%20%5Cfrac%7B1%7D%7BT%7D%5Cmathop%7B%5Cmathbb%7BE%7D%7D%5Cleft%5B%5Csum_%7Bt%20%3D%201%7D%5ET%20R%28s_t%2Ca_t%29%20%5Cright%20%5D%20%3D%20V_%5Cpi%28s_0%29)

[Taleb's take on this](https://medium.com/incerto/the-logic-of-risk-taking-107bf41029d3)


![\\\\R\left((x,win),null\right) = 0.5x \\R\left((x,lose),null\right) = -0.4x  \\R\left((x,choose),stop\right) = 0  \\\\P((x,win)|(x,choose),play) = 0.5\\P((x,lose)|(x,choose),play) = 0.5\\P((x,stopped)|(x,choose),stop) = 1\\P((x+0.5x,choose)|(x,win),null) = 1\\P((x-04x,choose)|(x,lose),null) = 1\\\\](https://latex.codecogs.com/svg.latex?%5C%5C%20%5C%5CR%5Cleft%28%28x%2Cwin%29%2Cnull%5Cright%29%20%3D%200.5x%20%5C%5C%20R%5Cleft%28%28x%2Close%29%2Cnull%5Cright%29%20%3D%20-0.4x%20%5C%5C%20R%5Cleft%28%28x%2Cchoose%29%2Cstop%5Cright%29%20%3D%200%20%5C%5C%20%5C%5C%20P%28%28x%2Cwin%29%7C%28x%2Cchoose%29%2Cplay%29%20%3D%200.5%5C%5C%20P%28%28x%2Close%29%7C%28x%2Cchoose%29%2Cplay%29%20%3D%200.5%5C%5C%20P%28%28x%2Cstopped%29%7C%28x%2Cchoose%29%2Cstop%29%20%3D%201%5C%5C%20P%28%28x+0.5x%2Cchoose%29%7C%28x%2Cwin%29%2Cnull%29%20%3D%201%5C%5C%20P%28%28x-04x%2Cchoose%29%7C%28x%2Close%29%2Cnull%29%20%3D%201%5C%5C%20%5C%5C)

I would argue that most MDPs of interest are clearly non-ergodic. An MDP combined with a stochastic policy \pi is ergodic if all deterministic policies result in Markov Reward Processes that are ergodic. Almost all RL algorithms assume ergodicity. Value Iteration, the prime one, will just pass back rewards

Equivalently, we can say that an agent with a stochastic policy should be able to visit all states. The problem of ergodicity is that it makes agents overoptimistic, as it kinds of assumes that kinds of possible errors and bad luck are eventually recoverable. If I train as if ergodicity true, a 99% chance of losing everything vs an 1% chance of winning big times will average out, and an agent might actually go for high payout.

To work around the luck of ergodicity we make absorbing states extremely unrewarding. If you break your little toy helicopter you will, you get a massive negative reward. The reward has to be big enough, so that between the choice of getting further away on average and breaking down every so often, breaking down every so often to be considered unacceptable.

Generally, until now, tinkering with the reward function is considered enough. The agent learns to avoid those absorbing states, so that, eventually, the ergodic property is reclaimed.

The problem with this approach is that it's not trivial to model this arbitrary reward functions.

![Percentages of winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist.png?raw=true)

![Wealth of winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist_means.png?raw=true)

![Percentages of winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist_less_rounds.png?raw=true)

![Wealth of winners and losers](https://github.com/ssamot/ergo_mdp/blob/main/plots/hist_means_less_rounds.png?raw=true)

![Tree](https://github.com/ssamot/ergo_mdp/blob/main/plots/tree.png?raw=true)


Well, the model is bonkers. The vast population becomes broke; the probability of being extremely wealthy is less and less (but more wealthy as things move forward). At the very end, because you cannot subdivide an indivudal to fewer than one points and let them have infinite wealth, the whole wealth model collapses.

So what is the
