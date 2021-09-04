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


'''
## 工具与配置

### flake8

[`flake8`](https://flake8.pycqa.org/) 是一个结合了 pycodestyle，pyflakes，mccabe 检查 Python 代码规范的工具。


使用方法：

```bash
flake8 {source_file_or_directory}
```

在项目中创建 `setup.cfg` 或者 `tox.ini` 或者 `.flake8` 文件，添加 `[flake8]` 部分。

推荐的配置文件如下：

```ini
[flake8]
ignore =
    ;W503 line break before binary operator
    W503,
    ;E203 whitespace before ':'
    E203,

; exclude file
exclude =
    .tox,
    .git,
    __pycache__,
    build,
    dist,
    *.pyc,
    *.egg-info,
    .cache,
    .eggs

max-line-length = 120
```

如果需要屏蔽告警可以增加行内注释 `# noqa`，例如：

```python
example = lambda: 'example'  # noqa: E731
```

### pylint

[`pylint`](https://www.pylint.org/) 是一个能够检查编码质量、编码规范的工具。

配置项较多，单独一个配置文件配置，详情可查阅：[.pylintrc](https://git.code.oa.com/standards/python/blob/master/.pylintrc)

使用方法：

```bash
pylint {source_file_or_directory}
```

如果遇到一些实际情况与代码冲突的，可以在行内禁用相关检查，例如 ：

```python
try:
    do_something()
except Exception as ex:  # pylint: disable=broad-except
    pass
```

如果需要对多行的进行禁用规则，可以配套使用 `# pylint: disable=具体错误码`/`# pylint: enable=具体错误码`。

```python
# pylint: disable=invalid-name
这里的代码块会被忽略相关的告警
app = Flask(__name__)
# pylint: enable=invalid-name
```


### black

[`black`](https://github.com/psf/black) 是一个官方的 Python 代码格式化工具。

使用方法：

```bash
black {source_file_or_directory}
```

如果不想格式化部分代码，可以配套使用 `# fmt: off`/`# fmt: on` 临时关闭格式化。

```python
# fmt: off
在这的代码不会被格式化
# fmt: on
```

### EditorConfig

EditorConfig 可以帮助开发同一项目下的跨多 IDE 的开发人员保持一致编码风格。

在项目的根目录下放置
[`.editorconfig`](https://git.code.oa.com/standards/python/blob/master/.editorconfig)
文件，可以让编辑器规范文件对格式。参考配置如下：

```ini
# https://editorconfig.org

root = true

[*]
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
insert_final_newline = true
charset = utf-8
end_of_line = lf

[*.py]
max_line_length = 120

[*.bat]
indent_style = tab
end_of_line = crlf

[LICENSE]
insert_final_newline = false

[Makefile]
indent_style = tab
```

'''