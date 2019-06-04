#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create Date: 2019-06-04 17:32:53
# Author: Tingzhen.Lin

import sys


uri_map = {
    "cloud.google.com/go": "github.com/googleapis/google-cloud-go",
    "golang.org/x/crypto": "github.com/golang/crypto",
    "golang.org/x/exp": "github.com/golang/exp",
    "golang.org/x/image": "github.com/golang/image",
    "golang.org/x/lint": "github.com/golang/lint",
    "golang.org/x/net": "github.com/golang/net",
    "golang.org/x/oauth2": "github.com/golang/oauth2",
    "golang.org/x/sync": "github.com/golang/sync",
    "golang.org/x/sys": "github.com/golang/sys",
    "golang.org/x/text": "github.com/golang/text",
    "golang.org/x/time": "github.com/golang/time",
    "golang.org/x/tools": "github.com/golang/tools",
    "golang.org/x/xerrors": "github.com/golang/xerrors",
    "google.golang.org/api": "github.com/googleapis/google-api-go-client",
    "google.golang.org/appengine": "github.com/golang/appengine",
    "google.golang.org/genproto": "github.com/google/go-genproto",
    "google.golang.org/grpc": "github.com/grpc/grpc-go",
}


def main():
    replaces = []
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break
        if line.find("timeout") == -1:
            continue
        pieces = line.split()
        mod = pieces[1]
        if mod[-1] == ':':
            mod = mod[:-1]
        uri, version = mod.split('@')
        replaces.append((uri, uri_map.get(uri, "Unknown"), version))
    replaces.sort()
    for uri, new_uri, ver in replaces:
        print "replace {uri} {ver} => {new_uri} {ver}".format(uri=uri, new_uri=new_uri, ver=ver)


if __name__ == '__main__':
    main()



