#!/bin/bash

current_time=$(date +"%H:%M")
end_time="18:00"

current_seconds=$(date +%s)
end_seconds=$(date -d "today 18:00" +%s)

remaining=$((end_seconds - current_seconds))

hours=$((remaining / 3600))
minutes=$(( (remaining % 3600) / 60 ))

echo "Current time: $current_time"
echo "Work day ends after $hours hours and $minutes minutes"
