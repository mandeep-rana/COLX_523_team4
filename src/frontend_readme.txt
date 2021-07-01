Coursera Courses Annotation Project

This frontend is divided into 5 search fields where users can search based on different search criteria.

1. Search by course name
2. Search by annotation
3. Search the reviews by keyword
4. Search reviews of instructor
5. Select the graphs to display

1. Search by course name
This is a free text search where users can input any name of course to search. Users can also select a rating from drop-down and results will be filtered based on ratings. On the backend data is filtered from the SQLlite db using SQL queries.  
Users can not search if the text field is left blank or the user tries to input special characters in the text field after clicking on “Search”.   This validation has been implemented keeping in mind about the security features and user should not be able to do SQL injection.
If the user wants to see all the 90 courses, he can click on “Click courses to display the list of all the courses”. A list of all the courses will be displayed and the user can view the course for further searching.

2. Search by annotation
There are five categories Content, Course Delivery, Difficulty, Workload, Usefulness. On selecting the category, results of that category are displayed where the text is annotated. Course title, reviews, and review ratings are displayed for annotated content.

3. Search the reviews by keyword
If the user wants to search for a particular keyword in the text in reviews, he can input any text in the input field. Users can also select a rating from the drop-down and results will be filtered based on ratings. On the backend data is filtered from the SQLlite db using SQL queries.  The output will have additional information like Course URL, review date, ratings, and reviews containing that keyword.

Users can not search if the text field is left blank or the user tries to input special characters in the text field after clicking on “Search”.   This validation has been implemented keeping in mind about the security features and user should not be able to do SQL injection.


4. Search reviews of instructor
If the user wants to search for courses taught by particular instructors, he can search for the input name of the instructor. Users can also select review ratings from drop-down and results will be filtered based on ratings. On the backend data is filtered from the SQLlite db using SQL queries.  The output will have additional information like Course URL, review date, ratings and reviews, average rating on the instructor.

Users can not search if the text field is left blank or the user tries to input special characters in the text field after clicking on “Search”.   This validation has been implemented keeping in mind about the security features and user should not be able to do SQL injection.

5. Select the graphs to display
Users can select 2 different graphs to display total annotations category-wise and a graph for the count of all the review ratings from 1.0 to 5.0. All the counts are sorted in descending order.

Additional features while searching the records.

Total count of records found in the search will be displayed at the bottom of the page.
All tables are scrollable.