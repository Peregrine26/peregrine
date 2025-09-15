#!/bin/bash

echo "编译 task3-/cmd_analyzer.cpp..."
g++ ../task3-/cmd_analyzer.cpp -o ../task3-/cmd_analyzer
if [ $? -ne 0 ]; then
    echo "编译失败"
    exit 1
fi

echo "运行 cmd_analyzer..."
../task3-/cmd_analyzer ../task3-/commands.log
