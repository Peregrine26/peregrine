#include <iostream>
#include <fstream>
#include <string>
#include <map>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "用法: " << argv[0] << " <日志文件路径>" << std::endl;
        return 1;
    }
    std::ifstream infile(argv[1]);
    if (!infile) {
        std::cerr << "无法打开文件: " << argv[1] << std::endl;
        return 1;
    }
    std::map<std::string, int> cmd_count;
    std::string line;
    while (std::getline(infile, line)) {
        if (!line.empty()) {
            ++cmd_count[line];
        }
    }
    for (const auto& pair : cmd_count) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    return 0;}
