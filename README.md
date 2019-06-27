# faca_crawler

This spider crawls FACAdatabase.gov using the scrapy package to look for the urls of federal agencies advisory committees. The Federal Advisory Committee Act (FACA) database contains information on around 1,000 advisory committees.

To crawl the database, make sure you are on the root directory of faca_crawler.
Then run the facaspider and the results will be stored in the root directory as "facaspider_links.csv".
You should be looking at something like this:

```console
foo@bar:~$ cd faca_crawler/faca_scraper
FACA.ipynb		faca_scraper		scrapy.cfg
foo@bar:~$ scrapy runspider faca_scraper/spiders/facaspider.py
2019-06-27 10:28:22 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: faca_scraper)
2019-06-27 10:28:22 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: faca_scraper)
2019-06-27 10:28:22 [scrapy.utils.log] INFO: Versions: lxml 4.3.4.0, libxml2 2.9.9, cssselect 1.0.3, parsel 1.5.1, w3lib 1.20.0, Twisted 19.2.1, Python 3.7.3 (default, Jun 19 2019, 07:38:49) - [Clang 10.0.1 (clang-1001.0.46.4)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1c  28 May 2019), cryptography 2.7, Platform Darwin-18.5.0-x86_64-i386-64bit
...
foo@bar:~$ ls
FACA.ipynb		facaspider_links.csv
faca_scraper		scrapy.cfg
```
