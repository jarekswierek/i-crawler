# I-Crawler

App for crawling Instagram by API and saving results in Elasticsearch. App also allow for searching photos in collected media by tag.

# Setup

1. Clone app

```
git clone git@github.com:jarekswierek/i-crawler.git
```

2. Install requirements on virtualenv with python3

```
virtualenv -p python3 ENV
source ./ENV/bin/activate
cd i-crawler
pip install -r requirements.txt
```

3. Add api_keys.json file to i-crawler dir

```
{
    "user_id": "<INSTAGRAM_USER_ID>",
    "token": "<INSTAGRAM_USER_TOKEN>"
}
```

4. Install, configure and run elasticsearch in other terminal tab (use tutorial)

```
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04
```

5. Start crawling (recommended in other terminal tab)

```
python3 manage.py run_crawler
```

6. Run web app (localhost:8000)

```
python3 manage.py runserver
```
