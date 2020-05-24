
# ricordarsi di installare i pacchetti :
###         pip install py-readability-metrics
###         python -m nltk.downloader punkt

from readability import Readability


output_file = '/Users/valeriaguttilla/Desktop/MASTER/PROGETTONE/ANALISI_TESTUALE/SOTTOTITOLI/DISNEY/Disney Animation/1950/Cinderella_1950.srt'
with open(output_file, 'r', encoding='utf-8', newline='\n') as output_handle:
    text = output_handle.read()


# se volete mettere un testo di prova
# text = ("""On a June day sometime in the early 1990s, encouraged by his friend and fellow economist Jörgen Weibull, Abhijit went swimming in the Baltic. He leaped in and instantly jumped out—he claims that his teeth continued to chatter for the next three days. In 2018, also in June, we went to the Baltic in Stockholm, several hundred miles farther north than the previous encounter. This time it was literally child’s play; our children frolicked in the water. ' \
#        Wherever we went in Sweden, the unusually warm weather was a topic of conversation. It was probably a portent of something everyone felt, but for the moment it was hard not to be quite delighted with the new opportunities for outdoor life it offered.""")



# per leggere il testo
r = Readability(text)


### Flesch-Kincaid Grade Level

fk = r.flesch_kincaid()
print('\n\nFlesch-Kincaid Grade Level score is {}'.format(fk.score))
print('Flesch-Kincaid Grade Level grade level is {}'.format(fk.grade_level))



### Flesch Reading Ease

f = r.flesch()
print('\n\nFlesch Reading Ease score is: {}'.format(f.score))
print('Flesch Reading Ease is: {}'.format(f.ease))
print('Flesch Reading Ease grade levels are: {}'.format(f.grade_levels))



### Dale Chall Readability

dc = r.dale_chall()
print('\n\nDale Chall Readability score is: {}'.format(dc.score))
print('Dale Chall Readability grade levels are: {}'.format(dc.grade_levels))



### Automated Readability Index (ARI)

ari = r.ari()
print('\n\nAutomated Readability Index (ARI) is: {}'.format(ari.score))
print('Automated Readability Index (ARI) grade levels are: {}'.format(ari.grade_levels))
print('Automated Readability Index (ARI) ages are:{}'.format(ari.ages))



### Coleman Liau Index

cl = r.coleman_liau()
print('\n\nColeman Liau Index score is: {}'.format(cl.score))
print('Coleman Liau Index grade level is: {}'.format(cl.grade_level))



### SMOG
# Da usare se il testo ha più di 30 frasi. Original formula is for at least 30 sentences, with all_sentences=True the limit is lifted, but doesn't work below 30 sentences

s = r.smog(all_sentences=True)
print('\n\nSMOG score is: {}'.format(s.score))
print('SMOG grade level is: {}'.format(s.grade_level))



### SPACHE

s = r.spache()
print('\n\nSPACHE score is: {}'.format(s.score))
print('SPACHE grade level is: {}'.format(s.grade_level))



### Linsear Write

lw = r.linsear_write()
print('\n\nLinsear Write score is: {}'.format(lw.score))
print('Linsear Write grade level is: {}'.format(lw.grade_level))