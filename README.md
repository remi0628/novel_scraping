# novel_scraping
小説家になろう　URL：https://syosetu.com/  

URLサイトから好きな小説のデータをGoogle SpreadSheetsにスクレイピングします。  
小説本文に対して形態素解析を行います。  
その結果をヒストグラム、ワードクラウドで表します。  

Scrape the data of your favorite novel from the URL site into your Google SpreadSheets.  
Morphological analysis is performed on the text of the novel.  
The results are represented in a histogram and word cloud.  


# Demo
Google Coraboratoryから各ファイルを実行。  

Eseguire ogni file da Google Coraboratory.  



>### crawler.ipynb
><img src="https://user-images.githubusercontent.com/16487150/87391191-3d02d580-c5e5-11ea-83af-5675edb055ff.png" width="90%">

>### data_plot.ipynb
><img src="https://user-images.githubusercontent.com/16487150/87386954-a7fbde80-c5dc-11ea-9796-9c00c3d5a58a.png" width="40%">
><img src="https://user-images.githubusercontent.com/16487150/87387066-e42f3f00-c5dc-11ea-8676-241073cbb7f7.png" width="40%">


# Note
Google SpreadSheetに大量のデータを入れたい場合は、Google Claboratoryで実行した方が良いです。  
通常1ユーザーあたり100秒間のリクエスト数に制限があるため、長時間掛かります。  

If you want to put a large amount of data into Google SpreadSheet, it is better to run it in Google Claboratory.  
This is because there is a limit to the number of requests per 100 seconds per user, and this can take a long time.  
