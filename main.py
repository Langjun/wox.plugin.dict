#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI

class Main(Wox):

  def request(self,url):
    #如果用户配置了代理，那么可以在这里设置。这里的self.proxy来自Wox封装好的对象
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

  def query(self,key):
    # r = self.request('http://dict.baidu.com/s?wd=' + key)
    # bs = BeautifulSoup(r.text)
    url = 'https://dict.baidu.com/'
    results = []
    # for i in bs.select(".comhead"):
      # title = i.previous_sibling.text
      # url = i.previous_sibling["href"]
    results.append({
      "Title": 'title' ,
      "SubTitle": 'subtitle',
      "IcoPath":"img/pic.png",
      "JsonRPCAction":{
        "method": "Wox.ShowApp",
        "parameters":[url],
        "dontHideAfterAction":True
      }
    })

    return results

  def openUrl(self,url):
    webbrowser.open(url)
    WoxAPI.change_query(url)

if __name__ == "__main__":
  Main()