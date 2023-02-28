# Masterclass 22.03: Rethinking Metadynamics: the On-the-fly Probability Enhanced Sampling (OPES) method

This lesson was given as part of the PLUMED masterclass series in 2022.  It includes:

* Two videos, one about the theory and one about the exercises.
* A series of exercises for you to complete.
* Two python notebooks that contain the full solutions to the exercises.

The flow chart shown below indicates the order in which you should consult the resources.  You can click on the nodes to access the various resources.  Follow the thick black lines for the best results.  The resources that are connected by dashed lines are supplmentary resources that you may find useful when completing the exercise.

This lesson was the third masterclass in the 2022 series.

```mermaid
flowchart TB;
  A[Umbrella Sampling] -.-> C[Lecture I];
  B[ref2] -.-> C;
  C ==> D[Instructions];
  E[Slides] ==> D;
  F[Theory] -.-> D;
  D ==> G[Solutions OPES_EXPANDED];
  D ==> H[Solutions OPES_METAD];
  G ==> I[Lecture II];
  H ==> I[Lecture II];
  click A "ref1" "A previous tutorial that introduces umbrella sampling";
  click B "ref2" "A previous tutorial that introduces metadynamics";
  click C "video1" "A lecture that was given on February 28th 2022 as part of the plumed masterclass series that introduces you to the exercises in this lesson";
  click D "INSTRUCTIONS.md" "Instructions for the exercises that you are supposed to complete";
  click E "ref3" "The slides that were used in the lecture";
  click F "THEORY.md" "An introduction to the OPES theory";
  click G "notebooks/1-opes_expanded.ipynb" "A python notebook that presents the OPES method for replica-exchange-like sampling";
  click H "notebooks/2-opes_metad.ipynb" "A python notebook that presents the OPES method for metadynamics-like sampling";
  click I "video2" "A lecture that was given on March 7th 2022 as part of the plumed masterclass series that goes through the solutions to the exercises in the lesson";
```

## References
1. [Unified Approach to Enhanced Sampling](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.10.041034)
2. [Rethinking Metadynamics: From Bias Potentials to Probability Distributions](https://pubs.acs.org/doi/10.1021/acs.jpclett.0c00497)
3. [Exploration vs Convergence Speed in Adaptive-Bias Enhanced Sampling](https://pubs.acs.org/doi/10.1021/acs.jctc.2c00152)

