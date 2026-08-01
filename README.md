# OVOS TTS Plugin AhoTTS

An OVOS text-to-speech plugin for [AhoTTS](https://github.com/aholab/AhoTTS). It generates
speech in Basque (`eu`) and Spanish (`es`).

## Install

```bash
pip install ovos-tts-plugin-ahotts
```

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

A container that serves this plugin behind [OpenVoiceOS/ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server)'s
ElevenLabs-compatible HTTP API on port `9666` is published to
`ghcr.io/openvoiceos/ovos-tts-plugin-ahotts`.

The image is fully self-contained and offline. `pyahotts` bundles the synthesis engine
and all Basque and Spanish voice data, so the container needs no model download and no
API key.

Run the container:

```bash
docker run --rm -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-ahotts:dev
```

Or with compose:

```bash
docker compose up
```

The served language defaults to Basque (`eu`) and is set by the `AHOTTS_LANG` build arg
(`eu` or `es`). To switch it, rebuild the image:

```bash
docker build --build-arg AHOTTS_LANG=es -t ahotts-es .
```

## Related projects

- [OpenVoiceOS/ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server): the HTTP server this plugin's Docker image runs behind.
- [OpenVoiceOS/ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): loads and manages this plugin at runtime.
- [aholab/AhoTTS](https://github.com/aholab/AhoTTS): the upstream synthesis engine this plugin wraps.

## Credits

This plugin was developed by [TigreGotico](https://tigregotico.pt) for OpenVoiceOS under the [ILENIA](https://proyectoilenia.es) project.

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project [ILENIA](https://proyectoilenia.es) with reference 2022/TL22/00215337

## License

Apache-2.0
