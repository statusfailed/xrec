# Some notes

[How to find X11 window IDs](https://stackoverflow.com/questions/252906/how-to-get-the-list-of-open-windows-from-xserver/1017932#1017932)

    xprop -root|grep ^_NET_CLIENT_LIST

[How to record a window by its ID with `ffmpeg`](https://stackoverflow.com/questions/62649524/how-can-i-record-a-window-using-ffmpeg-by-id)

    ffmpeg -y -s 800x600 -f x11grab -window_id 0x3200008 -framerate 30 -i :11.0+0,0 -c:v libx264 -preset ultrafast -crf 40 output_select_window.mp4

This works for me:

    ffmpeg -y -f x11grab -window_id $WINDOW_ID -framerate 30 -i :0.0 out.mpg 

See record-window.sh for a script version of this that allows selecting the
window with the mouse. It's something like this:

    #!/usr/bin/env bash

    XWI_OUT=$(xwininfo  | grep 'xwininfo: Window id:')
    WINDOW_ID=$(echo $XWI_OUT | awk '{print $4}')
    echo "recording window $XWI_OUT"
    echo "window ID is $WINDOW_ID"
    ffmpeg -y -f x11grab -window_id $WINDOW_ID -framerate 60 -i :0.0 out.mpg 

Note that we needed to use xwininfo to get the ID.

    xwininfo  | grep 'xwininfo: Window id:' | awk '{print $(NF - 1)}' 

On Arch Linux, this requires installing the xorg-xwininfo package.

# Formats

[this thread](https://forum.videohelp.com/threads/404503-ffmpeg-x11grab-capture-on-Xubuntu-Linux-fails)

gives this incantation for using x264:

    ffmpeg -video_size 1920x1080 -framerate 24 -f x11grab -i :0.0 -c:v h264_nvenc -qp 0 ~/Desktop/video.mp4

you can easily change that to use libwebp too (make sure to `pacman -S libwebp`)

    ffmpeg -video_size 1920x1080 -framerate 24 -f x11grab -i :0.0 -c:v libwebp -qp 0 ~/Desktop/video.mp4

# webp

[This post](https://stackoverflow.com/questions/68664693/trying-to-convert-an-mp4-to-webp-with-ffmpeg-with-different-lossless-compression)
suggests just letting ffmpeg pick all the options- it seems to work pretty well.
