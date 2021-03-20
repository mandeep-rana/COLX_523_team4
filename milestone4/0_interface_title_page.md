# Corpus interface title page

**Purpose:**

The purpose of this project is to create a more detailed filtering system for user reviews on Coursera (https://www.coursera.org/). Currently, reviews on Coursera are only being categorized into 2 aspects: 
1. Whether the reviewer has completed the course (learners/completers)
2. Reviewers' overall perception of the course (1-5 stars)

Our team would like to break down each review into different aspects and label them, so that a potential learner can easily find reviews that mention aspects of the course that are of their interest.







**Corpus:**

This corpus contains 19822 reviews over 90 Coursera courses along with some metadata about each course. Each course is associated with a unique URL, a course name, the instructor name (in the case where there are multiple instructors to the course, only the first name is shown), and an overall rating of the course ranging from 1 to 5 stars. Each review is also associated with a rating that the user has chosen, which contributes to the overall rating of the course.







**Annotation:**

289 reviews have been annotated based on 5 labels: Content, Course delivery, Workload, Difficulty, and Usefulness. Our team have done a multi-label annotation, so that the annotators would choose all applicable aspects that a text has mentioned.
- Breakdown of the annotations:
- 39 reviews annotated as containing "Content"
- 171 reviews annotated as containing "Course delivery"
- 9 reviews annotated as containing "Workload"
- 22 reviews annotated as containing "Difficulty"
- 103 reviews annotated as containing "Usefulness"