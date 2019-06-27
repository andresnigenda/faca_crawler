# faca_crawler

This spider crawls FACAdatabse.gov using the scrapy package to look for the urls of the Federal agency advisory committees. The Federal Advisory Committee Act (FACA) database contains information on around 1,000 advisory committees.

To crawl the database, make sure you are on the root directory of faca_crawler.
Then run the facaspider, and the results will be stored in the root directory as "facaspider_links.csv".

```console
foo@bar:~$ cd faca_crawler/faca_scraper
FACA.ipynb		faca_scraper		scrapy.cfg
foo@bar:~$ scrapy runspider faca_scraper/spiders/facaspider.py
```
