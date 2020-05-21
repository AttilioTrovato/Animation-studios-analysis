
import csv
from cv2 import cv2
import os
import shutil

from collections import Counter
from sklearn.cluster import KMeans

SEPARATOR = '\n#############################################################\n'

FRAMES_FOLDER = 'movie_frames'
CENTROIDS_FOLDER = 'movie_centroids'
NUMBER_OF_CENTROIDS = 10

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_centroids(filename):
    image = get_image(filename)

    #modified_image = cv2.resize(image, (640, 480), interpolation = cv2.INTER_AREA)
    #modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    modified_image = image.reshape(image.shape[0]*image.shape[1], 3)

    clf = KMeans(n_clusters = NUMBER_OF_CENTROIDS)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i]/255 for i in counts.keys()]

    return ordered_colors

def create_folder_tree():
    if os.path.exists(CENTROIDS_FOLDER):
        shutil.rmtree(CENTROIDS_FOLDER) # rimuovi la vecchia 'movie_frames'

    os.mkdir(CENTROIDS_FOLDER)

    for i in range(1930, 2010 + 1, 10):
        os.mkdir(CENTROIDS_FOLDER + '/' + str(i))

    return

def main():
    create_folder_tree()

    field_names = ['frame_id', 'centroid_id', 'red', 'green', 'blue']

    for r, d, files in os.walk(FRAMES_FOLDER):
        if (len(files) == 0):
            continue

        print(SEPARATOR)
        print('Processing', r)

        centroids_filename = r.replace(FRAMES_FOLDER, CENTROIDS_FOLDER) + '.csv'
        print('File created:', centroids_filename)

        with open(centroids_filename, 'w') as w_fh:
            csv_writer = csv.writer(w_fh)
            csv_writer.writerow(field_names)

            f_id = 0
            for f in files:
                print('.', end = '')
                rgb_centroids = get_centroids(r + '/' + f)
                c_id = 0
                for c in rgb_centroids:
                    row = [f_id] + [c_id] + c.tolist()
                    csv_writer.writerow(row)
                    c_id += 1
                f_id += 1

    return 0

if __name__ == "__main__":
    main()



