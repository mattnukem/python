import urllib.request


urllib.request.urlretrieve("http://cros-omahaproxy.appspot.com/all", "crosversions.csv")
urllib.request.urlretrieve("https://raw.githubusercontent.com/reynhout/cbiddb/master/cbids.json", "cbids.json")
