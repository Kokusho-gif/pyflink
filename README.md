# Pyflink example

This repository includes my example of pyflink.

このリポジトリは私が作成したpyflinkコードが入っています。

## Tabale of contents

1. Instruction
2. Requirements
3. Usage

　　
1. 導入
2. 依存関係
3. 使い方


## Instruction
### Motivation
Since pyflink is new and on the way of development, it's hard to find code example which is fit to your demand. So I decided to put my procedure of understanding about pyflink here as python scripts.

pyflinkは新しくまだ開発途中なので、日本語でのリファレンスはほとんど存在しなく、英語や中国語でさえも情報が少ないです。そこで私が実装したpyflinkコードを結集することにしました。

### Architecture of this repository
This repository includes project, requirements.txt.

* project
  Including various sample. Each content have own python script and additional files the example needs. e.g. Kafka
* requirements.txt
  Including python pip dependency. 
  WARN: I use one python environment to execute whole of examples. It means if you want to 
  execute one sample, some pip dependencies don't have to be installed.
  
このリポジトリはprojectフォルダ、requirements.txtを含みます。

* project
  作成したすべてのサンプルが入っています。各サンプルはフォルダで分けられ各サンプルに必要な外部ファイルなども同梱しています。
* requirement.txt
  インストールするべきpipライブラリのリストです。
  注意:すべてのサンプルを実行するのに必要なライブラリが入っています。なのでもし一部のサンプルを使用する場合不必要なライブラリも含まれています。


## Requiement
### OS
ubuntu18.0.4LTS(Linux)

### python
3.6.9

### Java
open-jdk 11.0.15

HINT:
Pyflink needs python 3.6~3.9 and Java11

## Usage
1. After your environment satisfy all requirement shown above, let's install python libraries by pip.
```
pip pip install -r requirements.txt
```
Main library you have to install is apache-flink.

2. Then you can execute any of my example code.
```
python project/hogehoge.py
```

