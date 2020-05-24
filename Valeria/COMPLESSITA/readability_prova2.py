import csv
import os
from readability import Readability

path= r"/Users/valeriaguttilla/Desktop/MASTER/PROGETTONE/ANALISI_TESTUALE/SOTTOTITOLI/DISNEY/Disney Animation"
output_file='text_analysis.csv'
header=['Title','Flesch-Kincaid score','Flesch-Kincaid grade level']

with open (output_file, 'w', encoding='utf-8', newline='\n') as output_handle:
    my_writer= csv.writer(output_handle, delimiter=',', quotechar='"')
    my_writer.writerow(header)

    for dirpath, dirnames, files in os.walk(path):
        print(f'Found directory: {dirpath}')
        for file in files:
            with open(dirpath+ "/" + file, 'r', encoding='Latin-1') as f:
                text=f.read()
                print(text)
                r = Readability(text)
                print(r)
                fk = r.flesch_kincaid()
                Flesch_Kincaid_score = fk.score
                Flesch_Kincaid_gl = fk.grade_level

                row = [file, Flesch_Kincaid_score, Flesch_Kincaid_gl]
                my_writer.writerow(row)