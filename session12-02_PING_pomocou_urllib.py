import urllib.request
import time


# posielame request na url adresu

def ping_url(host):
    t1 = time.time()
    urllib.request.urlopen(host+'/index.html').read()
    print(t1,'\t', time.time())
    return ((time.time()-t1)*1000.0)

print(ping_url('https://fortisauris.com'))