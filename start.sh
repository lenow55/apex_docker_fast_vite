#!/bin/bash
if [[ $1 = "dev" ]]
then
    docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
fi
if [[ $1 = "build" ]]
then
    docker-compose -f docker-compose.yml up --build
fi

