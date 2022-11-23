# encoding:utf-8
import os
import sys
from dtsdk.sdk import DTException, DTAnalytics, BatchConsumer, AsyncBatchConsumer, DebugConsumer, DTIllegalDataException
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

dt = DTAnalytics(AsyncBatchConsumer(app_id="app_id_xxxx", token="xxxxxxxxxxxxxxxxxxxxxxx",server_url="https://test.roiquery.com/sync"))
#dt =DTAnalytics(BatchConsumer(app_id="app_id_xxxx", token="xxxxxxxxxxxxxxxxxxxxxxx"), debug=True)
dt.enable_log(True) # 如果您想看log，请打开log标志
common = {"#os":"android","app_version":"2.1"}
dt.set_super_properties(common)
properties = {
    "#event_time":1669022011679,
    # 选填，设置这条event发生的时间戳，13位，精确到毫秒，如果不设置的话，则默认是当前时间，建议加上
    "$ip":"192.168.123.123",
    # 选填，设置用户的IP（非服务器的IP），DT会自动根据该IP解析所属国家，如果不设置的话，则默认无，建议加上
    "#event_syn": "xxx",
    # 选填，事件序列ID，字符串类型，重传的时候可以用于去重，窗口期1小时，建议加上
    "sku":"xxx", # 自定义内容
    "price":15, # 自定义内容
    "order":"订单号xxx" # 自定义内容
}
dt.track(dt_id="aaaa",acid='ddd$fff',event_name="purchase",properties=properties)

dt.flush()
dt.close()

