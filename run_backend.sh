#!/bin/bash

cd backend
source venv/bin/activate
granian shorty_link.asgi:application --interface asgi
