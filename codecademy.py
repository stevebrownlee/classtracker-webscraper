import re
import requests
import json
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

FAKE_HEADERS = {'User-Agent': 'Mozilla/5.0'}

def scrape_codecademy(student_name, url):
  REQUIRED_BADGES = [
    "Lesson Completed: Objects",
    "Lesson Completed: Iterators",
    "Lesson Completed: Loops",
    "Lesson Completed: Arrays",
    "Lesson Completed: Scope",
    "Lesson Completed: Functions",
    "Lesson Completed: Variables",
    "Lesson Completed: Introduction to JavaScript",
    "Lesson Completed: Tables",
    "Lesson Completed: Introduction to HTML",
    "Lesson Completed: Learn HTML: Forms",
    "Lesson Completed: Learn HTML: Form Validation",
    "Lesson Completed: Advanced CSS Grid",
    "Lesson Completed: CSS Grid Essentials",
    "Lesson Completed: CSS Typography",
    "Lesson Completed: CSS Color",
    "Lesson Completed: CSS Display and Positioning",
    "Lesson Completed: Changing the Box Model",
    "Lesson Completed: The Box Model",
    "Lesson Completed: CSS Visual Rules",
    "Lesson Completed: CSS Setup and Selectors",
  ]

  def is_achievement_url(href):
    return href and re.compile('achievements').search(href)

  def is_badge_title(tag):
    return tag.name == 'h6' and 'title' in tag['class'][0]

  if url:
    try:
      req = request.Request(url, headers=FAKE_HEADERS)
      with request.urlopen(req) as profile:
        profile_soup = BeautifulSoup(profile, 'html.parser')
        achievement_link = profile_soup.find('a', href=is_achievement_url)

        if achievement_link is not None:
          badges_url = achievement_link['href']
          badge_req = request.Request(
              f'https://codecademy.com{badges_url}', headers=FAKE_HEADERS)
        else:
          print(f"{student_name} needs to update their privacy settings on codecademy")
          return

        with request.urlopen(badge_req) as badges:

          badge_soup = BeautifulSoup(badges, 'html.parser')
          all_badges = badge_soup.find_all(is_badge_title)

          completed_badges = []
          for badge in all_badges:
            if badge.contents[0].strip() in REQUIRED_BADGES:
              completed_badges.append(badge.contents[0].strip())
          percent_complete = int(
              (len(completed_badges) / len(REQUIRED_BADGES)) * 100)
          return percent_complete

    except Exception as e:
      print(f'{student_name}: {e}')
