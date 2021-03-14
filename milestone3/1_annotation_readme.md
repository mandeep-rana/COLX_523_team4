# Annotation Readme

## The process (with links)

**Code**
1. [Sampling code](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/m3_subset_extractor.ipynb): extract samples from the corpus and prepare for annotation
2. [Raw to final annotation](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/m3_import_annotation.ipynb): convert raw multi-annotator annotation to the single final annotation

**Sampled corpus for exploratory annotation**</br>
We sampled 3 small sets of reviews (~15 reviews each) to try different settings on Mechanical Turk that might result in better annotation:
1. [Control group](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/annotation/sampled_reviews.csv)
    - Used the original annotation guidelines completed in milestone 2
    - No restrictions on annotator approval rate
    - \$0.03 per task (moderate pay)
2. [High pay high standard](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/data/sampled_reviews_0.csv)
    - Used the original annotation guidelines completed in milestone 2, with emphasize on multi-label
    - Annotator approval rate must be >80%
    - 0.05 per task (high pay)
3. [Simple rules](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/data/sampled_reviews_1.csv)
    - Simplified annotation guidelines to improve readability, with emphasize on multi-label
    - No restrictions on annotator approval rate
    - \$0.03 per task (moderate pay)
    
**Corresponding exploratory annotation files**
1. [Control group: annotation](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/annotation/sampled_review_annotated.csv)
2. [High pay high standard: annotation](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/annotation/sampled_review_annotated_0.csv)
3. [Simple rules: annotation](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/annotation/sampled_review_annotated_1.csv)

**Final annotation**</br>
For the final annotation we chose the second approach: high pay and high standard (for details please see the [interannotator agreement study](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/milestone3/2_inter_annotator_agreement_study.ipynb))
1. [Corpus for annotation (291 annotations)](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/data/reviews_full.csv)
2. [Mechanical Turk file](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/annotation/reviews_full_annotated.csv)
3. [Final *single* annotation file (291 annotations with text)](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/src/d2.db)

## Challenges
**Corpus**</br>
Also mentioned in milestone 2, the corpus includes many non-English reviews that cannot be filtered out nor avoided when sampling for annotation. To deal with this problem, we asked all annotators to mark all non-English texts with empty labels.

**Mechanical Turk**</br>
As this annotation task requires detailed definition for each label to facilitate interannotator agreement, it is not the most suitable task for crowdsourcing on Mechanical Turk. Annotators were not motivated to look through the annotation guidelines in detail, and sometimes they would choose a single annotation label instead of multiple ones, just to complete the task as quickly as possible. To counter this inherit problem of Mechanical Turk, we set the annotator requirement to have a high approval rate, so they are more motivated to be *correct* instead of *quick*. 

