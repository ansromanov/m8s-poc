# Usage

```sh
grpcurl -plaintext localhost:9000 list
```

The -plaintext flag is due to the fact that our local server has no TLS certificate yet. list lists all our registered service on our server. Our gRPC server is [localhost:9000](http://localhost:9000) You should see the following output.

```sh
grpcurl -plaintext localhost:9000 describe
```

Finally let's test our GetBook method by running the following

```sh
grpcurl -d '{"name": "To Kill a Mockingbird", "isbn": 12345}' -plaintext localhost:9000 book.BookService/GetBook
```
