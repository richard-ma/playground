# 图片查找工具

# 目的
读取test.csv的文件，查找每行中image的文件是否在image目录中存在（文件名有可能包含中文）。
存在：将文件以code列命名移动到newimages目录中，并将记录写入newimages.csv文件中
不存在：将记录写入notfound.csv文件中
