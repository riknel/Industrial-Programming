#!/usr/bin/env bash

docker-compose up -d db queue
sleep 10
docker-compose up consumer producer
