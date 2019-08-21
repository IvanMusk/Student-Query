
import json
import xlrd

def get_studentinfo():
    file = "student_info.xls"
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    nrows = table.nrows

    return_data = {}
    data = []

    for i in range(2, nrows-1):
        content = table.row_values(i)
        no = str(content[1])[:-2]
        name = content[0]
        total = content[6]
        proname = content[11]

        data = [name, total, proname]
        return_data[no] = data
    return return_data

# if __name__ == '__main__':
#     return_json = get_studentinfo()
#     data_str = json.dumps(return_json)
#     with open('student_info.json', 'w', encoding='utf-8') as f:
#         f.write(data_str)
#         f.close()
#     with open('student_info.json', 'r', encoding='utf-8') as f:
#         get_data = f.read()
#         f.close()
#     data_json = json.loads(get_data)
#     print(data_json['***'])