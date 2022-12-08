#!/usr/bin/env bash

XWI_OUT=$(xwininfo  | grep 'xwininfo: Window id:')
WINDOW_ID=$(echo $XWI_OUT | awk '{print $4}')
echo "recording window $XWI_OUT"
echo "window ID is $WINDOW_ID"
ffmpeg -y -f x11grab -window_id $WINDOW_ID -framerate 60 -i :0.0 out.mpg 
