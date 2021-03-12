# Annotation Readme

## The process (with links)

**Code**
1. [Sampling code](): extract samples from the corpus and prepare for annotation
2. [Raw to final annotation](): convert raw multi-annotator annotation to the single final annotation

**Sampled corpus for exploratory annotation**</br>
We sampled 3 small sets of reviews (~15 reviews each) to try different settings on Mechanical Turk that might result in better annotation:
1. [Control group]()
    - Used the original annotation guidelines completed in milestone 2
    - No restrictions on annotator approval rate
    - \$0.03 per task (moderate pay)
2. [High pay high standard]()
    - Used the original annotation guidelines completed in milestone 2, with emphasize on multi-label
    - Annotator approval rate must be >80%
    - 0.05 per task (high pay)
3. [Simple rules]()
    - Simplified annotation guidelines to improve readability, with emphasize on multi-label
    - No restrictions on annotator approval rate
    - \$0.03 per task (moderate pay)
    
**Corresponding exploratory annotation files**
1. [Control group: annotation]()
2. [High pay high standard: annotation]()
3. [Simple rules: annotation]()

**Final annotation**</br>
For the final annotation we chose the second approach: high pay and high standard (for details please see the [interannotator agreement study]())
1. [Corpus for annotation (291 annotations)]()
2. [Mechanical Turk file]()
3. [Final *single* annotation file (291 annotations with text)]()

## Reflection on the process
**Corpus**
Also mentioned in milestone 2, the corpus includes many non-English reviews that cannot be filtered out nor avoided when sampling for annotation. To deal with this problem, we asked all annotators to mark all non-English texts with empty labels.

**Mechanical Turk**
As this annotation task requires detailed definition for each label to facilitate interannotator agreement, it is not the most suitable task for crowd sourcing on Mechanical Turk. Annotators were not motivated to look through the annotation guidelines in detail, and sometimes they would choose a single annotation label instead of multiple ones, just to complete the task as quickly as possible. To counter this inherit problem of Mechanical Turk, we set the annotator requirement to have a high approval rate, so they are more motivated to be *correct* instead of *quick*. 

