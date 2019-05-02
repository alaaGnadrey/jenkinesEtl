import pandas as pd


file_base_path = "resources/pipelines/poc_pipeline/"
input_file_path = file_base_path + 'test1.txt'
output_file_path = file_base_path + 'test2.txt'

df = pd.read_csv(input_file_path, sep = "\t")
df.head()
df['amount_of_days']=33
df.head()
df.to_csv(output_file_path, sep = "\t", encoding = 'utf-8',mode='a', index = False)


