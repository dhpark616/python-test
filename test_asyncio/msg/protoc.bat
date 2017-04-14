@echo off

echo generating protobuf...
echo.

color 01
protoc.exe --python_out=..\src\msg msg_enum.proto
color 02
protoc.exe --python_out=..\src\msg msg_error.proto
color 03
protoc.exe --python_out=..\src\msg msg_struct.proto
color 04
protoc.exe --python_out=..\src\msg msg_type_api.proto
color 05
protoc.exe --python_out=..\src\msg msg_packet_api.proto

color 01
protoc.exe --csharp_out=.\cs_files msg_enum.proto
color 02
protoc.exe --csharp_out=.\cs_files msg_error.proto
color 03
protoc.exe --csharp_out=.\cs_files msg_struct.proto
color 04
protoc.exe --csharp_out=.\cs_files msg_type_api.proto
color 05
protoc.exe --csharp_out=.\cs_files msg_packet_api.proto

color 03
python fix_import.py ..\src\msg\msg_struct_pb2.py
color 05
python fix_import.py ..\src\msg\msg_packet_api_pb2.py

echo.
echo done.
pause