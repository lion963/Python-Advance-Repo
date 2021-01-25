import os
from os.path import join
path='C:\\Users\Yordana\Desktop'
name_file='report.txt'

report_dict={}
for root, dirs, files in os.walk('C:\\Users\Yordana\PycharmProjects\Python-Advance-Repo\Exercise File Handling'):
    for file in files:
        name, extension = file.split('.')
        if '.'+extension not in report_dict:
            report_dict['.'+extension]=[]
        report_dict['.'+extension].append(file)
report_dict=dict(sorted(report_dict.items(), key=lambda x: (x[0], x[1])))
report_file=open(join(path, name_file), 'w')
report_file.close()

report_file=open(join(path, name_file), 'a')
for key, values in report_dict.items():
    report_file.write(key)
    report_file.write('\n')
    for value in values:
        report_file.write(f'- - - {value}')
        report_file.write('\n')
report_file.close()