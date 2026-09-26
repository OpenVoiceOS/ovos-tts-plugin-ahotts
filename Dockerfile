# AhoTTS Basque/Spanish voices served through ovos-tts-server's ElevenLabs-compatible
# API. A self-contained, offline image: any client that speaks the ovos-tts-server /
# ElevenLabs API can hit it, and it can be A/B-tested against other ovos-tts-server
# voices (phoonnx, omnivoice, ...) by pointing at a different port.
#
# pyahotts bundles the prebuilt HTS synthesis engine (x86_64 + aarch64 .so) and all
# voice/dictionary data and emits WAV directly, so no system AhoTTS build, no model
# download, and no ffmpeg transcode are needed.
FROM python:3.11-slim

WORKDIR /app
COPY . /app

# the plugin + pyahotts (self-contained engine + data) + the OVOS TTS server.
# setuptools<81 keeps ovos-plugin-manager's pkg_resources usage working.
# ovos-tts-server>=1.13.5a1's alpha floor lets pip resolve the prerelease without --pre.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir "setuptools<81" "." "ovos-tts-server>=1.13.5a1"

# Default language, overridable with the AHOTTS_LANG build arg ("eu" or "es").
ARG AHOTTS_LANG=eu
RUN useradd -m -u 1000 ovos \
    && mkdir -p /home/ovos/.config/mycroft \
    && printf '{\n  "tts": {\n    "module": "ovos-tts-plugin-ahotts",\n    "ovos-tts-plugin-ahotts": {\n      "lang": "%s"\n    }\n  }\n}\n' "${AHOTTS_LANG}" \
        > /home/ovos/.config/mycroft/mycroft.conf \
    && chown -R 1000:1000 /home/ovos/.config
USER 1000

EXPOSE 9666
ENTRYPOINT ["ovos-tts-server", "--engine", "ovos-tts-plugin-ahotts", \
            "--host", "0.0.0.0", "--port", "9666", "--cache"]
