# A lower bound of 3.671741 for the random 3-SAT threshold

**Fedor Vorobyev — technical note, version 1.2, 7 October 2026.**

**[Read the PDF](note.pdf)** · [LaTeX source](note.tex) · [Exact arithmetic checker](certify_3671741.py)

This note deduces

$$
\alpha_3\ge\inf_{0\le x<1}\frac{4(1-x+x\log x)}{(1-x)^3}>3.671741,
\qquad 0\log0=0.
$$

The variational constant, approximately 3.671741106632344, comes from the earlier spatial-coupling work of Achlioptas, Hassani, Macris, and Urbanke. The contribution of the note is its transfer to the **exact satisfiability threshold**, using Proposition 4.6 of OpenAI's *Computing the Random 3-SAT Threshold*.

Writing A for this variational constant, spatial coupling gives zero limiting minimum violation density below A. The new proposition gives a positive linear number of unavoidable violations above the exact threshold. A density strictly between the two thresholds would contradict both statements. The note provides the clause-model transfers and an exact rational certificate for the displayed decimal bound.

Together with the separate [4.268 upper-bound result](https://github.com/yamelton/sat-upper-4268), this gives **3.671741 < α₃ ≤ 4.268**. The upper bound is not an input to the lower-bound proof.

The [cavity-method prediction](https://arxiv.org/abs/cs/0309020) is approximately **4.267**. The lower bound remains about **0.60 clauses per variable below that prediction**, leaving a substantial gap.

## Verification

Run the scalar certificate using Python 3 and its standard library:

```sh
python3 certify_3671741.py
```

Successful output has `"status": "PASS"`. Every proof comparison uses exact rational arithmetic. Decimal diagnostic values are not used in any proof decision. The recorded output is [certificate.json](certificate.json).

To rebuild the PDF with a standard LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The checker establishes the scalar inequality only. The probabilistic theorems are external inputs, and the complete deduction is not formalized in Lean. Language models assisted with the research, checking, code, and writing; the note describes that assistance. Separate model checks are not independent human peer review.

## Mathematical sources

1. **D. Achlioptas, S. H. Hassani, N. Macris, R. Urbanke.** *Bounds for Random Constraint Satisfaction Problems via Spatial Coupling*. SODA 2016, pp. 469–479. [Published paper](https://doi.org/10.1137/1.9781611974331.ch35), [full author manuscript](https://di.uoa.gr/~optas/papers/spatial.pdf). Theorem 4 and equations (90), (92) in the appended full version supply the rough/MAX-SAT bound.
2. **S. H. Hassani, N. Macris, R. Urbanke.** *Threshold Saturation in Spatially Coupled Constraint Satisfaction Problems*. Journal of Statistical Physics 150 (2013), pp. 807–850. [arXiv:1112.6320v2](https://arxiv.org/abs/1112.6320v2). Theorems 1–2 supply the limiting energy comparison.
3. **OpenAI.** *Computing the Random 3-SAT Threshold*, preprint dated 27 September 2026. [Pinned manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf). Theorem 4.4 identifies the threshold across models; Proposition 4.6 gives linear violation robustness.
4. **G. Carenini.** *A polynomial scaling window for random k-SAT and a proof of the satisfiability conjecture*. [ECCC TR26-229](https://eccc.weizmann.ac.il/report/2026/229/), 5 October 2026. Cited for threshold existence and its priority.
5. **S. Mertens, M. Mézard, R. Zecchina.** *Threshold values of random K-SAT from the cavity method*. Random Structures & Algorithms 28(3) (2006), pp. 340–373. [arXiv:cs/0309020](https://arxiv.org/abs/cs/0309020). Source of the predicted value near 4.267.
6. **F. Vorobyev.** *A direct proof of convergence of the random k-SAT threshold*, draft, 7 October 2026. [Repository](https://github.com/yamelton/sat-constant-threshold). Theorem 1.1 gives a later independent proof of threshold existence, following the results of Carenini and OpenAI. The lower-bound argument here uses OpenAI's violation-robustness theorem.

[Source provenance](source_provenance.json) records the OpenAI commit and hashes of source files consulted. Source manuscripts are not redistributed here.

## Citation

```bibtex
@misc{vorobyev2026satlower,
  author = {Fedor Vorobyev},
  title = {A lower bound of 3.671741 for the random 3-SAT threshold},
  year = {2026},
  month = oct,
  note = {Technical note, version 1.2},
  url = {https://github.com/yamelton/sat-lower-3671741}
}
```
