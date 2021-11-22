# TensorFlowTTS 中文合成语音

## 配置环境

1. 安装 Anaconda3(Python 3.7+)
2. pip 配置清华大学镜像源，新建 C:/Users/username/pip/pip.ini 文件，然后记事本打开复制以下内容
   ```
   [global]
   index-url = https://pypi.tuna.tsinghua.edu.cn/simple
   [install]
   trusted-host = pypi.tuna.tsinghua.edu.cn
   ```
3. conda 配置清华大学镜像源，记事本打开 C:/Users/username/.condarc 文件，然后复制以下内容覆盖原内容
   ```
   channels:
     - defaults
   show_channel_urls: true
   channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
   default_channels:
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
   custom_channels:
     conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   ```
4. 创建虚拟环境
   ```bash
   $ conda create -n tts python=3.8
   ```
5. 切换虚拟环境
   ```bash
   $ conda activate tts
   ```

## 安装依赖

```bash
$ pip install TensorFlowTTS
$ pip install git+https://github.com/repodiac/german_transliterate
$ pip install jupyter ipython flask python-docx zhon cn2an
$ conda install cudatoolkit=10.1 cudnn=7.6.5
```

## 配置 nltk_data

将 doc/nltk_data 文件夹复制到 C:/Users/username/AppData/Roaming 文件夹下

## 解压 tacotron2

将 doc/model/tacotron2.zip 文件解压到 tts/model 文件夹

## 问题及解决方法

1. tensorflow.python.framework.errors_impl.AlreadyExistsError: Another metric with the same name already exists.
   ```bash
   # 降低 keras 版本
   $ pip install keras==2.6.*
   ```
