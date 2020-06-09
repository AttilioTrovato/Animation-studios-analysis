import os
import re

spam_words_ci = ['resync', 'synched', 'synced', 'downloader', 'www.', 'subtitle']
def spam_line(line):
    if ('Sync' in line):
        return True
    lower_line = line.lower()
    for sw in spam_words_ci:
        if (sw in lower_line):
            return True
    return False

for r, d, files in os.walk('subtitles_spam'):
    for f in files:
        filename = r + '/' + f
        with open(filename, 'r', encoding='latin-1') as r_fh:
            new_filename = filename.replace('subtitles_spam', 'subtitles_no_spam')
            with open(new_filename, 'w', encoding='latin-1') as w_fh:
                for line in r_fh:
                    if (not spam_line(line)):
                        w_fh.write(line)