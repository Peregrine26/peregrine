导入必要的模块（sys、collections.deque）

函数 read_map(file_path):
    打开文件 file_path
    读取所有行
    初始化空列表 map_grid
    对于每一行 in 行列表:
        去除行首尾空白符
        按空格分割行得到数字列表
        将数字列表中的每个元素转换为整数，并添加到 map_grid
    返回 map_grid

函数 bfs(map_grid, start_x, start_y, goal_x, goal_y):
    获取地图的行数 rows 和列数 cols
    初始化 visited 矩阵（大小与地图相同），所有元素为 False
    初始化 parent 字典，用于记录每个节点的父节点
    初始化队列 queue
    将起点 (start_x, start_y) 加入队列
    标记 visited[start_y][start_x] 为 True
    设置 parent[(start_x, start_y)] 为 None

    定义移动方向 directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 右、左、下、上

    当队列不为空时:
        出队当前节点 (x, y)
        如果 (x, y) 等于 (goal_x, goal_y):
            跳出循环
        对于每个方向 (dx, dy) in directions:
            计算邻居坐标 nx = x + dx, ny = y + dy
            如果 nx 和 ny 在地图范围内（0<=nx<cols, 0<=ny<rows）:
                如果地图[ny][nx] 为 0 且 visited[ny][nx] 为 False:
                    标记 visited[ny][nx] 为 True
                    设置 parent[(nx, ny)] = (x, y)
                    将 (nx, ny) 加入队列

    如果 visited[goal_y][goal_x] 为 True:
        初始化路径列表 path
        设置 current = (goal_x, goal_y)
        当 current 不为 None:
            将 current 加入 path
            设置 current = parent[current]
        反转 path 列表
        返回 path
    否则:
        返回 None

主函数 main():
    如果命令行参数数量不等于 6:
        打印使用说明："./program_name <map_file> <start_x> <start_y> <goal_x> <goal_y>"
        退出程序

    获取命令行参数：
        map_file = sys.argv[1]
        start_x = int(sys.argv[2])
        start_y = int(sys.argv[3])
        goal_x = int(sys.argv[4])
        goal_y = int(sys.argv[5])

    调用 read_map(map_file) 获取 map_grid

    检查起点和终点是否在地图范围内，如果不在，输出错误并退出（假设地图已知大小，这里省略范围检查细节）
    如果 map_grid[start_y][start_x] == 1:
        打印 "I can't go to the position ({goal_x},{goal_y})."
        退出
    如果 map_grid[goal_y][goal_x] == 1:
        打印 "I can't go to the position ({goal_x},{goal_y})."
        退出

    调用 bfs(map_grid, start_x, start_y, goal_x, goal_y) 获取路径 path

    如果 path 不为 None:
        创建输出网格 output_map，其中每个元素是地图对应位置的字符串形式（将整数转换为字符串）
        对于路径中的每个点 (x, y):
            设置 output_map[y][x] = '*'
        对于 output_map 的每一行:
            用空格连接行中的元素并打印
    否则:
        打印 "I can't go to the position ({goal_x},{goal_y})."

如果作为脚本运行，调用 main()
