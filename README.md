Example command: manim -p -ql first.py class_name Turn off your computer's security software if you have any permission_related problems during execution.g

项目架构说明： 项目名称： _创作年份: volume I 几何基础： 具体命题名称

关于执行命令：
    manim -p -ql first.py SquareToCircle 执行时如果出现权限相关的问题，把电脑的安全软件关一下

关于命令使用说明：
    manim -p -ql first.py SquareToCircle ： 运行first.py文件中的SquareToCircle类
    -p ： 表示渲染完毕后自动预览动画
    -ql ： 表示低质量（’quality low’）渲染动画，速度快但是画质不好，视频分辨率和帧率较低;480p分辨率
    -qh ： 高质量渲染（’quality high’）渲染动画，速度慢但是画质好，视频分辨率和帧率较高;720p分辨率
    -qm ： 中质量渲染（’quality medium’）渲染动画，速度一般，画质一般，视频分辨率和帧率适中。
    first.py ： 具体文件名
    class_name ： 具体命题名称

    手动指定分辨率：
            manim -p -r 1920,1080 test_2.py SquareToCircle ：-r手动指定分辨率为1920x1080，1080p分辨率
            manim -p -r 3840,2160 test_2.py SquareToCircle : -r手动指定分辨率为3840x2160，2160p分辨率,4k分辨率
    
    手动指定帧率：
            manim -p -ql -r 1920,1080 --fps 60 test_2.py SquareToCircle ：-f手动指定帧率为60，即每秒60帧,默认是15帧（15fps）



关于latex的安装：
    1.安装latex：https://blog.csdn.net/Nicolecocol/article/details/136968456
    2.注意manim.cfg文件中latex的路径是否正确
    3.若执行时出现‘RuntimeError: latex failed but did not produce a log file. Check your LaTeX installation.’的错误，可执行以下命令：
        cd C:\Users\xxxx\.texlive2024\texmf-var\web2c\pdftex 
                然后执行命令：fmtutil --all --force         # 重新生成格式文件
