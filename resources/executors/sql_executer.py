import sys
import psycopg2
import json

def main():
    # print command line arguments
    # for arg in sys.argv[1:]:
        # print arg
    con=psycopg2.connect(dbname= 'crossensedb', host='redshift-cluster-2.c4srspvxpvhg.eu-west-1.redshift.amazonaws.com', 
    port= '5439', user= 'crossense', password= 'txKW9hkN4kKN4aoP')
    cur = con.cursor()
    cur.execute("select domain_name from main.mobile_urls limit 1;")
    data = cur.fetchall()

    if data and len(data):
        print('data loaded with len = {0}'.format(json.dumps(data)))

    else:
        print('data is empty')

    cur.close() 
    con.close()

if __name__ == "__main__":
    print("sql exectuer main")
    main()