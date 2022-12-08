#!/usr/bin/env bash

#SCREENSHOT=$(mktemp);
#trap '{ rm -f -- "$SCREENSHOT" }'

# see man ffmpeg section "X11 grabbing"
#   -f x11grab          record screen
#   -i :0.0             select input? (X11 session)
#   -video_size         hardcoded screen size (sorry)
ffmpeg \
  -f x11grab  \
  -video_size 3840x2160 \
  -framerate 25 \
  -i :0.0 \
  out.mpg
