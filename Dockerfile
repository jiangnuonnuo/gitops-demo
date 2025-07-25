# 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .

# 设置环境变量
ENV PORT=6000
ENV PYTHONUNBUFFERED=1

# 暴露端口
EXPOSE 6000

# 启动命令
CMD ["python", "app.py"]