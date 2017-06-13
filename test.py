#需要先做数据预处理，处理完后再使用
import pandas as pd
import xgboost as xg
import os

base_path = "/media/root/Entertainment/zrx_workspace/human_resource_format2016"

zhongrong_in_file = "zhongrong_in.xlsx"
fangyuan_in_file = "fangyuan_in.xlsx"
fangyuan_out_file = "fangyuan_out.xlsx"
sort_excel_file = "sort.xlsx"

zhongrong_in_path = os.path.join(base_path,zhongrong_in_file)

fangyuan_in_path = os.path.join(base_path,fangyuan_in_file)
fangyuan_out_path = os.path.join(base_path,fangyuan_out_file)
sort_file_path = os.path.join(base_path,sort_excel_file)

zhongrong_data = pd.read_excel(zhongrong_in_path)
fangyuan_in_data = pd.read_excel(fangyuan_in_path)
fangyuan_out_data = pd.read_excel(fangyuan_out_path)
sort_file_data = pd.read_excel(sort_file_path)


print("a")


