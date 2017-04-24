# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2,random,re
# import cookielib

proxy_on=True

proxy_list = [
    {"http": "104.236.174.220:3128"},



]

user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    ]

# download url,设置代理 ／cookies
def download(url,user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',num_retries=2):
    print "Downloading:", url
    headers={'User-agent':random.choice(user_agents)}
    request=urllib2.Request(url,headers=headers)
    if proxy_on:
        print '----Use Proxy---'
        ####-----http://www.xicidaili.com/
        proxy_ip=random.choice(proxy_list)
        print proxy_ip
        proxy_support = urllib2.ProxyHandler(proxy_ip)
        #--------cookie setting
        # cj = cookielib.LWPCookieJar()
        # cookie_support = urllib2.HTTPCookieProcessor(cj)
        # opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)
        #-----http proxy setting
        opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    try:
        html= urllib2.urlopen(request).read()
        print html
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html=None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                #recursively retry 5xx HTTP errors print download("http://httpstat.us/500")
                return download(url,user_agent,num_retries-1)

    return html

# //通过sitemap得到相关链接
def crawl_sitemap(url):
    #download the sitemap file
    sitempap=download(url)
    #extract the sitemap links
    links=re.findall('<loc>(.*?)</loc>',sitempap)
    #download each link
    for link in links:
        html=download(link)
        #scrape html here


print download("http://qd.lianjia.com/ershoufang/pg2/")

