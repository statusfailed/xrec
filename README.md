# 🔴XREC

A collection of kludges for recording screen/windows on X11.

- `xrec.py`: launch a command, wait for it to spawn a new window, then try to
  record it with ffmpeg
- `record-window.sh`: record a specified window by clicking it

`record-screen.sh` shows how to record the whole screen, but it hardcodes the
screen size so you probably don't want to use it.

Example usage:

    xrec.py ./my-program.sh

Waits 0.5s for my-program to create a window, then records it with ffmpeg
