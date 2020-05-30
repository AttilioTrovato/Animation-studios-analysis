# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:01:54 2020

@author: Amministratore
"""

import os
import re
import spacy
import en_core_web_sm
import matplotlib.pyplot as plt
import nltk
import csv
from collections import Counter

nlp = en_core_web_sm.load()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

path= r"C:\Users\Amministratore\Desktop\MASTER\Progettone\clean_subtitles"
output_file='text_analysis.csv'
header=['Title','House', 'Decade', 'Year', 'Category', 'Movie_len','Avg_WordLen_Movie', 'Avg_PhrLen_Movie', 'Avg_WordLen_Phrase', 'Num_Adjectives', 'Num_Adverbs', 'Short_Phrases%']

with open (output_file, 'w', encoding='utf-8', newline='\n') as output_handle:
    my_writer= csv.writer(output_handle, delimiter=',', quotechar='"')
    my_writer.writerow(header)

    for dirpath, dirnames, files in os.walk(path):
        print(f'Found directory: {dirpath}')
        for file in files:
            with open(dirpath+'\\' + file, 'r', encoding='Latin-1') as f:
                text=f.read()
                doc= nlp(text)
                #print('Text', text)
                
                #testo del film con frasi separate
                phrases=[]
                for sentence in doc.sents:
                    phrases.append(sentence.text)
                movie_length=len(phrases)
                #print('Movie length', movie_length)
                
                count=0
                for phrase in phrases:
                    if len(phrase) <= 3:
                        count+=1
                    else:
                        continue
                short_p=(count/len(phrases))*100
                
                #testo del film in token di parole
                words=nltk.word_tokenize(text)
                for word in words:
                    if len(word) <= 1:
                        words.remove(word)
                #lunghezza media di parole per film   
                w_lenghts=[]
                for word in words:
                    w_lenghts.append(len(word))
                
                media=sum(w_lenghts)/len(words)
                avg=round(media,2)  
                
                
                #testo del film con token di parole, diviso per frasi
                tokenized_phrases=[]
                for phrase in phrases:
                    split_phrase=phrase.split(' ')
                    tokenized_phrases.append(split_phrase)
                
                #lunghezza media della frase per film (contando i token)
                phrases_len=[]
                for element in tokenized_phrases:
                    phrases_len.append(len(element))
                
                mean_phr=round(sum(phrases_len)/len(tokenized_phrases),2)
                
                #lunghezza media delle parole per frase
                
                len_w=[]
                for phrase in tokenized_phrases:
                    w_len_phr=[]
                    for word in phrase:
                        w_len_phr.append(len(word))
                    #print(w_len_phr)
                    len_w.append(w_len_phr) 
    
                mean_per_phr=[]
                for phrase in len_w:
                    m=sum(phrase)/len(phrase)
                    mean_per_phr.append(m)
    
                avg_wlen_phr=round(sum(mean_per_phr)/len(mean_per_phr),2)
                
                
                #conteggio aggettivi e avverbi
                tokens = nltk.word_tokenize(text)
                text = nltk.Text(tokens)
                tags = nltk.pos_tag(text)
                
                counts = Counter(tag for word,tag in tags)
                
                adj=counts['JJ']
                adv=counts['RB']
                
                
                x=dirpath.split('\\')
                decade=x[-1]
                            
                if x[7]== 'Disney':
                    house=x[7]
                    category=x[8]
                else:
                    house=x[7]
                    category='Animation'
                
        
                #house=x[len(x)-2]
                #year=x[len(x)-1]
                
                s=file.split('.')
                title=s[0]
                year=s[1]
                
                row=[title, house, decade, year, category, movie_length, avg, mean_phr,avg_wlen_phr, adj, adv, short_p]
                
                
                my_writer.writerow(row)
  
    
    
    

"""questa parte non è da eseguire """         
              
#folder=r"C:\Users\Amministratore\Desktop\MASTER\Progettone\clean_subtitles"                
                
#def count_movies(folder):
#    count = 0
#    for r, d, files in os.walk(folder):
#        count += len(files)
     
#    return count       

#print(count_movies(folder))       

            