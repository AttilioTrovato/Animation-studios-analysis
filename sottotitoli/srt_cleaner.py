import os
import re
import shutil

#set di patterns per individuare le linee e le stringhe da rimuovere
text_pattern = re.compile('[a-zA-Z]') # caratteri dalla a alla z, maiuscoli e minuscoli
text2_pattern = re.compile('\(.*?\)') # (qualsiasi_carattere_tra_queste_parentesi)
text3_pattern = re.compile('\[.*?\]') # [qualsiasi_carattere_tra_queste_parentesi]
text4_pattern = re.compile('[\<]+.*?[\>]+') # <qualsiasi_carattere_tra_queste_parentesi>
text5_pattern = re.compile('[\[\(].*|.*[\]\)]') # [or(qualsiasi_carattere or qualiasi_carattere)or]
text6_pattern = re.compile(' +') # più istanze di ' '
text7_pattern = re.compile('^-*\s*[^a-z]+:[^0-9]') # e.g. 'ZACH & CHAMP: ', 'DUCKY'S MOM: '
text8_pattern = re.compile('^-*\s*[A-Za-z]+:') # e.g. 'Remus:', '- Balto:'

source = 'subtitles_no_spam(still_not_clean)'
dest = 'clean_subtitles'

# r=root, d=directories, f = files
for r, d, files in os.walk(source): # lo script si aspetta nella stessa directory una cartella con nome 'subtitles'
    for f in files:
        filename = r + '/' + f
        print(filename)
        with open(filename, 'r', encoding='latin-1') as r_fh:
            clean_filename = filename.replace(source, dest)
            with open(clean_filename, 'w', encoding='latin-1') as w_fh:
                for line in r_fh:
                    # se non è una linea di testo o è vuota o è spam, passa alla linea successiva
                    if (re.search(text_pattern, line) == None or len(line) == 0):
                        continue

                    #rimuovi stringhe tra parentesi [(<
                    line = text2_pattern.sub(' ', line)
                    line = text3_pattern.sub(' ', line)
                    line = text4_pattern.sub(' ', line)
                    line = text5_pattern.sub(' ', line) # parentesi aperte e chiuse su due linee diverse

                    #rimpiazza più occorrenze di ' ' con un solo ' ', e rimuovi ' ' a inizio linea
                    line = text6_pattern.sub(' ', line)
                    if line.startswith(' '):
                        line = line[1:]
                    
                    #rimuovi i nomi di personaggi prima della battuta (e.g. - SONNY: Mom!)
                    line = text7_pattern.sub(' ', line)
                    line = text8_pattern.sub(' ', line)
                    line = line.replace('--','__').replace('-','')

                    #rimpiazza più occorrenze di ' ' con un solo ' ', e rimuovi ' ' a inizio linea
                    line = text6_pattern.sub(' ', line)
                    if line.startswith(' '):
                        line = line[1:]

                    if (len(line) > 0):
                        w_fh.write(line)