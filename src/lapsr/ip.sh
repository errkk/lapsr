#!/bin/sh

ifconfig | grep 192 | awk '{print $2}'
