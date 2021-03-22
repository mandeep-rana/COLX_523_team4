from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from collections import defaultdict
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import random
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect


app = FastAPI()


def get_courses(course, rating):
    """given course keyword and/or rating, returns corresponding reviews for that course and with their selected rating"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"SELECT a.title, b.review, a.average_rating FROM courses a , reviews b where a.title like '%{course}%' and a.url = b.course_url"
        if rating != 0:
            query = query + " and a.average_rating >= " + rating

        rs = con.execute(query)
        S = []
        count = 0

        S.append(
            "<div id='table-wrapper'> <div id='table-scroll'><table border =1  class='ex_table' ><tr><th>Title</th><th>Reviews</th><th>Rating</th></tr>"
        )
        for row in rs:
            count += 1
            S.append("<tr>")
            S.append("<td >" + str(row[0]) + "</td>")
            S.append("<td  >" + str(row[1]) + "</td>")
            S.append("<td>" + str(row[2]) + "</td>")
            S.append("</tr>")
        S.append("</table></div></div>")
        S.append("<div class='myDiv'>Total records found: " + str(count) + "</div>")

        con.close()
    return "".join(S)


def get_all_courses():
    """This function gets the list of all the 90 courses from databases"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"SELECT title FROM courses"

        rs = con.execute(query)
        S = []
        count = 0
        S.append(
            "<div id='table-wrapper'> <div id='table-scroll'><table border =1  class='ex_table'><tr><th>Course</th></tr>"
        )
        for row in rs:
            count += 1
            S.append("<tr>")
            S.append("<td>" + str(row[0]) + "</td>")

            S.append("</tr>")
        S.append("</table></div></div>")
        S.append("<div class='myDiv'>Total records found: " + str(count) + "</div>")
        con.close()
    return "".join(S)


def get_annotation(annotation):
    """return annotation, couse, review and ratings based on input category"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"select c.title,b.review,b.rating  from annotation a , reviews b, courses c where a.{annotation}='T' and a.id = b. id and b.course_url = c.url"

        rs = con.execute(query)
        S = []
        count = 0
        S.append(
            "<div id='table-wrapper'> <div id='table-scroll'><table border =1  class='ex_table'><tr><th>Title</th><th>Review (" + annotation + ")</th><th>Rating</th></tr>"
        )
        for row in rs:
            count += 1
            S.append("<tr>")
            S.append("<td>" + str(row[0]) + "</td>")
            S.append("<td >" + str(row[1]) + "</td>")
            S.append("<td >" + str(row[2]) + "</td>")

            S.append("</tr>")
        S.append("</table></div></div>")
        S.append("<div class='myDiv'>Total records found: " + str(count) + "</div>")
        con.close()
    return "".join(S)


def get_reviews(review, rating):
    """given input review keyword and rating, return corresponding reviews satisfying the query"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"select course_url,review_date,helpful_count,rating,review from reviews where review like '%{review}%'"
        if rating != 0:
            query = query + " and rating >= " + rating

        rs = con.execute(query)
        S = []
        count = 0

        S.append(
            "<div id='table-wrapper'> <div id='table-scroll'><table border =1 class='ex_table'><tr><th>Course url</th><th>Review Date</th><th>Helpful Count</th><th>Ratings</th><th>Review</th></tr>"
        )
        for row in rs:
            count += 1
            S.append("<tr>")
            S.append("<td>" + str(row[0]) + "</td>")
            S.append("<td>" + str(row[1]) + "</td>")
            S.append("<td>" + str(row[2]) + "</td>")
            S.append("<td>" + str(row[3]) + "</td>")
            S.append("<td>" + str(row[4]) + "</td>")

            S.append("</tr>")
        S.append("</table></div></div>")
        S.append(
            "<div class='myDiv'>Total records found: " + str(count) + "/19822</div>"
        )
        con.close()
    return "".join(S)


