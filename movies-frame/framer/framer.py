
import os
import shutil
import re

SEPARATOR = '\n#############################################################\n'

MOVIES_FOLDER = 'movies'
FRAMES_FOLDER = 'movie_frames'

def get_ffmpeg_command(filename, dest_folder):
    #command = 'ffmpeg -i \'' + filename + '\' -ss 60 -r 0.03  -f image2 -vframes ' + NOF + ' ' + TMP_FOLDER + '/image-%3d.png'
    #command = 'ffmpeg -i ' + filename + ' -vframes ' + NOF + ' -f image2 ' + TMP_FOLDER + '/image-%3d.png'
    #command = 'ffmpeg -ss 60 -vf thumbnail=720 -vsync 0  -f image2 -vframes ' +  NOF +' -i \'' + filename + '\' ' + TMP_FOLDER + '/image-%3d.png'
    command = './framer_util.sh \'' + filename + '\' \'' + dest_folder + '\''
    print(command)
    return command + ' >/dev/null 2>&1'

def create_folder_tree():
    if os.path.exists(FRAMES_FOLDER):
        shutil.rmtree(FRAMES_FOLDER) # rimuovi la vecchia 'movie_frames'

    os.mkdir(FRAMES_FOLDER)

    for i in range(1930, 2010 + 1, 10):
        os.mkdir(FRAMES_FOLDER+'/'+str(i))

    return

def remove_spaces():
    for r, d, files in os.walk(MOVIES_FOLDER):
        for f in files:
            full_name = r + '/' + f
            new_full_name = r + '/' + re.sub("['\s]+", "_", f)
            os.rename(full_name, new_full_name)

    return

def count_movies():
    count = 0
    for r, d, files in os.walk(MOVIES_FOLDER):
        count += len(files)

    return count

def main():
    remove_spaces()
    create_folder_tree()
    tot_movies = count_movies()
    print("Movies to process:", tot_movies)

    count = 0
    for r, d, files in os.walk(MOVIES_FOLDER):
        for f in files:
            count += 1
            print(SEPARATOR)
            print('Processing', str(count) + '/' + str(tot_movies), f)
            
            filename = r + '/' + f
            frames_folder_dest = filename.replace(MOVIES_FOLDER, FRAMES_FOLDER)
            os.mkdir(frames_folder_dest)

            os.system(get_ffmpeg_command(filename, frames_folder_dest))

            print("frames generated:", len(os.listdir(frames_folder_dest)))

    return 0

if __name__ == "__main__":
    main()



