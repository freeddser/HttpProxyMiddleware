#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2


def get_html(url):
    request = urllib2.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11")
    html = urllib2.urlopen(request)
    return html.read()


def get_soup(url):
    soup = BeautifulSoup(get_html(url), "lxml")
    return soup


def fetch_us_proxy():
    proxyes = []
    try:
        url = "http://www.us-proxy.org/"
        soup = get_soup(url)
        table = soup.find("table", attrs={"id": "proxylisttable"})

        tbs = table.find_all("tr")
        # print trs
        for i in range(1, 20):
            # print tbs[i]
            # print '----\n'
            tr = tbs[i]
            tds = tr.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            # print ip+":"+port
            proxyes.append("%s:%s" % (ip, port))
    except Exception as e:
        print e
        print "fail to fetch from US"
    return proxyes


# def fetch_all():
#     proxyes = []
#     proxyes += fetch_us_proxy()
#     valid_proxyes = []
#     print "checking proxyes2 validation"
#     for p in proxyes:
#         print p
#     #     if check(p):
#     #         valid_proxyes.append(p)
#     # return valid_proxyes


def check(proxy_ip):
    proxy_on=True

    url="http://qd.lianjia.com/ershoufang/pg2/"
    user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    print "Downloading:", url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    if proxy_on:
       print '----Use Proxy---'
       print proxy_ip
       proxy_support = urllib2.ProxyHandler({'http': "http://" + proxy_ip})
            # --------cookie setting
            # cj = cookielib.LWPCookieJar()
            # cookie_support = urllib2.HTTPCookieProcessor(cj)
            # opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)
            # -----http proxy setting
       opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
       urllib2.install_opener(opener)

    try:
            html = urllib2.urlopen(request).read()
            print html
            if html.find("authType"):
                print "Need AUTH"
            else:
                print "###############can use###########"
                print proxy_ip

                return True

    except urllib2.URLError as e:
            print 'Download error:', e.reason
            html = None
            # if num_retries > 0:
            #     if hasattr(e, 'code') and 500 <= e.code < 600:
            #         # recursively retry 5xx HTTP errors print download("http://httpstat.us/500")
            #         return download(url, user_agent, num_retries - 1)

            return False
    

if __name__ == '__main__':
    import sys

    proxyes = fetch_us_proxy()[0]
    print len(fetch_us_proxy())
    listip= fetch_us_proxy()
    for p in range(0,len(listip)):
        print listip[p]
        print check(listip[p])
    # # print check("202.29.238.242:3128")
    # for p in proxyes:
    #     print check(p)
    #     #
    #     # print check("178.140.174.37:8081")