def get_instructor(instructor, rating):
    """return corresponding reviews that are about courses taught by given instructor"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"select title,instructor,average_rating,course_url,review_date,helpful_count,rating,review from reviews left join courses on reviews.course_url=courses.url where instructor  like '%{instructor}%'"
        if rating != 0:
            query = query + " and rating >= " + rating

        rs = con.execute(query)
        S = []
        count = 0
        S.append(
            "<div id='table-wrapper'> <div id='table-scroll'><table border =1  class='ex_table'><thead><tr><th>Title</th><th>Instructor</th><th>Average Rating</th><th>Course url</th><th>Review Date</th><th>Helpful Count</th><th>Rating</th><th>Review</th></tr></thead><tbody>"
        )
        for row in rs:
            count += 1
            S.append("<tr>")
            S.append("<td>" + str(row[0]) + "</td>")
            S.append("<td>" + str(row[1]) + "</td>")
            S.append("<td>" + str(row[2]) + "</td>")
            S.append("<td>" + str(row[3]) + "</td>")
            S.append("<td>" + str(row[4]) + "</td>")
            S.append("<td>" + str(row[5]) + "</td>")
            S.append("<td>" + str(row[6]) + "</td>")
            S.append("<td>" + str(row[7]) + "</td>")

            S.append("</tr>")
        S.append("</tbody></table></div></div>")
        S.append(
            "<div class='myDiv'>Total records found: " + str(count) + "/19822</div>"
        )
        con.close()
    return "".join(S)


def get_annotation_count():
    """annotation distribution statistics, for graphing purposes"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"select * from annotation"
        rs = con.execute(query)
        count_dict = defaultdict(int)
        for row in rs:
            if row[1] == "T":
                count_dict["Content"] += 1
            if row[2] == "T":
                count_dict["Course Delivery"] += 1
            if row[3] == "T":
                count_dict["Difficulty"] += 1
            if row[4] == "T":
                count_dict["Workload"] += 1
            if row[5] == "T":
                count_dict["Usefulness"] += 1
        con.close()

    return count_dict


def get_rating_count():
    """rating distribution statistics, for graphing purposes"""
    engine = create_engine("sqlite:///d2.db")
    with engine.connect() as con:
        query = f"select rating from reviews"
        rs = con.execute(query)
        count_dict1 = defaultdict(int)
        for row in rs:
            if row[0] == 1.0:
                count_dict1["1.0"] += 1
            elif row[0] == 2.0:
                count_dict1["2.0"] += 1
            elif row[0] == 3.0:
                count_dict1["3.0"] += 1
            elif row[0] == 4.0:
                count_dict1["4.0"] += 1
            elif row[0] == 5.0:
                count_dict1["5.0"] += 1
        con.close()

    return count_dict1


def save_bar_graph(count_dict, filename, get_title, x_label):
    """produce bar graphs from given statistics """

    sorted_annotation = sorted(
        count_dict.keys(), key=lambda x: count_dict[x], reverse=True
    )
    nums = [count_dict[annotation] for annotation in sorted_annotation]
    ticks = np.arange(0, len(nums))

    plt.bar(ticks, nums, width=0.8, align="center")
    plt.xticks(ticks, sorted_annotation, rotation=0)
    plt.ylabel("Count", fontsize=15)
    plt.xlabel(x_label, fontsize=15)
    plt.title(get_title, fontsize=15)
    plt.savefig(filename)
    plt.clf()


@app.get("/")
def start():
    return FileResponse("frontend.html")


@app.get("/{filename}")
def get_file(filename):
    return FileResponse(filename)


@app.get("/pos/")
def display_pos(genre, rating, annotation, review, instructor, mode, all):
    "Main function to display the page based on the query generated"
    count_dict = get_annotation_count()
    count_dict1 = get_rating_count()
    if all == "courses":
        
       return HTMLResponse(get_all_courses())
    if mode == "ann_graph":
        save_bar_graph(
            count_dict, "ann_graph.png", "Total Annotation Count Category-wise", "Annotations"
        )
        return HTMLResponse(
            '<div align=center><img src="ann_graph.png?'
            + str(random.randint(1, 1000))
            + '"></div>'
        )

    if mode == "rate_graph":
        save_bar_graph(
            count_dict1, "rate_graph.png", "Distribution of ratings count", "Ratings"
        )
        return HTMLResponse(
            '<div align=center><img src="rate_graph.png?'
            + str(random.randint(1, 1000))
            + '"></div>'
        )

    if len(genre) != 0 and rating != 0:
        return HTMLResponse(get_courses(genre, rating))
    if annotation != "default":
        return HTMLResponse(get_annotation(annotation))
    if len(review) != 0:

        return HTMLResponse(get_reviews(review, rating))

    if len(instructor) != 0:

        return HTMLResponse(get_instructor(instructor, rating))

        
    get_annotation_count()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999, debug=True)