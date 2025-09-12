#!/bin/bash

echo "编译 hello_robo.cpp..."
g++ hello_robo.cpp -o hello_robo
if [ $? -ne 0 ]; then
    echo "编译失败"
    exit 1
fi

echo "运行 hello_robo..."
./hello_robo
