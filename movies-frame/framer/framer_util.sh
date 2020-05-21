#!/bin/bash

FILE=$1
FOLDER_DEST=$2

START_OFFSET=60
STOP_OFFSET=360

DURATION=$(ffprobe -v 0 -show_entries format=duration -of compact=p=0:nk=1 $FILE)
#echo $DURATION

# if short movie, reduce offsets 
if [ ${DURATION%.*} -le 600 ]  # cast float to int
then 
    START_OFFSET=30
    STOP_OFFSET=15
fi 
#echo $START_OFFSET
#echo $STOP_OFFSET

STOP=$(echo "$DURATION - $STOP_OFFSET" | bc)
#echo $STOP

# generate frames by sampling 1 frame per 720 frames (720 = 24 fps * 30 s)
ffmpeg -ss $START_OFFSET -t $STOP -i $FILE -vf "scale=640:-2,  thumbnail=720" -vsync 0 -f image2 ./$FOLDER_DEST/image-%3d.png
