#!/bin/sh
cd audit/web || exit

tailwindcss -i static/main.css -o static/main.dist.css --watch
