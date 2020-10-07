import csv
import re
import jieba
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from corextopic import corextopic as ct

if __name__ == '__main__':
    with open('student_review.csv') as csvfile:
        rows = csv.DictReader(csvfile)
        csv_list = []
        for row in rows:
            row_list = []
            if row['Interest']=='5' and row['Gain']==row['Positive']==row['Speed']==row['Difficult']=='3':
                row_list.append('Interest_5')
                row_list.append(row['Content'])
                csv_list.append(row_list)
            if row['Interest']=='1' and row['Gain']==row['Positive']==row['Speed']==row['Difficult']=='3':
                row_list.append('Interest_1')
                row_list.append(row['Content'])
                csv_list.append(row_list)

            if row['Gain']=='5' and row['Interest']==row['Positive']==row['Speed']==row['Difficult']=='3':
                row_list.append('Gain_5')
                row_list.append(row['Content'])
                csv_list.append(row_list)
            if row['Gain']=='1' and row['Interest']==row['Positive']==row['Speed']==row['Difficult']=='3':
                row_list.append('Gain_1')
                row_list.append(row['Content'])
                csv_list.append(row_list)

            if row['Positive']=='5' and row['Gain']==row['Interest']==row['Speed']==row['Difficult']=='3':
                row_list.append('Positive_5')
                row_list.append(row['Content'])
                csv_list.append(row_list)
            if row['Positive']=='1' and row['Gain']==row['Interest']==row['Speed']==row['Difficult']=='3':
                row_list.append('Positive_1')
                row_list.append(row['Content'])
                csv_list.append(row_list)

            if row['Speed']=='5' and row['Gain']==row['Positive']==row['Interest']==row['Difficult']=='3':
                row_list.append('Speed_5')
                row_list.append(row['Content'])
                csv_list.append(row_list)
            if row['Speed']=='1' and row['Gain']==row['Positive']==row['Interest']==row['Difficult']=='3':
                row_list.append('Speed_1')
                row_list.append(row['Content'])
                csv_list.append(row_list)

            if row['Difficult']=='5' and row['Gain']==row['Positive']==row['Speed']==row['Interest']=='3':
                row_list.append('Difficult_5')
                row_list.append(row['Content'])
                csv_list.append(row_list)
            if row['Difficult']=='1' and row['Gain']==row['Positive']==row['Speed']==row['Interest']=='3':
                row_list.append('Difficult_1')
                row_list.append(row['Content'])
                csv_list.append(row_list)
        for i in range(len(csv_list)):
            print(csv_list[i])

        with open('new_student_review.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 寫入二維表格
            writer.writerow(['Label','Content'])
            writer.writerows(csv_list)

