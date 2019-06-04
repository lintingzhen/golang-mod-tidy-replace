# Golang-mod-tidy-replace
---
根据go mode tidy命令输出的timeout信息，将需翻墙访问的url提取出来，生成对应的replace信息，最后加到go.mod文件中。

```
mini→ hugo$ go mod tidy
go: finding github.com/golang/sync v0.0.0-20190423024810-112230192c58
go: finding github.com/golang/appengine v1.6.0
go: finding github.com/golang/text v0.3.1-0.20181227161524-e6919f6577db
go: finding github.com/golang/sys v0.0.0-20190530182044-ad28b68e88f1
go: finding github.com/golang/text v0.3.2
go: finding github.com/golang/image v0.0.0-20190523035834-f03afa92d3ff
go: finding github.com/golang/genproto v0.0.0-20190522204451-c2c4e71fbf69
go: github.com/golang/genproto@v0.0.0-20190522204451-c2c4e71fbf69: git fetch -f https://github.com/golang/genproto refs/heads/*:refs/heads/* refs/tags/*:refs/tags/* in /Users/lintingzhen/private/programming/go/pkg/mod/cache/vcs/554bf689757e745c8262a4a10b7dd8c4232573b1ec71e508da98c7c683bbdb05: exit status 128:
    fatal: could not read Username for 'https://github.com': terminal prompts disabled
go: finding go.opencensus.io v0.15.0
go: google.golang.org/grpc@v1.21.0: unrecognized import path "google.golang.org/grpc" (https fetch: Get https://google.golang.org/grpc?go-get=1: EOF)
go: golang.org/x/net@v0.0.0-20190522155817-f3200d17e092: unrecognized import path "golang.org/x/net" (https fetch: Get https://golang.org/x/net?go-get=1: EOF)
go: golang.org/x/time@v0.0.0-20190308202827-9d24e82272b4: unrecognized import path "golang.org/x/time" (https fetch: Get https://golang.org/x/time?go-get=1: EOF)
go: google.golang.org/grpc@v1.20.1: unrecognized import path "google.golang.org/grpc" (https fetch: Get https://google.golang.org/grpc?go-get=1: EOF)
go: golang.org/x/xerrors@v0.0.0-20190410155217-1f06c39b4373: unrecognized import path "golang.org/x/xerrors" (https fetch: Get https://golang.org/x/xerrors?go-get=1: net/http: TLS handshake timeout)
go: golang.org/x/net@v0.0.0-20190424112056-4829fb13d2c6: unrecognized import path "golang.org/x/net" (https fetch: Get https://golang.org/x/net?go-get=1: EOF)
go: finding github.com/google/go-cmp v0.2.0
go: finding github.com/golang/net v0.0.0-20190501004415-9ce7a6920f09
go: google.golang.org/api@v0.5.0: unrecognized import path "google.golang.org/api" (https fetch: Get https://google.golang.org/api?go-get=1: EOF)
go: finding github.com/golang/sys v0.0.0-20190222072716-a9d3bda3a223
go: golang.org/x/oauth2@v0.0.0-20190402181905-9f3314589c9a: unrecognized import path "golang.org/x/oauth2" (https fetch: Get https://golang.org/x/oauth2?go-get=1: EOF)
go: google.golang.org/genproto@v0.0.0-20190307195333-5fe7a883aa19: unrecognized import path "google.golang.org/genproto" (https fetch: Get https://google.golang.org/genproto?go-get=1: EOF)
go: golang.org/x/net@v0.0.0-20181023162649-9b4f9f5ad519: unrecognized import path "golang.org/x/net" (https fetch: Get https://golang.org/x/net?go-get=1: EOF)
go: google.golang.org/genproto@v0.0.0-20190425155659-357c62f0e4bb: unrecognized import path "google.golang.org/genproto" (https fetch: Get https://google.golang.org/genproto?go-get=1: EOF)
go: finding github.com/Azure/azure-sdk-for-go v21.3.0+incompatible
go: golang.org/x/net@v0.0.0-20190311183353-d8887717615a: unrecognized import path "golang.org/x/net" (https fetch: Get https://golang.org/x/net?go-get=1: EOF)
go: finding github.com/golang/oauth2 v0.0.0-20190523182746-aaccbc9213b0
go: finding github.com/golang/xerrors v0.0.0-20190513163551-3ee3066db522
go: golang.org/x/net@v0.0.0-20190420063019-afa5a82059c6: unrecognized import path "golang.org/x/net" (https fetch: Get https://golang.org/x/net?go-get=1: EOF)
go: finding github.com/golang/sys v0.0.0-20190502145724-3ef323f4f1fd
go: golang.org/x/crypto@v0.0.0-20190422183909-d864b10871cd: unrecognized import path "golang.org/x/crypto" (https fetch: Get https://golang.org/x/crypto?go-get=1: net/http: TLS handshake timeout)
go: finding github.com/fortytw2/leaktest v1.2.0
go: finding pack.ag/amqp v0.8.0
go: golang.org/x/sys@v0.0.0-20190422165155-953cdadca894: unrecognized import path "golang.org/x/sys" (https fetch: Get https://golang.org/x/sys?go-get=1: net/http: TLS handshake timeout)
go: finding github.com/Azure/go-autorest v11.0.0+incompatible
go: google.golang.org/grpc@v1.19.0: unrecognized import path "google.golang.org/grpc" (https fetch: Get https://google.golang.org/grpc?go-get=1: EOF)
go: google.golang.org/genproto@v0.0.0-20190508193815-b515fa19cec8: unrecognized import path "google.golang.org/genproto" (https fetch: Get https://google.golang.org/genproto?go-get=1: EOF)
go: finding github.com/kisielk/errcheck v1.1.0
go: cloud.google.com/go@v0.39.0: unrecognized import path "cloud.google.com/go" (https fetch: Get https://cloud.google.com/go?go-get=1: net/http: TLS handshake timeout)
go: golang.org/x/crypto@v0.0.0-20181001203147-e3636079e1a4: unrecognized import path "golang.org/x/crypto" (https fetch: Get https://golang.org/x/crypto?go-get=1: net/http: TLS handshake timeout)
go: golang.org/x/sys@v0.0.0-20181128092732-4ed8d59d0b35: unrecognized import path "golang.org/x/sys" (https fetch: Get https://golang.org/x/sys?go-get=1: net/http: TLS handshake timeout)
go: golang.org/x/tools@v0.0.0-20190422233926-fe54fb35175b: unrecognized import path "golang.org/x/tools" (https fetch: Get https://golang.org/x/tools?go-get=1: net/http: TLS handshake timeout)
go: golang.org/x/image@v0.0.0-20180708004352-c73c2afc3b81: unrecognized import path "golang.org/x/image" (https fetch: Get https://golang.org/x/image?go-get=1: EOF)
go: error loading module requirements

mini→ golang-mod-tidy-replace$ pbpaste | python main.py
replace cloud.google.com/go v0.39.0 => github.com/googleapis/google-cloud-go v0.39.0
replace golang.org/x/crypto v0.0.0-20181001203147-e3636079e1a4 => github.com/golang/crypto v0.0.0-20181001203147-e3636079e1a4
replace golang.org/x/crypto v0.0.0-20190422183909-d864b10871cd => github.com/golang/crypto v0.0.0-20190422183909-d864b10871cd
replace golang.org/x/sys v0.0.0-20181128092732-4ed8d59d0b35 => github.com/golang/sys v0.0.0-20181128092732-4ed8d59d0b35
replace golang.org/x/sys v0.0.0-20190422165155-953cdadca894 => github.com/golang/sys v0.0.0-20190422165155-953cdadca894
replace golang.org/x/tools v0.0.0-20190422233926-fe54fb35175b => github.com/golang/tools v0.0.0-20190422233926-fe54fb35175b
replace golang.org/x/xerrors v0.0.0-20190410155217-1f06c39b4373 => github.com/golang/xerrors v0.0.0-20190410155217-1f06c39b4373
```
