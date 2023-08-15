#检测方式 
# 0->平均值
# 1->像素数量
judgeMethod=1
#检测阈值(百分比)(两种方法都可以)
launchThreshold=90
#原神游戏路径(不要去动那个r)
launchPath=r"A:\yuanshen_setup_20230619213504.exe"
#程序进程名字(不一定全部匹配)
procressName="原神"
#延时(不要设置太高或者太低了,推荐0.05~0.5)
judgeDelay=0.1
#重新设置图片分辨率(设置小一点可以降低CPU占用)
imageSize=(1920,1080)
#自定义启动声音(推荐填写绝对路径,默认是“原神，启动！”,
# 留空注意不要去掉两个双引号)
launchSound=""
#延迟播放音频(可以自己微调)
soundDelay=0
#触发一次以后再触发的时延(单位是秒)
antiRelaunch=25
#启动参数,默认为空
#如果要全屏启动非全屏的原神可以试试加上(注意，不包括前面的井号,并且不要去掉双引号
#-screen-fullscreen 0
launchArgs=""