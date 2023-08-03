# 🔴XREC

A collection of kludges for recording screen/windows on X11.

- `xrec.py`: launch a command, wait for it to spawn a new window, then try to
  record it with ffmpeg
- `record-window.sh`: record a specified window by clicking it
- `get-window-id.sh`: Get a window's ID by clicking it with the mouse
- `set-window-size.sh`: Set

`record-screen.sh` shows how to record the whole screen, but it hardcodes the
screen size so you probably don't want to use it.

# xrec.py

Example usage:

    xrec.py ./my-program.sh

Waits 0.5s for my-program to create a window, then records it with ffmpeg

# Recording open windows

If you want to record a window which is already open by selecting it with the
mouse, use one of the following:

**Record a webp (no audio)**:

    ./record-window.sh

**Record a webm (audio recorded from microphone)**:

    ./record-audio-window.sh

# Modifying open windows

Sometimes, you want your resulting video to be a specific resolution.
These utils help you set a window's size to exactly the resolution you want.

**Get a window's ID interactively**:

    ./get-window-id.sh

**Set a window's size to 800x600 interactively**:

    ./set-window-size $(./get-window-id.sh) 800 600

# Dependencies

- wmctrl
- xwininfo
- awk
- ffmpeg
- python
