FROM golang:1.15-alpine as builder

# Set necessary environmet variables needed for our image
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# RUN mkdir /app
# ADD main.go /app
WORKDIR /app
    
# Add this go mod download command to pull in any dependencies
COPY . .
RUN go mod download
# we run go build to compile the binary
# executable of our Go program
RUN go build -o main .
# Our start command which kicks off
# our newly created binary executable

WORKDIR /dist
RUN cp /app/main . 


FROM scratch
COPY --from=builder /dist/main /

# Command to run
ENTRYPOINT ["/main"]