import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))


from bootstrap import DATA_PATH as RAW_DATA_PATH

def read_raw_data():
    txt = RAW_DATA_PATH.read_text()
    return txt






if __name__ == "__main__":
    txt = read_raw_data()
    print(len(txt), 'chars')
