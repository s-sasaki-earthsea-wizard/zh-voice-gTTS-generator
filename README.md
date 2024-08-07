# zh-voice-gTTS-generator (Under Construction)
テキストから中国語の音声ファイルの生成と再生をし、MP3ファイルとして保存するPythonプロジェクトです。
Google Text-to-Speech (gTTS)を使用してテキストを音声に変換し、生成されたファイルを再生します。

## 概要
このプロジェクトは、入力された中国語のテキストをMP3形式の音声ファイルに変換し、再生と保存を行います。
gTTSを使用してテキストをMP3形式の音声に変換して保存し、pydubを使用して再生します。

## 開発環境
開発環境は以下の通りです：

- OS: macOS Ventura 13.6.8
  - 現在、ローカルマシンでの動作を確認中ですが、DockerのUbuntuコンテナでの動作も予定しています。
- Python: 3.8.6
- 依存関係: Poetry, gTTS, pydub

## インストール方法
プロジェクトの依存関係をインストールするには、以下のコマンドを実行してください：

```bash
poetry install
```
Poetryをインストールしていない場合は、以下の公式ドキュメントに記載のofficial installerを使った方法を試してください。
- https://python-poetry.org/docs/#installing-with-the-official-installer

## 使い方
現在は生成する中国語の文章の入力ができません。
以下のコマンドでサンプル音声の生成が行われます。

```bash
python src/zh_voice_generator/generate_zh_voice.py
```

## その他
現在特になし

_____

# zh-voice-gTTS-generator (Under Construction)
A Python project for generating and playing Chinese voice files from text, and saving them as MP3 files.
This project uses Google Text-to-Speech (gTTS) to convert text into speech and plays the generated files.

## Overview
This project converts input Chinese text into an MP3 format voice file, which is then played and saved.
It uses gTTS to convert text into MP3 format and pydub for audio playback.

## Development Environment
The development environment is as follows:

- OS: macOS Ventura 13.6.8
  - The development is currently done on a local machine, but the project is planned to run in a Docker Ubuntu container as well.
- Python: 3.8.6
- Dependencies: Poetry, gTTS, pydub

## Installation
To install the project dependencies, run the following command:

```bash
poetry install
```

If you do not have Poetry installed, please follow the instructions on the official Poetry documentation using the official installer:

- https://python-poetry.org/docs/#installing-with-the-official-installer

## Usage
Currently, you cannot input Chinese text for generation.
Running the following command will generate a sample voice file:

```bash
python src/zh_voice_generator/generate_zh_voice.py
```

## Others
None at the moment.