# Reading list essentials

1. [Basset (Kelley et al. 2016)](https://genome.cshlp.org/content/26/7/990.long)

   This is one of the first S2F models predicting **DNase-seq** signal to determine sequence determinants of open chromatin

2. [DeepSEA (Zhou et al. 2015)](https://www.nature.com/articles/nmeth.3547)

   This model predicts **DNase-seq**, **Histone marks**, and **TF binding**

3. [Expecto (Zhou et al. 2018)](https://www.nature.com/articles/s41588-018-0160-6)

   This model predicts **chromatin signal** and **histone marks**, and **TF binding** to predict **gene expression** from the predicted regulatory signal with a linear transformation. 

4. [DeepBind (Alipanahi et al. 2015)](https://www.nature.com/articles/nbt.3300)

   This model predicts TF and RBP binding from ChIP-, CLIP-seq, SELEX, and Protein binding microarray (PBM) data

5. [SpliceAI (Jaganathan 2019)](https://doi.org/10.1016/j.cell.2018.12.015)

   This model predicts splice junctions

6. [Enformer (Avsec et al. 2021)](https://www.nature.com/articles/s41592-021-01252-x)

   This model predicts the signal from over 5,000 experiments from ENCODE for human and mouse, i.e. Histone marks, TF binding, CAGE-seq, 

7. [Borzoi (Linder et al. 2025)](https://www.nature.com/articles/s41588-024-02053-6)

   Successor of Enformer

8. [AlphaGenome (Avsec et al. 2025, DeepMind)](https://storage.googleapis.com/deepmind-media/papers/alphagenome.pdf)

   Successor of Borzoi

9. [BpNet (Avsec et al. 2021)](https://www.nature.com/articles/s41588-021-00782-6)

   Model that predicts ChIPnexus profiles at base-pair resolution to understand intricate TF binding syntax

10. [ChromBpNet (Pampari 2025)](https://www.biorxiv.org/content/10.1101/2024.12.25.630221v2)

    Successor of BPnet that predicts ATAC-seq profiles at base-pair resolution to understand intricate TF binding syntax leading to chromatin regulation

11. [Decima (Lal et al. 2025)](https://www.biorxiv.org/content/10.1101/2024.10.09.617507v3)

    One of the latest models that use transfer learning to predict scRNA-seq from large sequence windows

12. [Yeast Promoter MPRA model (Vaishnav et al. 2022)](https://www.nature.com/articles/s41586-022-04506-6)

    The model was trained on 1 million random yeast promoter sequences using an Massively Parallel Reporter Assay (MPRA) of expression of yellow fluorescent protein (YFP)

13. [Saluki (Agarwal et al. 2022)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02811-x)

    Predicts **mRNA decay rates** across different cell types collected from pulse labeling-based methods

14. [Puffin (Dudnyk et al. 2024)](https://www.science.org/doi/10.1126/science.adj0116)

    Predicts CAGE, GRO-cap, and PRO-cap profiles at transcription start sites to understand transcription initiation

15. [DeepSTARR (de Almeida et al. 2022)](https://www.nature.com/articles/s41588-022-01048-5)

    Enhancer syntax from STARR-seq MRPA for prediction and design

16. [APARENT (Linder et al. 2019)](https://www.cell.com/cell/fulltext/S0092-8674(19)30498-2)

    Predicting **Alternative Poly-Adenylation** site usage and design with the model