Life Evolved - An Evolution Simulator
=====================================

Organisms
---------
For simplicity purposes only multicellular Eukaryotes are modelled directly, though the affects of unicellular
Eukaryotes and Prokaryotes may be modelled indirectly e.g. bacterial infections.

Organisms belong to species, and there could be multiple organisms of each species existing at the same time in the
world.

An organism's complexity is described as a function of it's chromosome count, gene count and trait count. More complex
organisms are likely to be more resistant to detrimental mutations due to redundancy in their genotype. Though simpler
organisms will experience more rapid evolution and so may be better suited to coping with changes in their environment.


Species
-------
An organism is considered a new species after a mutation with alters the trait count. This will generate a different
genotype and thus a new species. While this is not the same as real-world classification, this is to allow
easier tracking of phenotype differences.

Species are able to cross-breed, though the offspring may be sterile. If two species can not genetically cross-breed they
are considered to be in separate genera, though physical and geographical variables may prevent species of the same
genera breeding.


Traits, Genes, Chromosomes & Mutations
--------------------------------------
Traits can be affected by any number of genes. Genes are grouped into chromsomes, usually as a chromosome pair (diploid)
represented as a pair of dominant and/or recessive alleles. If two dominant or two recessive alleles of a trait are
combined then the trait is averaged, e.g. red petals + white petals = pink petals.

When an organism spawns a child it's genes are copied into the child. At this stage mutations can occur on genes.

Mutations are expressed as changes to the traits the gene affects, this can be a simple change on a property of a trait.
Additionally, chromosomes can be fused or split to create fewer or more total chromosomes. In these occurences the traits
do not change in number and all the same information is available. However over time these different chromosomes will
continue to mutate and drive speciation.

If two organisms with differing numbers of chromosomes mix, the female's (F) chromosomes are preferred over the males (M).
For example:

- F(14) + M(15) = O(14)
- F(15) + M(14) = O(15)

Though there will be incomplete chromosomes leading to loss of traits. The survival of the offspring depends on how
vital these traits were.

Chromosomes are paired by their gene index, this is the ordered list of genes in the chromosome. If fusion or fission
has created differing keys the chromosomes will not match.


Components
----------
Components are the parts that make up an organism. An organism can consist of any number of components.

### Organs
An organ is any component that performs an involuntary function, for example a plant's stem or an animal's eye.

### Appendage
An appendage is any component that performs a voluntary function or none at all.


Data Format
-----------
Data is saved in `json` format.

The data consists of `genepool`, `species` and `organisms`.