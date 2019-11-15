#!/usr/bin/env bash

# Cleanup
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
echo "" > ~/.aws/temp_session

# Show all AWS profiles, select one, generate temp_session
python ~/.bin/aws-session-manager.py

# Source it for the current shell window
source ~/.aws/temp_session

echo "## Credentials set! ##"
