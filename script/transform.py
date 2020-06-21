from os import listdir
from os.path import isfile, join
import pandas as pd
from multiprocessing.pool import ThreadPool

def xlsx_to_csv(xlsx):
    try:
        read_file = pd.read_excel ('../data/xlsx/' + xlsx)
        file_name = xlsx.split('.')[0]
        read_file.to_csv('../data/csv/' + file_name + '.csv', index = None, header=True)
    except Exception as e:
        print(xlsx)
        print(e)
    return file_name

def xlsx_to_csv_multithread(xlsx_list):
    results = ThreadPool(10).imap_unordered(xlsx_to_csv, xlsx_list)
    for r in results:
        print(r)

def xlsx_to_json(xlsx):
    try:
        read_file = pd.read_excel ('../data/xlsx/' + xlsx)
        file_name = xlsx.split('.')[0]
        read_file.to_json(path_or_buf='../data/json/' + file_name + '.json', orient='records')
    except Exception as e:
        print(xlsx)
        print(e)
    return file_name


def xlsx_to_json_multithread(xlsx_list):
    results = ThreadPool(10).imap_unordered(xlsx_to_json, xlsx_list)
    for r in results:
        print(r)

def get_xlsx_file_name(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

if __name__ == "__main__":
    xlsx_list = get_xlsx_file_name('../data/xlsx/')
    xlsx_to_csv_multithread(xlsx_list)
    xlsx_to_json_multithread(xlsx_list)
