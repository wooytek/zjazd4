import pandas as pd
import requests
import pprint

url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"


response_users=requests.get(url_users)
response_posts=requests.get(url_posts)
response_comments=requests.get(url_comments)

if response_users.status_code == 200:
    data_users = response_users.json()
    data_posts = response_posts.json()
    pprint.pprint(data_users)

else:
    raise Exception('Nie udało się pobrać danych')
df_users = pd.DataFrame(data_users)
df_posts = pd.DataFrame(data_posts)
print(df_users.to_string())
print(df_posts.to_string())

posts_per_user = df_posts.groupby('userId', as_index=False)['id'].count()
print(posts_per_user)
