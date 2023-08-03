#!/usr/bin/env bash

WINDOW_ID=$1
WIDTH=$2
HEIGHT=$3

echo WINDOW_ID: ${WINDOW_ID}
echo WIDTH: ${WIDTH}
echo HEIGHT: ${HEIGHT}

# -i interprets $WID as an ID (I think!)
# -e arguments are gravity,x,y,width,height
#     a value of -1 for x/y means "don't change"
wmctrl -i -r ${WINDOW_ID} -e "0,-1,-1,${WIDTH},${HEIGHT}"
