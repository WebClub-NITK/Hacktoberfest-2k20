#!/bin/bash
/usr/local/bin/gunicorn --log-level DEBUG --preload -w 3 -b :8080 -t 600 application.app:app
