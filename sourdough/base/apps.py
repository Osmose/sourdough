from django.apps import AppConfig

import session_csrf


class BaseConfig(AppConfig):
    name = 'sourdough.base'
    _patches_applied = False

    def ready(self):
        """Apply monkeypatches once when Django loads."""
        if not self._patches_applied:
            self.apply_monkeypatches()
            self._patches_applied = True

    def apply_monkeypatches(self):
        session_csrf.monkeypatch()
