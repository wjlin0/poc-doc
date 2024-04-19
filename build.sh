#!/bin/bash
# 设置脚本路径为当前路径
cd `dirname $0`
rm -r docs  && mkdir -p docs && cd ./docs
git clone https://github.com/wy876/POC.git
cd POC && rm -rf .git && mv README.md ../../README.md && mv * ../
cd ../ && rm -r POC && cd ../
echo "当前目录：`pwd`"
echo "正在初始化远程仓库"
git add .
git commit -m "$(date '+%Y-%m-%d %H:%M')" 1>/dev/null 2>&1

git push origin main -f
exit_status=$?
if [[ $exit_status -eq 0 ]]; then
	echo "提交成功 -> https://poc.wjlin0.com"
else
	echo "提交失败: $exit_status"
fi

