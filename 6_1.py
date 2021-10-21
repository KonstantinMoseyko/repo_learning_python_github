# 6_1

file_parsing_logs = open('nginx_logs.txt', 'r', encoding='utf-8')
result = ((one_line.split()[0], one_line.split()[5][1:], one_line.split()[6])for one_line in file_parsing_logs)
result_logs = [val for val in result]
print(result_logs)
file_parsing_logs.close()
