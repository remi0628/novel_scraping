import os, time, datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin, urlparse

# Google spreadsheet書き込み為のライブラリ
from google.colab import auth
from oauth2client.client import GoogleCredentials
import gspread

# 認証
auth.authenticate_user()
gc = gspread.authorize(GoogleCredentials.get_application_default())

# スプレッドシート作成
BOOKNAME = "Web小説"
try:
  book = gc.open(BOOKNAME)
except:
  book = gc.create(BOOKNAME)

# スクレイピング
NARO_URL = 'https://ncode.syosetu.com'
# NCODE = 'N8611BV' # ありふれた職業で世界最強
# NCODE = 'n2267be' # Re:ゼロから始める異世界生活
# NCODE = 'n6316bn'   # 転生したらスライムだった件
NCODE = 'n9636x'    # 薬屋のひとりごと
url = "{}/{}/".format(NARO_URL, NCODE)

html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
novel_title = soup.find("p", class_="novel_title").get_text(strip=True)
author = soup.find("div", class_="novel_writername").get_text(strip=True)
print("タイトル：" + novel_title + '\n' + "著者：" + author)
s = len(soup.select("dl.novel_sublist2")) #連載回数取得

print(s)
# タイトルのシートを作成
try:
  sheet = book.worksheet(novel_title[:16])
except:
  sheet = book.add_worksheet(novel_title[:16], 5+s, 6)

"""
worksheets = book.worksheets()
print(worksheets)
for sheet in worksheets:
  if 'novel_title[:16]' == sheet.title:
    sheet = sheet.worksheet(novel_title[:16])
    sheet = sheet.add_worksheet(novel_title[:16], 5+s,6)
"""

sheet.update_cell(1,1, "タイトル")
sheet.update_cell(1,2, novel_title)
sheet.update_acell("A2", "著者")
sheet.update_acell("B2", author)
sheet.update_acell("A3", 'NCODE')
sheet.update_acell("B3", NCODE)

i=4
sheet.append_row(["更新", "サブタイトル", "まえがき", "あとがき", "本文", "URL"])
for data in soup.select("dl.novel_sublist2"):
  subtitle = data.select_one("dd").get_text(strip=True)
  update = data.select_one("dt.long_update").get_text(strip=True)
  texturl = urljoin(url, data.a['href'])
  print(subtitle, update, texturl)

  textdata = urlopen(texturl)
  textsoup = BeautifulSoup(textdata, "lxml")
  text = textsoup.select_one("div#novel_honbun").get_text(strip=True)

  preface ='' #まえがき
  for tp in textsoup.select("div#novel_p"):
    preface += tp.get_text(strip=True)
  afterword = '' #あとがき
  for aw in textsoup.select("div#novel_a"):
    afterword += aw.get_text(strip=True)
  list = [update, subtitle, preface, afterword, text, texturl] #データ
  i += 1
  for j, data in enumerate(list):
    sheet.update_cell(i, j+1, data)
  time.sleep(100)