from core import EnchantmentProbabilityNotice
from urllib import request, parse
import bs4
import json

def _getDataFromUrl(url, data=None):
    if data!=None: data=parse.urlencode(data).encode()
    req = request.Request(url, data=data, headers={
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    with request.urlopen(req) as response:
      data = response.read().decode('utf-8')
    return str(data)

def _getScrollInfo2Url(SN: str):
    return 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollInfo2.ashx?SN=' + SN

def _getScrollDetail2(SN: str, scrollID: str):
    return 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=' + SN + '&scrollID=' + scrollID

def _getScrollID(SN):
    url = _getScrollInfo2Url(SN)
    data = _getDataFromUrl(url)
    return str(json.loads(data)['Scrolls'][0]['ScrollID'])

def _getSN(noticeUrl: str):
    data = _getDataFromUrl(noticeUrl)
    data = bs4.BeautifulSoup(data, 'html.parser')
    data = data.find('input', id='loadPageUrl')
    return data.get('value').replace('https://ro.gnjoy.com.tw/notice/Scroll2/index.html#','')  # type: ignore     

def _getAPIFromNotice(url):
    SN = _getSN(url)
    scrollID = _getScrollID(SN)
    return _getScrollDetail2(SN, scrollID)

def _getDataFromAPI(url):
    data = _getDataFromUrl(url)
    return json.loads(data)

def _getAllProbabilityNoticeUrl():
    url = "https://ro.gnjoy.com.tw/api/getNewsList.ashx"
    data = {
      "newsType": 8,
      "pageSize": 999999,
      "page": 1,
      "searchKey": "",
      "GameId": "RO",
    }
    data = _getDataFromUrl(url, data)
    data = json.loads(data)
    ids = map(lambda x: x["newsId"], data["news"])
    urls = map(lambda id:"https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=" + str(id), ids)
    return list(urls)

class EnchantmentProbabilityNoticeCrawler:
    def run(self, url: str) -> EnchantmentProbabilityNotice:
        api = _getAPIFromNotice(url)
        result = _getDataFromAPI(api)
        return {
            'Name': result['Name'],
            'Items': result['Items'],
            'Des': result['Des'],
            'Url': url,
            'API': api
        }

    def runAll(self):
        urls = _getAllProbabilityNoticeUrl()
        notices = map(lambda url: self.run(url), urls)
        notices = filter(lambda notice: self.checkNotice(notice), notices)
        return list(notices)

    def checkNotice(self, notice: EnchantmentProbabilityNotice):
        return notice['Items'][0]['Name'] == '---------------固定附加第一欄隨機能力---------------'
