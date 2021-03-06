import pandas as pd
import psycopg2
from sqlalchemy import create_engine

output_path = "resources/pipelines/poc_pipeline/"
output_file_path = output_path + 'test1.txt'

update_query="update israel_team.users_amazon_score_by_action_poc set amount_of_days=32 WHERE respondent_id='7ee87a52-cbf3-4ba7-af74-d0d267d9bba4' and action_name='Search'" 
con=psycopg2.connect(dbname= 'crossensedb', host='xs-redshift-instance.cm17e00im9n9.us-east-1.redshift.amazonaws.com', 
    port= '5439', user= 'crossense', password= '89VdfK5RmWKzUw43')
cur = con.cursor()
cur.execute(update_query)

input_query="select * from israel_team.users_amazon_score_by_action_poc where respondent_id='7ee87a52-cbf3-4ba7-af74-d0d267d9bba4' and action_name='Search'"
df = pd.read_sql(input_query, con=con)
df.to_csv(output_file_path, sep = "\t", encoding = 'utf-8',mode='a', index = False)

cur.close() 
con.close()




