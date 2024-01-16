# MGN
code for Multi-Directional Guidance Network for Fine-Grained Visual Classification
一、项目名称与简介
用于细粒度图像分类的多阶段多层次多特征融合网络
二、文件夹列表
模型：backbone.py、model.py
配置：config.py
数据集：datesets.py
训练：train.py

三、所需环境
Package                 Version
----------------------- --------------------
absl-py                 1.4.0
cachetools              4.2.4
certifi                 2022.6.15
charset-normalizer      2.0.12
click                   8.0.4
cycler                  0.11.0
dataclasses             0.8
decorator               4.4.2
docker-pycreds          0.4.0
filelock                3.4.1
gitdb                   4.0.9
GitPython               3.1.20
google-auth             2.16.2
google-auth-oauthlib    0.4.6
grpcio                  1.48.2
huggingface-hub         0.4.0
idna                    3.3
imageio                 2.15.0
importlib-metadata      4.8.3
importlib-resources     5.4.0
joblib                  1.1.1
jsonpatch               1.32
jsonpointer             2.3
kiwisolver              1.3.1
Markdown                3.3.7
matplotlib              3.3.4
networkx                2.5.1
numpy                   1.19.5
oauthlib                3.2.2
opencv-python           4.6.0.66
packaging               21.3
pandas                  1.1.5
pathtools               0.1.2
Pillow                  8.4.0
pip                     21.2.4
promise                 2.3
protobuf                3.19.4
psutil                  5.9.1
pyarrow                 6.0.1
pyasn1                  0.4.8
pyasn1-modules          0.2.8
pyparsing               3.0.9
python-dateutil         2.8.2
pytz                    2022.1
PyWavelets              1.1.1
PyYAML                  6.0
pyzmq                   23.2.0
requests                2.27.1
requests-oauthlib       1.3.1
rsa                     4.9
scikit-image            0.17.2
scikit-learn            0.24.2
scipy                   1.5.4
sentry-sdk              1.9.4
setproctitle            1.2.3
setuptools              49.6.0.post20210108
shortuuid               1.0.9
six                     1.16.0
smmap                   5.0.0
tensorboard             2.10.1
tensorboard-data-server 0.6.1
tensorboard-plugin-wit  1.8.1
tensorboardX            2.5.1
thop                    0.1.1.post2209072238
threadpoolctl           3.1.0
tifffile                2020.9.3
timm                    0.6.12
torch                   1.8.0+cu111
torchaudio              0.8.0
torchfile               0.1.0
torchvision             0.9.0+cu111
tornado                 6.1
tqdm                    4.64.0
typing_extensions       4.1.1
urllib3                 1.26.11
visdom                  0.1.8.9
wandb                   0.13.1
websocket-client        1.3.1
Werkzeug                2.0.3
wget                    3.2
wheel                   0.37.1
zipp                    3.6.0

四、使用方法（★极其重要）
1、数据集： CUB-200-2011，Stanford Cars 和FGVC Aircraft
2、训练：python train.py
五、其他
比较特殊的注意事项。
