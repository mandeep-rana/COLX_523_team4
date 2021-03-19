import sqlite3
import json
from urllib.parse import unquote

db_name='d2.db'

def param_decipher(url):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    kw=url.split('kw=')[1]
    if 'search_course_by_keywords' in url:
        res=search_course_by_keywords(kw,cur)
    elif 'search_review_by_keywords' in url:
        res=search_review_by_keywords(kw,cur)
    elif 'search_review_by_instructor' in url:
        res=search_review_by_instructor(kw,cur)
    elif 'search_annotation_by_facet' in url:
        res=search_annotation_by_facet(kw,cur)
    else:
        res={'msg':'error: invalid params'}
    return json.dumps(res)

def search_course_by_keywords(kw,cur):
    kw=unquote(kw)
    search_keywords=kw.split()
    sql_cmd_base="""select url,title,instructor,average_rating from courses where """
    tail="and ".join(["""title like '%{}%'""".format(i) for i in search_keywords])
    sql_cmd=sql_cmd_base+tail


def search_review_by_keywords(kw,cur):
    pass

def search_review_by_instructor(kw,cur):
    pass

def search_annotation_by_facet(kw,cur):
    pass

param_decipher('search_course_by_keywords?kw=data%20science')
