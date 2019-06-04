### Outline

  * Review of rules of probability
  * likelihood
  * basic likelihood demo
  * likelihood for a hierarchical model demo



<img src="images/by-paul-lewis/pol-probability-0.png"/>



<img src="images/by-paul-lewis/pol-probability-1.png"/>



<img src="images/by-paul-lewis/pol-probability-2.png"/>



<img src="images/by-paul-lewis/pol-probability-3.png"/>



<img src="images/by-paul-lewis/pol-probability-4.png"/>



A disease is found in 8% of the population.
A diagnostic test has a false positive rate of 10%, and
a false negative rate of 5%.
If someone has a positive result, what is the chance that they have the disease?



A disease is found in 8% of the population.
A diagnostic test has a false positive rate of 10%, and
a false negative rate of 5%.
If someone has a positive result, what is the chance that they have the disease?

`\begin{eqnarray}
\Pr(D) & = & 0.08 \\
\Pr(+\mid H) & = & 0.1 \\
\Pr(-\mid D) & = & 0.05 \\
\Pr(D\mid +) & = & ?
\end{eqnarray}`




### Bayes' rule
`\begin{eqnarray}
\Pr(A \mid B) & = &  \frac{\Pr(A, B)}{\Pr(B)}
\end{eqnarray}`
<br />
`\begin{eqnarray}
\Pr(D\mid +)  & = & \frac{\Pr(D,+)}{\Pr(+)} \\
\Pr(+) & = & ?
\end{eqnarray}`




### Law of total probability
`\begin{eqnarray}
\Pr(A) & = & \sum_{i\in\mathcal{B}} {\Pr(A\mid B=i)}{\Pr(B=i)}
\end{eqnarray}`
<br />
`\begin{eqnarray}
\Pr(+) & = & \Pr(+\mid H)\Pr(H) + \Pr(+\mid D)\Pr(D) \\
& = & 0.1\times 0.92 + 0.95\times 0.08 \\
& = & 0.168
\end{eqnarray}`




### Bayes' rule (again)
`\begin{eqnarray}
\Pr(D\mid +)  & = & \frac{\Pr(D,+)}{\Pr(+)} \\
\Pr(+) & = & 0.168 \\
\Pr(D,+) & = & 0.95\times 0.08 = 0.076 \\
\Pr(D\mid +)  & = & 0.076 / 0.168 \\
& = & 0.452
\end{eqnarray}`




<a href="./bayesgraph.html" target="_blank">Bayes' rule graphically</a>




### Bayes' rule
`\begin{eqnarray}
\Pr(D\mid +)  & = & \frac{\Pr(D,+)}{\Pr(+)} \\
\Pr(+) & = & 0.168 \\
\Pr(D,+) & = & 0.95\times 0.08 = 0.076 \\
\Pr(D\mid +)  & = & 0.076 / 0.168 \\
& = & 0.452
\end{eqnarray}`



### Some Common Discrete Probaility Distributions...

(with nice images from the wonderful folks who contribute to Wikipedia)...




If you have *n* trials each which has the same probability of
success (call that *p*), what is the probability of exactly *k* successes?
<br />**Binomial distribution:**
`$$\Pr(k\mid n, p) = {n\choose k} p^k (1-p)^{n-k}$$`
<img src="images/wikimedia/Binomial_distribution_pmf.svg"/>



Imagine you perform independent trials until your first success.
If the probability of a success on each trial is *p*, what is the
probability that the first success will occur on trial *k*? (waiting time=*k* trials)
<br />**Binomial distribution:**
`$$\Pr(k\mid p) = p^k (1-p)^{k-1}$$`
<img src="images/wikimedia/Geometric_pmf.svg"/>



Imagine independent events happen at the same rate *r* over a time
interval of *t*. If `$\lambda = rt$`, what is the probability
that exactly *k* events occur?
<br />**Poisson distribution:**
`$$\Pr(k\mid \lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$$`
<img src="images/wikimedia/Poisson_pmf.svg"/>




For the next set of slides, see 
<a href="./midwest-phylo-likelihood.html">midwest-phylo-likelihood.html</a> ...

