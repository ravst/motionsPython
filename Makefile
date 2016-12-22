message.proto:
	curl "https://raw.githubusercontent.com/ravst/motionsFormat/6913cd1282f224a08f5f75be00d03fde4801d31a/message.proto" -o message.proto
message_pb2.py: message.proto
	protoc message.proto --python_out=.

