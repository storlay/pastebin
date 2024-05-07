#!/bin/bash

if [[ "${1}" == "worker" ]]; then
    celery -A pastebin worker -l warning
elif [[ "${1}" == "flower" ]]; then
    celery -A pastebin flower
elif [[ "${1}" == "beat" ]]; then
    celery -A pastebin beat -l warning
fi