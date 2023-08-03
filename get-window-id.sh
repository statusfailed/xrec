#!/usr/bin/env bash

# Interactively obtain a window's ID by clicking it with the mouse.
XWI_OUT=$(xwininfo  | grep 'xwininfo: Window id:')
WINDOW_ID=$(echo $XWI_OUT | awk '{print $4}')
echo $WINDOW_ID
