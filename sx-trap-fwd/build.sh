#!/bin/bash
VERSION=$1

if [ -z "$VERSION" ]
then
	echo "Usage: $0 <VERSION>"
	exit 1
fi

docker build -t "sx-trap-fwd:$VERSION" .
docker save -o sx_trap_fwd_$VERSION.tar.gz sx-trap-fwd:$VERSION