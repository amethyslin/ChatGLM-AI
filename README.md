
# ChatGLM - AI

-----


## 介绍

ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型，基于 [General Language Model (GLM)]() 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。 ChatGLM-6B 使用了和 ChatGPT 相似的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。

chatGLM可以做什么?

- 自我认知
- 提纲写作
- 文案写作
- 右键写作助手
- 信息抽取
- 编写代码
- 中英文写作
- 角色扮演
- 评论比较
- 旅游向导



## 使用方式
#### 硬件要求（仔细看一下自己电脑的GPU专用显存大小）：



|量化等级|最低 GPU 显存（推理）|最低 GPU 显存（高效参数微调）|
| --- | --- | --- |
|FP16（无量化）	|13 GB|	14 GB|
|INT8	|8 GB|	9 GB|
|INT4	|6 GB|	7 GB|


#### 修改配置文件
```json
 // config.json文件 
{
    //6G显存,将false改成4,8-12G显存可以改成4或者8,大于13G无需更改
    "quantize":4,
    //输入指令例 [title]
    "prompt":"[title]",
    // 最大令牌数量600 <max_length< 4096
    "max_length":3500,
    //top
    "top_p":0.7,
    //温度,值越高，生成越随机
    "temperature":1
}

```




#### 环境安装
1、从官网下载CUDA和CUDN环境，要求CUDA版本11.7,CUDN版本11.x

2、将模型文件chatglm-6b下载解压到根目录，[下载地址]()

```python
#升级pip
python -m pip install --upgrade pip

#安装torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

# 安装环境
pip install -r requirements.txt

```

#### 启动
```python
#启动界面ui
python web.py

#启动api
python api.py

#启动本地生成
python generate.py
```





## 引用
```
@inproceedings{
  zeng2023glm-130b,
  title={{GLM}-130B: An Open Bilingual Pre-trained Model},
  author={Aohan Zeng and Xiao Liu and Zhengxiao Du and Zihan Wang and Hanyu Lai and Ming Ding and Zhuoyi Yang and Yifan Xu and Wendi Zheng and Xiao Xia and Weng Lam Tam and Zixuan Ma and Yufei Xue and Jidong Zhai and Wenguang Chen and Zhiyuan Liu and Peng Zhang and Yuxiao Dong and Jie Tang},
  booktitle={The Eleventh International Conference on Learning Representations (ICLR)},
  year={2023},
  url={https://openreview.net/forum?id=-Aw0rrrPUF}
}
```

```
@inproceedings{du2022glm,
  title={GLM: General Language Model Pretraining with Autoregressive Blank Infilling},
  author={Du, Zhengxiao and Qian, Yujie and Liu, Xiao and Ding, Ming and Qiu, Jiezhong and Yang, Zhilin and Tang, Jie},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={320--335},
  year={2022}
}
```
