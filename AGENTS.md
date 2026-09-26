# ovos-tts-plugin-ahotts

OVOS TTS plugin wrapping the AhoTTS engine (via `pyahotts`) for Basque (`eu`) and Spanish (`es`) speech synthesis.

## Setup

```bash
pip install ovos-tts-plugin-ahotts
# or from source
pip install .
```

Runtime deps: `ovos-plugin-manager>=1.0.0,<3.0.0`, `pyahotts`.

## Test

No test suite exists. The module ships a manual smoke entry:

```bash
python -m ovos_tts_plugin_ahotts   # synthesizes "kaixo mundua" to /tmp/test.wav
```

## Lint/Typecheck

None configured.

## Layout

- `ovos_tts_plugin_ahotts/__init__.py` — `AhoTTSPlugin(TTS)`, the whole implementation. Constructs `pyahotts.AhoTTS`, validates `lang` is `es`/`eu`, implements `get_tts(sentence, wav_file, lang)` returning `(wav_file, None)` (no phonemes), and advertises `available_languages = {"es", "eu"}`.
- `ovos_tts_plugin_ahotts/version.py` — version block consumed by `setup.py`.
- `setup.py` — packaging; entry point.

Entry-point group: `mycroft.plugin.tts` → `ovos-tts-plugin-ahotts = ovos_tts_plugin_ahotts:AhoTTSPlugin`. This is the OPM TTS plugin group.

Config block (`mycroft.conf`):

```json
"tts": {"module": "ovos-tts-plugin-ahotts",
        "ovos-tts-plugin-ahotts": {"lang": "eu"}}
```

## Conventions

- Branches: work on `dev`, stable on `master`. NEVER use `main`.
- Never edit `version.py`; gh-automations bumps semver from conventional-commit prefixes (`feat:`/`fix:`/`feat!:`).
- New repos private by default.
- Commit identity: JarbasAi <jarbasai@mailfence.com>.
- Reference `OpenVoiceOS/gh-automations` reusable workflows at `@dev`.
- No Neon/`neon-*` references.
- No meta-commentary (no history, no dates) in docs/commits/code.
- CI is provided by OpenVoiceOS/gh-automations.

## Gotchas

- `build_tests.yml` is bespoke (not a gh-automations reusable workflow), has broken YAML indentation under the "Build Source Packages" step, and tries to `pip install .[audio-backend,mark1,stt,...]` extras this repo does not define — it cannot pass as written.
- `release_workflow.yml` / `publish_stable.yml` reference `TigreGotico/gh-automations/...@master`, not `OpenVoiceOS/gh-automations@dev`.
- `setup.py` classifiers list Python 2.7 / 3.0–3.6, but CI targets 3.11/3.14 — stale metadata.
- The synthesis quality and language coverage depend entirely on the external `pyahotts`/AhoTTS engine; unsupported langs fall back to `eu` with a warning.
- Committed build artifact: `ovos_tts_plugin_ahotts.egg-info/` is tracked.
