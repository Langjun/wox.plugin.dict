#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI

class Main(Wox):

  def request(self,url):
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

  def query(self,key):
    r = self.request('http://dict.baidu.com/s?wd=' + key)
    bs = BeautifulSoup(r.text)
    results = []

    c = bs.select('#en-simple-means > div > p')

    for i in c:
      results.append({
        "Title": i.find('strong').text,
        "SubTitle": i.find('span').text,
        "IcoPath":"img/pic.png",
        "JsonRPCAction":{
          "method": "Wox.ShowApp",
          "parameters":[],
          "dontHideAfterAction":True
        }
      })

    return results

if __name__ == "__main__":
  Main()