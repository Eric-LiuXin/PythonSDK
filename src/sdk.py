import time, datetime, pytz, calendar, decimal


############## 时间接口 START ##############
# 描述：获取时间戳
# 输入：
# 输出：int
def get_ts():
    return int(round(time.time() * 1000))


# 描述：简单格式化
# 输入：int
# 输出：str
def format_ts(dt, lite=False):
    if lite:
        return dt.strftime("%Y%m%d%H%M%S")
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# 描述：时间戳格式化 到秒
# 输入：int
# 输出：str
def time_ts(ts, show_s=False):
    """
    转毫秒为可读时间
    """
    if not ts:
        return ""
    if type(ts) == str:
        return ts
    return (
        datetime.datetime.utcfromtimestamp(ts / 1000.0)
        .astimezone(pytz.timezone("Asia/Shanghai"))
        .strftime("%Y-%m-%d %H:%M:%S" if show_s else "%Y-%m-%d %H:%M")
    )


# 描述：时间戳格式化 到日
# 输入：int
# 输出：str
def date_ts(ts, lite=False):
    if not ts:
        return ""
    return (
        datetime.datetime.utcfromtimestamp(ts / 1000.0)
        .astimezone(pytz.timezone("Asia/Shanghai"))
        .strftime("%Y-%m-%d" if lite else "%Y{y}%m{m}%d{d}")
        .format(y="年", m="月", d="日")
    )


# 描述：字符串转时间
# 输入：str
# 输出：datetime
def ts_dt(ts, back_to_future=False):
    if not ts:
        ts = "9999-12-31 00:00:00" if back_to_future else "1988-05-17 00:00:00"
    return datetime.datetime.strptime("%s +0800" % ts, "%Y-%m-%d %H:%M:%S %z")


# 描述：当前时间，上海时区
# 输入：
# 输出：datetime
def now_dt():
    return datetime.datetime.now(pytz.timezone("Asia/Shanghai"))


# 描述：当前时间，上海时区
# 输入：
# 输出：str
def now_ts(lite=False):
    return format_ts(now_dt(), lite)


# 描述：获取时间戳
# 输入：
# 输出：int
def get_timestamp(mode="m"):
    if mode == "s":
        return calendar.timegm(datetime.datetime.utcnow().utctimetuple()) * 1000
    return int(time.time() * 1000)


############## 时间接口 END ##############


############## 数据处理 START ##############
# 描述：转百分数
# 输入：int/float
# 输出：str
def float2percentage(value, n=2):
    try:
        v = format(float(value) * 100, ".%sf" % n)
    except:
        return value
    return "%s%%" % v


# 描述：数据小数位处理， 默认四舍五入，两位小数
# 输入：int/float
# 输出：decimal.Decimal
def round_value(f, n=2, type="ROUND_HALF_UP"):
    type_list = [
        "ROUND_HALF_UP",  # 四舍五入
        "ROUND_UP",  # 向上进位
        "ROUND_DOWN",  # 去尾保留
    ]
    context = decimal.getcontext()
    context.rounding = type if type in type_list else "ROUND_HALF_UP"
    return round(decimal.Decimal(str(f), context), int(n))


############## 数据处理 END ##############
