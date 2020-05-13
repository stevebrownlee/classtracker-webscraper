import re
import requests
import json
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver


def scrape_replit(student_name, url):
  if not url:
    print(f'ERROR: Url not found for {student_name}')
    return
  try:
    with request.urlopen(url) as rq:
      bs = BeautifulSoup(rq, 'html.parser')

      if not bs.find('div', class_='profile-no-repls') is None:
        return

      repls = bs.find_all('a', class_='repl-item-wrapper')
      return len(repls)

  except Exception as e:
    print(f'ERROR: {student_name} {e}')

