## <p align="center">📣 OpenCompass 2.0  环境初始化</p>

## 一、安装ubuntu（推荐22.04以上）
ubuntu镜像下载：https://ubuntu.com/download/desktop  
windows环境可以使用[WSL2](https://learn.microsoft.com/zh-cn/windows/wsl/install)

## 二、安装Anaconda或Miniconda
1. 下载[Miniconda](https://docs.anaconda.com/free/miniconda/)
<br>下载[Anaconda](https://www.anaconda.com/download/success)
2. 安装完成后，进入shell，执行 `conda init`
<br>如出现提示 `command not found` 则手动配置环境：
https://blog.csdn.net/weixin_38705903/article/details/86533863
<br>重启终端。执行 `conda info` 查看信息
3. 关闭base环境的自动激活
    ```bash
    conda config --set auto_activate_base false
    ```
4. 在用户目录下的.condarc文件中配置[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)：
    ```bash
    channels:
    - defaults
    show_channel_urls: true
    default_channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    custom_channels:
    conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
    ```
5. pip设置清华源，终端执行：
    ```bash
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```
## 三、准备 OpenCompass 运行环境
- 安装[git-lfs](https://packagecloud.io/github/git-lfs/install)(拉取大模型文件必备)
    ```
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    sudo apt-get install git-lfs
    git lfs install
    ```
- 配置github镜像加速(挂全局代理可以忽略)：
<br>https://mirror.ghproxy.com/
<br>https://kkgithub.com
- 配置huggingface镜像加速(挂全局代理可以忽略)：
    ```bash
    echo 'export HF_ENDPOINT="https://hf-mirror.com"' >> ~/.bashrc
    source ~/.bashrc
    ```
    镜像网站地址：https://hf-mirror.com/
- 安装hf-mirror-cli(解决git从huggingface镜像站上下载速度慢的问题)：
<br>https://github.com/wangshuai67/hf-mirror-cli.git
    ```python
    pip install hf-cli
    ```
## **mkl-service错误解决办法**
- 问题描述：[pytorch多卡训练](https://www.zywvvd.com/notes/study/deep-learning/bug-fix/mkl-service-err-message/mkl-service-err-message/) | [opencompass评测内容为空](https://github.com/open-compass/opencompass/issues/436)
- 错误信息：
  ```
  Error: mkl-service + Intel® MKL: MKL_THREADING_LAYER=INTEL is incompatible with libgomp.so.1 library. Try to import numpy first or set the threading layer accordingly. Set MKL_SERVICE_FORCE_INTEL to force it.
  ``` 
- 解决办法：
   ```bash
   echo 'export MKL_SERVICE_FORCE_INTEL=1' >> ~/.bashrc
   echo 'export MKL_THREADING_LAYER=GNU' >> ~/.bashrc
   source ~/.bashrc
   ```

