## COLX 523: Advanced Corpus Linguistics
### Team 4
### Members: Mia, Lisa, Derek, Mandeep
#### Coursera review study

#### Background
With the development of internet and especially under the situation of CONVID-19, people are switching from offline to online to work and study. Online study helps people get educated by the well-known institutions and improve their lives for family and communities. Hence choose the right course is particularly important.

People tend to read reviews from the others to learn about the relevant course. That's the reason why we plan to do Coursera review analysis to help people to understand the course in a much easier way (at a glance in stead of reading hundreds of thousands of reviews and get lost.)

#### Methodology
Collect review data from Coursera: https://www.coursera.org/courses

After confirmation, for one course there are more than thousands of reviews, so that the corpus size is enough for our analysis.

#### More about the data

1. Each review has the reviewer’s name.
2. The reviewer’s profile is not accessable.
    a. We don’t know what other course the reviewers have taken.
    b. However, since we have the reviewer names, we might be able to fuzzy match reviews in different courses by the reviewer name. It’s fuzzy because two users might have the same name (i.e. John Brown).
3. Length: some reviews are short “very good course,” while other reviews are long and detailed. 
4. What we care about: course reviews, and in the coming analysis, we would set up a criteria of the length of reviews to analyze. (5-100)
5. Language: The reviews are most in English.
6. Content: course review.
7. Reviewer: the persons who have taken the course.
8. How to filter the reviews: we want reviews from all the courses by accessing the html tags.
9. Data structure: no structure.
10. Metadata: User-name, review upvote counts, review date, user rating for the course(1 to 5 stars).
11. Format: csv

#### Annotation

Course delivery
Assignment
Difficulty
Job hunting
Update frequency
...

#### Visualization
keyword searching by course
Word cloud
Annotation chart

#### Milestone

![](./img/timeline.png)
