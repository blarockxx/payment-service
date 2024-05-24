# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["python", "app.py"]

# --------------------------------------
# 使用官方 Python 3.9 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制所有应用代码到容器中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# 暴露应用运行的端口
EXPOSE 5003

# 运行测试
RUN python -m unittest discover -s tests || { echo 'Tests failed' ; exit 1; }

# 启动应用
CMD ["python", "app.py"]
