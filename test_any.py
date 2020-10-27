import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np
import main
import csv
# 如果檔案內有一些編碼錯誤，使用 errors='ignore' 來忽略錯誤
with open('worldcloudsource.csv') as csvfile:
	rows = csv.DictReader(csvfile)
	with open('stop_word_corex.txt') as ff:
		All_sw = ff.read()
		stop_word_list = All_sw.splitlines()
		words_list, Label = main.cut(rows, stop_word_list, '2')	
	words = " ".join(words_list)
	print(words)
	font = 'SourceHanSansTW-Regular.otf'

	#背景顏色預設黑色，改為白色、使用指定圖形、使用指定字體
	my_wordcloud = WordCloud(background_color='white',width=960,height=960,font_path=font,).generate(words)

	plt.imshow(my_wordcloud)
	plt.axis("off")
	plt.show()
	#存檔
	WordCloud.to_file('word_cloud.png')