import os
import csv

CENTROIDS_FOLDER = 'centroids'
CSV_FILENAME = 'frame_centroids.csv'

header = [
    'movie_id',
    'movie_title',
    'year',
    'frame_id',
    'centroid_id',
    'red',
    'green', 
    'blue'
]

with open(CSV_FILENAME, 'w') as w_fh:
    csv_writer = csv.writer(w_fh)
    csv_writer.writerow(header)
    movie_id = 0

    for r, d, files in os.walk(CENTROIDS_FOLDER):
        for f in files:
            year = r.split('/')[-1]
            title = f[:-8] # cut '.avi.csv'

            with open(r + '/' + f, 'r') as r_fh:
                csv_reader = csv.reader(r_fh)
                next(csv_reader) # skip header

                for row in csv_reader:
                    new_row = [str(movie_id), title, year] + row
                    csv_writer.writerow(new_row)

            movie_id += 1

print('DONE')
