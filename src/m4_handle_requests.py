import sqlite3
import json
from urllib.parse import unquote

db_name='d2.db'

def read_sql_to_dict(cur,sql_cmd):
    cur.execute(sql_cmd)
    desc = cur.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cur.fetchall()]
    return data

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
    res=read_sql_to_dict(cur,sql_cmd)
    print(res)
    return res

def search_review_by_keywords(kw,cur):
    kw=unquote(kw)
    search_keywords=kw.split()
    sql_cmd_base="""select course_url,review_date,helpful_count,rating,review from reviews where """
    tail="and ".join(["""review like '%{}%'""".format(i) for i in search_keywords])
    sql_cmd=sql_cmd_base+tail
    res=read_sql_to_dict(cur,sql_cmd)
    print(res)
    return res

def search_review_by_instructor(kw,cur):
    kw=unquote(kw)
    search_keywords=kw.split()
    sql_cmd_base="""select title,instructor,average_rating,course_url,review_date,helpful_count,rating,review from reviews left join courses on reviews.course_url=courses.url where """
    tail="or ".join(["""instructor like '%{}%'""".format(i) for i in search_keywords])
    sql_cmd=sql_cmd_base+tail
    res=read_sql_to_dict(cur,sql_cmd)
    print(res)
    return res

def search_annotation_by_facet(kw,cur):
    kw=unquote(kw)
    search_keywords=kw.split()
    sql_cmd_base="""select course_url,review_date,helpful_count,rating,review from annotation left join reviews on annotation.id=reviews.id where """
    tail="and ".join(["""{}='T'""".format(i) for i in search_keywords])
    sql_cmd=sql_cmd_base+tail
    res=read_sql_to_dict(cur,sql_cmd)
    print(res)
    return res

param_decipher('search_course_by_keywords?kw=data%20science')
param_decipher('search_review_by_keywords?kw=data%20science')
param_decipher('search_review_by_instructor?kw=andrew')
param_decipher('search_annotation_by_facet?kw=content%20difficulty')
