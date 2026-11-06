#!/bin/bash
# usage: serve.sh <dir> <port> <cmd...>
d=$1;port=$2;shift 2
python3 -m http.server $port -d "$d" >/dev/null 2>&1 & pid=$!
sleep 0.8; "$@"; r=$?; kill $pid; exit $r
