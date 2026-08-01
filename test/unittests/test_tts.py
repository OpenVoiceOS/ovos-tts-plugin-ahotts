"""Unit tests for the AhoTTS (Basque/Spanish) OVOS TTS plugin.

These exercise the real pyahotts engine bundled with the plugin: they
synthesise audio to disk and assert a non-empty WAV file is produced, plus
cover language handling and the advertised supported languages.
"""
import os
import tempfile
import unittest

from ovos_tts_plugin_ahotts import AhoTTSPlugin


class TestAhoTTSPlugin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tts = AhoTTSPlugin({"lang": "eu"})

    def _synth(self, sentence, lang=None):
        fd, path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        os.remove(path)
        try:
            out, phonemes = self.tts.get_tts(sentence, path, lang=lang)
            self.assertEqual(out, path)
            self.assertIsNone(phonemes)  # ahotts does not return phonemes
            self.assertTrue(os.path.isfile(out), "no wav file was written")
            self.assertGreater(os.path.getsize(out), 0, "wav file is empty")
        finally:
            if os.path.isfile(path):
                os.remove(path)

    def test_basque_synthesis(self):
        self._synth("kaixo mundua", lang="eu")

    def test_spanish_synthesis(self):
        self._synth("hola mundo", lang="es")

    def test_default_lang_synthesis(self):
        # no explicit lang -> falls back to the plugin's configured lang (eu)
        self._synth("kaixo")

    def test_unsupported_lang_falls_back_to_basque(self):
        # unsupported langs must not crash; the plugin logs a warning and
        # synthesises with the default 'eu' voice instead.
        self._synth("hello world", lang="en")

    def test_available_languages(self):
        self.assertEqual(AhoTTSPlugin.available_languages, {"es", "eu"})

    def test_rejects_unsupported_config_lang(self):
        with self.assertRaises(ValueError):
            AhoTTSPlugin({"lang": "en"})


if __name__ == "__main__":
    unittest.main()
