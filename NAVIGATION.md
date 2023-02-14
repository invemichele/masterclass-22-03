# Masterclass 22.03: Rethinking Metadynamics: the On-the-fly Probability Enhanced Sampling (OPES) method

This lesson was given as part of the PLUMED masterclass series in 2022.  It includes:

* Two videos that describe the theory. 
* A series of exercises for you to complete.
* A python notebook that contains a full solution to the exercises.

The flow chart shown below indicates the order in which you should consult the resources.  You can click on the nodes to access the various resources.  Follow the thick black lines for the best results.  The resources that are connected by dashed lines are supplmentary resources that you may find useful when completing the exercise.

This lesson was the third masterclass in the 2022 series.

```mermaid
flowchart TB;
  A[ref1] -.-> G[Lecture I];
  B[ref2] -.-> G;
  C[ref3] -.-> G;
  D[ref4] -.-> G;
  E[ref5] -.-> G;
  F[ref6] -.-> G;
  A -.-> H[Slides];
  B -.-> H;
  C -.-> H;
  D -.-> H;
  E -.-> H;
  F -.-> H;
  G ==> J[Instructions];
  I[theory I] -.-> J;
  K[theory II] -.-> J;
  H ==> J;
  J ==> L[Lecture II];
  L ==> M[Solutions I];
  L ==> N[Solutions II];
  click A "ref1" "A previous tutorial that introduces the basics of PLUMED syntax";
  click B "ref2" "A previous tutorial that introduces umbrella sampling";
  click C "ref3" "A previous tutorial that introduces metadynamics";
  click D "ref4" "A paper on the OPES method";
  click E "ref5" "Another paper on the OPES method";
  click F "ref6" "Yet another paper on the OPES method"; 
  click G "video1" "A lecture that was given on February 28th 2022 as part of the plumed masterclass series that introduces you to the exercises in this lesson";
  click H "ref7" "The slides that were used in the lecture";
  click I "THEORY.md" "An introduction to the theory";
  click J "INSTRUCTIONS.md" "Instructions for the exercises that you are supposed to complete";
  click K "MORE_THEORY.md" "Some more theoretical details";
  click L "video2" "A lecture that was given on March 7th 2022 as part of the plumed masterclass series that goes through the solutions to the exercises in the lesson";
  click M "notebooks/1-opes_expanded.ipynb" "A python notebook where the answers to the exericses are discussed";
  click N "notebooks/2-opes_metad.ipynb" "A python notebook where the answers to the exercises are discussed";
```
