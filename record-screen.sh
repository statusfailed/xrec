#!/usr/bin/env bash

#SCREENSHOT=$(mktemp);
#trap '{ rm -f -- "$SCREENSHOT" }'

# see man ffmpeg section "X11 grabbing"
#   -f x11grab          record screen
#   -r 30               30 FPS recording
#   -i :0.0             select input? (X11 session)
#   -acodec libvorbis   make a .webm
#   -video_size         well duh
ffmpeg \
  -f x11grab  \
  -video_size 3840x2160 \
  -framerate 25 \
  -i :0.0 \
  out.mpg
