# Annotation Plan

## Purpose

The purpose of the annotations is to create a more detailed filtering system for reviews on Coursera. <br>
Currently, reviews on Coursera are only being categorized on 2 aspects:

1. Whether the reviewer has completed the course (learners/completers)
2. Reviewers' overall perception of the course (1-5 stars)

Our team would like to break down each review into different aspects and label them, so that a potential learner can easily find reviews that mention aspects of the course that are of their interest.

## Approach
### What to annotate

Annotations indicate the presence of a certain aspect in a review. That is, we only care about whether a review mentions certain things, but we do not care about the sentiment of that review. The annotation tags are determined after an initial pilot study (please refer to the **Pilot Study** section) of a sample of scraped reviews.<br>
They are:
- **Content**: Course content. What the course is about.
- **Course delivery**: Quality of the course structure, format, and/or instructor.
- **Difficulty**: Difficulty of the concepts presented in the course.
- **Workload**: Amount of time required to devote to a course, or the number of assignments.
- **Usefulness**: If the course contributes to an increase in knowledge, or if it has real-world applications

Each tag is explained in detail in the **Annotation Guideline**.

### How to annotate

For this annotation task, we will be using Mechanical Turk for perform a crowd sourced annotation. Each review will have 3 annotators to work on, so interannotator agreement can be calculated further in the process. To ensure quality of the annotations, Annotators are trained using the Annotation Guideline, which is included in the instruction section of the Mechanical Turk task page.<br>
To complete this milestone, we have successfully had at least one worker complete one annotation. For details on this please refer to the **Pilot Study** section.

### How much to annotate

So far there are 14 reviews annotated by the end of milestone 2. Considering each review gives annotator a reward of \\$0.03, and 3 annotators will be working on each review, we expect to have $50 \div (3 \times 0.3) = 555$ reviews annotated by the end of milestone 3.

## Pilot Study

A pilot study has been done to ensure:
1. The quality of the annotation: the proposed annotation criteria are indeed a good representation of the corpus.
2. That annotation using Mechanical Turk is feasible.

### Stage 1

Initially, the team has decided on the annotation criteria to be course delivery, difficulty, workload, and usefulness. The first part of the pilot study was to check if these criteria well represent the corpus we have.<br>
Two team members have randomly sampled 150 reviews from the corpus and each performed manual annotation on half of the samples. The observation was that the tag `Course delivery` is ambiguous and difficult for annotators to reach an agreement. There were also many reviews mentioning the content of the course, which we did not have a tag for. Therefore, another tag `Content` is brought in to clarify the annotation boundaries. Another observation was that many reviews mentioned recommending a course, however we decided to not include a tag for that aspect, as its concept highly correlates to the star rating given by the reviews.

During this manual annotation process, we have also noticed problems that the corpus had:
1. The corpus included non-English reviews
2. Many reviews included names of the lecturers

This was communicated within the team, and codes have been implemented to remove non-English courses and person names on a best-effort basis.

After the initial manual annotation, the Annotation Guideline was written to explain each annotation tag to future annotators. Examples are also provided along with the explanation. For more details please refer to the **Annotation Guideline** section.

### Stage 2

A small batch of 14 reviews was randomly sampled from the corpus and uploaded on Mechanical Turk to ensure feasibility of crowd source annotation for this project. We requested 3 annotators for each review. At the time of documenting, 33/42 of the annotations have been completed. The batch result csv file from Mechanical Turk is included in the repo, please see repo readme for more details. This proves that it is feasible to implement Mechanical Turk annotation for this project.


## Annotation Guideline

[Please see here](https://github.ubc.ca/dinganc/COLX_523_team4/blob/master/milestone2/3_annotation_guidelines.md)