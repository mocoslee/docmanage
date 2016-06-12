
import psycopg2
from django.conf import settings
from coreops_user.celery import app


def _radius_delete_commit(db_conf,username):

    sql = "delete from radcheck where username='%s' and attribute='MD5-Password' and op=':=' " % username
    conn = psycopg2.connect(
            database = db_conf['NAME'],
            user = db_conf['NAME'], 
            password = db_conf['PASSWORD'], 
            host = db_conf['HOST'],
            port = db_conf['PORT']
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def _radius_passwd_md5_commit(db_conf,username,password):
    sql = "select count(*) from radcheck where username='%s' and attribute='MD5-Password' and op=':=' " % username
    conn = psycopg2.connect(
            database = db_conf['NAME'],
            user = db_conf['NAME'], 
            password = db_conf['PASSWORD'], 
            host = db_conf['HOST'],
            port = db_conf['PORT']
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0]==0:
        sql = "insert into radcheck(username,attribute,op,value) values('%s','MD5-Password',':=','%s')" % (username,password)
        cursor.execute(sql)
        conn.commit()
    
    conn.close()

def _radius_passwd_md5(db_conf,username,password):
    sql = "select count(*) from radcheck where username='%s' and attribute='MD5-Password' and op=':=' " % username
    conn = psycopg2.connect(
                database = db_conf['NAME'],
                user = db_conf['NAME'], 
                password = db_conf['PASSWORD'], 
                host = db_conf['HOST'],
                port = db_conf['PORT']
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0]>0:
        sql = """update radcheck set value = '%s' where username = '%s' and 
                    attribute='MD5-Password' and op=':=' """ % (password,username)
        cursor.execute(sql)
        conn.commit()
    conn.close()




@app.task
def password_send(user_id):
    db_conf = settings.DATABASES['default']
    sql = "select * from coreops_auth_usrprofile  where user_id='%s' " % user_id
    conn = psycopg2.connect(
                database = db_conf['NAME'],
                user = db_conf['USER'],
                password = db_conf['PASSWORD'],
                host = db_conf['HOST'],
                port = db_conf['PORT']
    )
    
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for line in result:
        if line[1]:
            _radius_passwd_md5(settings.DATABASES['radius'],line[9],line[2])



@app.task
def password_commit(user_id = None):
    db_conf = settings.DATABASES['default']
    sql = "select * from coreops_auth_usrprofile"
    if user_id :
        sql = "%s where user_id = %s" % (sql,user_id)
    conn = psycopg2.connect(
            database = db_conf['NAME'],
            user = db_conf['USER'],
            password = db_conf['PASSWORD'],
            host = db_conf['HOST'],
            port = db_conf['PORT']
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for line in result:
        if line[2]:
            if user_id:
                _radius_passwd_md5(settings.DATABASES['radius'],line[9],line[2])                    
            else:
                _radius_passwd_md5_commit(settings.DATABASES['radius'],line[9],line[2])

@app.task
def delete_commit(username):
    _radius_delete_commit(settings.DATABASES['radius'],username)

