#!/bin/bash

WEBHOOK_URL="https://hooks.slack.com/services/AAA/BBB/CCC"
DOCKER_CONTAINER="container"
SCRIPT_PATH="/home/ubuntu"
INTERVAL=2


sudo docker container logs "${DOCKER_CONTAINER}" 2>&1 |"${SCRIPT_PATH}"/req_monitor.py "${INTERVAL}" "${WEBHOOK_URL}"