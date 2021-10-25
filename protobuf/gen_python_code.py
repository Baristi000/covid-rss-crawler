import subprocess

subprocess.run([
    "python", "-m", "grpc_tools.protoc", "-I", ".",
    "--python_out=.", "--grpc_python_out=.",
    "--proto_path","protobuf","protobuf/train.proto","protobuf/serve.proto"
])

# python -m grpc_tools.protoc -I./protobuf --python_out=./protobuf/gencode --grpc_python_out=./protobuf/gencode protobuf/function.proto
# protoc --js_out=protobuf/js protobuf/function.proto
# protoc -I=./protobuf --js_out=import_style=commonjs:./client/src  --grpc-web_out=import_style=typescript,mode=grpcwebtext:./client/src ../protobuf/function.proto