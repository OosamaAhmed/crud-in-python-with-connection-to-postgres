import psycopg2

# global variable
dbname= 'crud'
dbpassword = 'iti' 
dbuser = 'python'
# ------------
# (1--> do connection )
def connect():
    try:
        connection = psycopg2.connect (
            database=dbname,
            user=dbuser,
                password=dbpassword, 
                            host='127.0.0.1',
                            port='5432')
        return connection
    except (Exception, psycopg2.Error) as e:
        print(e)
        return None