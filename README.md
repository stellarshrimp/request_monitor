# Req_monitor

req_monitor is a python script to monitor GET and POST requests in logs of the specific container using SLACK

## Usage

- set WEBHOOK_URL variable to desired webhook url in req_start.sh file
- set DOCKER_CONTAINER variable to desired container name 
- schedule req_start.sh in cron:
0 */2 * * * /home/ubuntu/req_start.sh >/dev/null 2>&1