#!/usr/bin/env python3

import subprocess
import sys
import time

def get_x11_window_ids():
    xprop_output = subprocess.run(["xprop", "-root"], capture_output=True)
    lines = xprop_output.stdout.splitlines()

    # we're looking for a line of output that looks like this:
    # _NET_CLIENT_LIST_STACKING(WINDOW): window id # 0x1c00002, 0x120002d, 0x1000002
    PATTERN = b"_NET_CLIENT_LIST_STACKING(WINDOW): window id # "
    net_client_list_output = [ s[len(PATTERN):] for s in lines if s.startswith(PATTERN) ]

    if len(net_client_list_output) == 0:
        print(f"I couldn't find the pattern '{PATTERN}' in the output of 'xprop -root', giving up.")
        sys.exit(1)
    if len(net_client_list_output) > 1:
        print(f"Multiple lines of output matched '{PATTERN}' in the output of 'xprop -root', giving up.")
        sys.exit(1)

    window_id_str = net_client_list_output[0]
    return window_id_str.split(b", ")

def watch_for_window(cmd, delay=0.5):
    """ This dodgy boi keeps looking for window IDs until one appears, and then
    assumes that's the window you want to record.

    Note that there's a delay kludge of 0.5s: it seems like sometimes multiple windows get opened
    """
    window_ids_before = set(get_x11_window_ids())
    # print('window_ids_before', window_ids_before)

    # run command
    # subprocess.run(cmd)

    new_windows = set()
    process = subprocess.Popen(cmd)
    # print(f'started process {process.pid}')

    # kludge: wait a bit so we get the right window
    # The better way to do this would be to keep polling until no more windows
    # are appearing, and then take the latest.
    time.sleep(delay)

    while not new_windows:
        window_ids_after = set(get_x11_window_ids())
        new_windows = window_ids_after - window_ids_before
        # print('window_ids_after', window_ids_after)

        if process.poll() is not None:
            # process died early, return nothing.
            break

    return process, new_windows


if __name__ == "__main__":
    cmd = sys.argv[1:]
    # print('I am going to run this command: ', cmd)

    process, window_ids = watch_for_window(cmd)
    for w in window_ids:
        print(w.decode("utf-8"))

    print('window_ids', window_ids)
    window_id = list(window_ids)[0].decode("utf-8")
    record_cmd = ["ffmpeg", "-y", "-f", "x11grab", "-window_id", window_id, "-framerate", "60", "-i", ":0.0", "out.mpg"]
    subprocess.run(record_cmd)
    process.wait()
