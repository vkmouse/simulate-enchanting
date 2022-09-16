from doctest import Example
from simulate_enchanting.crawler.crawler import EnchantmentProbabilityNoticeCrawler
from urllib import request, parse
import json

crawler = EnchantmentProbabilityNoticeCrawler()
url = "http://jwp63667.pythonanywhere.com/notices"
for notice in crawler.runAll():
    data = {
        "notice": json.dumps(notice)
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    with request.urlopen(req) as response:
        data = response.read().decode('utf-8')