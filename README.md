# OVOS TTS Plugin AhoTTS

## Description

OVOS TTS plugin for [AhoTTS](https://github.com/aholab/AhoTTS)

## Install

`pip install ovos-tts-plugin-ahotts`

You also need to compile AhoTTS and then set the binary path in your mycroft.conf

```bash
echo "Installing AhoTTS"
git clone https://github.com/aholab/AhoTTS /tmp/AhoTTS
cd /tmp/AhoTTS
./script_compile_all_linux.sh
mv /tmp/AhoTTS/bin /usr/bin/AhoTTS/
```

## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-ahotts",
    "ovos-tts-plugin-ahotts": {
        "bin": "/usr/bin/AhoTTS/tts",
        "lang": "eu",
        "speed": 100
    }
  }
```

## Credits

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337
