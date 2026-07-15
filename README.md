# OVOS TTS Plugin AhoTTS

## Description

OVOS TTS plugin for [AhoTTS](https://github.com/aholab/AhoTTS)

## Install

`pip install ovos-tts-plugin-ahotts`


## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-ahotts",
    "ovos-tts-plugin-ahotts": {
        "lang": "eu"
    }
  }
```

## Docker

A container that serves this plugin behind [ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server)'s
ElevenLabs-compatible HTTP API on port `9666` is published to
`ghcr.io/openvoiceos/ovos-tts-plugin-ahotts`.

The image is fully self-contained and offline: `pyahotts` bundles the synthesis
engine and all Basque/Spanish voice data, so there is no model download or API key.

```bash
docker run --rm -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-ahotts:dev
```

Or with compose:

```bash
docker compose up
```

The served language defaults to Basque (`eu`) and is an `AHOTTS_LANG` build arg
(`eu` or `es`), so switch it by rebuilding:

```bash
docker build --build-arg AHOTTS_LANG=es -t ahotts-es .
```

## Credits

This plugin was developed by [TigreGotico](https://tigregotico.pt) for OpenVoiceOS under the [ILENIA](https://proyectoilenia.es) project.

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project [ILENIA](https://proyectoilenia.es) with reference 2022/TL22/00215337
