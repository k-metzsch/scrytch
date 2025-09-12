import asyncio
from typing import Dict, Optional

import pygame


class Sound:
    _mixer_initialized = False
    _loaded_sound_cache: Dict[str, pygame.mixer.Sound] = {}
    _name_to_sound: Dict[str, pygame.mixer.Sound] = {}
    _active_channels: set[pygame.mixer.Channel] = set()

    def __init__(self, sprite):
        self.sprite = sprite
        self.__ensure_mixer()

    def play_sound(
        self,
        sound_name: Optional[str] = None,
        volume: Optional[float] = None,
    ) -> Optional[pygame.mixer.Channel]:
        sound = self.__get_sound(sound_name)
        if not sound:
            return None
        if volume is not None:
            sound.set_volume(max(0.0, min(1.0, volume)))
            channel = sound.play()
        else:
            channel = sound.play()
        if channel:
            self._active_channels.add(channel)
        return channel

    async def play_sound_until_done(
        self, sound_name: Optional[str] = None, volume: Optional[float] = None
    ):
        channel = self.play_sound(sound_name=sound_name, volume=volume)
        if not channel:
            return
        while channel.get_busy():
            await asyncio.sleep(0.01)

    def stop_all_sounds(self):
        if not self._mixer_initialized:
            return
        pygame.mixer.stop()
        self._active_channels.clear()

    @classmethod
    def __ensure_mixer(cls):
        if not cls._mixer_initialized:
            pygame.mixer.init()
            cls._mixer_initialized = True

    def __ensure_sounds_dict(self) -> Dict[str, str]:
        main = getattr(self.sprite, "main", None)
        if not main:
            return {}
        if not hasattr(main, "_sounds"):
            if hasattr(main, "sounds") and callable(getattr(main, "sounds")):
                result = main.sounds()
                if isinstance(result, dict):
                    main._sounds = result
                else:
                    if not hasattr(main, "_sounds"):
                        main._sounds = {}
            else:
                main._sounds = {}
        return main._sounds

    def __get_sound(self, sound_name: Optional[str]) -> Optional[pygame.mixer.Sound]:
        sounds_dict = self.__ensure_sounds_dict()
        if not sounds_dict:
            return None
        if sound_name is None:
            for k in sounds_dict.keys():
                sound_name = k
                break
            if sound_name is None:
                return None
        if sound_name in self._name_to_sound:
            return self._name_to_sound[sound_name]
        path = sounds_dict.get(sound_name)
        if not isinstance(path, str):
            return None
        if path not in self._loaded_sound_cache:
            try:
                self._loaded_sound_cache[path] = pygame.mixer.Sound(path)
            except Exception:
                return None
        sound_obj = self._loaded_sound_cache[path]
        self._name_to_sound[sound_name] = sound_obj
        return sound_obj
