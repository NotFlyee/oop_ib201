# ленивая реализация

from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

class LightingSystem(System):
    def __init__(self):
        self._is_on = 0
        self._brightness = 50

    def turn_on(self) -> str:
        self._is_on = 1
        return 'Освещение: включено'

    def turn_off(self) -> str:
        self._is_on = 0
        return "Освещение: выключено"

    def set_brightness(self, value: float) -> str:
        self._brightness = value
        return f"Яркость освещения установлена на {value}%"

    def get_status(self) -> str:
        if self._is_on:
            return f'Освещение: включено | {self._brightness}%'
        return 'Освещение: выключено'

class ClimateControlSystem(System):
    def __init__(self):
        self._is_on = 0
        self._temperature = None
        self._is_special_climate_mode_on = 0

    def turn_on(self) -> str:
        self._is_on = 1
        return "Климат-контроль: включен"
    
    def turn_off(self) -> str:
        self._is_on = 0
        return "Климат-контроль: выключен"

    def set_temperature(self, value: float) -> str:
        self._temperature = value
        return f"Температура установлена на {self._temperature}°C"
    
    def turn_on_special_climate_mode(self) -> str:
        self._is_special_climate_mode_on = 1
        if self._is_special_climate_mode_on:
            return 'Особый климат-режим активирован'
        return "Обычный климат-режим активирован"
    
    def turn_off_special_climate_mode(self) -> str:
        self._is_special_climate_mode_on = 0
        if self._is_special_climate_mode_on:
            return 'Особый климат-режим выключен'
        return "Обычный климат-режим выключен"

    def get_status(self) -> str:
        result = ""
        if self._is_on:
            result += f"Климат-контроль: включен, температура {self._temperature}°C"
        else:
            result += f"Климат-контроль: выключен"
        if self._is_special_climate_mode_on:
            result += "\nОсобый климат-режим активирован"
        return result
 
class SecuritySystem(System):
    def __init__(self):
        self._is_on = 0

    def turn_on(self) -> str:
        self._is_on = 1
        return "Сигнализация включена"
    
    def turn_off(self) -> str:
        self._is_on = 0
        return "Сигнализация выключена"

    def get_status(self) -> str:
        if self._is_on:
            return "Сигнализация включена"
        return "Сигнализация выключена"

class MultimediaSystem(System):
    def __init__(self):
        self._is_on = 0
        self._is_music_playing = 0

    def turn_on(self) -> str:
        self._is_on = 1
        return "Мультимедийная система: включена"
    
    def turn_off(self) -> str:
        self._is_on = 0
        return "Мультимедийная система: выключена"
    
    def play_music(self) -> str:
        if self._is_music_playing:
            return ""
        self._is_music_playing = 1
        return "Музыка включена"
    
    def stop_music(self) -> str:
        if not self._is_music_playing:
            return ""
        self._is_music_playing = 0
        return "Музыка выключена"
    
    def get_status(self) -> str:
        if self._is_on:
            return "Мультимедийная система: включена"
        return "Мультимедийная система: выключена"

class SmartHomeFacade:
    def __init__(self):
        self._lighting_system = LightingSystem()
        self._climate_control_system = ClimateControlSystem()
        self._security_system = SecuritySystem()
        self._multimedia_system = MultimediaSystem()
        
    def get_all_systems_status(self):
        return "\n".join([
            self._lighting_system.get_status(),
            self._climate_control_system.get_status(),
            self._security_system.get_status(),
            self._multimedia_system.get_status()
        ])

    def home_mode(self):
        result = []
        result.append(self._lighting_system.turn_on())
        result.append(self._lighting_system.set_brightness(100))
        result.append(self._climate_control_system.turn_on())
        result.append(self._climate_control_system.set_temperature(22))
        result.append(self._security_system.turn_off())
        result.append(self._climate_control_system.turn_off_special_climate_mode())
        return result

    def party_mode(self):
        result = []
        result.append(self._lighting_system.turn_on())
        result.append(self._lighting_system.set_brightness(40))
        result.append(self._multimedia_system.turn_on())
        result.append(self._multimedia_system.play_music())
        result.append(self._climate_control_system.turn_on_special_climate_mode())
        return result

    def night_mode(self):
        result = []
        result.append(self._lighting_system.turn_off())
        result.append(self._climate_control_system.turn_on())
        result.append(self._climate_control_system.set_temperature(18))
        result.append(self._security_system.turn_on())
        result.append(self._multimedia_system.turn_off())
        result.append(self._climate_control_system.turn_off_special_climate_mode())
        return result

    def away_mode(self):
        result = []
        result.append(self._lighting_system.turn_off())
        result.append(self._climate_control_system.turn_off())
        result.append(self._multimedia_system.turn_off())
        result.append(self._security_system.turn_on())
        result.append(self._climate_control_system.turn_off_special_climate_mode())
        return result
