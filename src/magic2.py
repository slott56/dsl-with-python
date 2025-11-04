"""Proxy magic 2 module for demo"""

class Spell:
    def __init__(self, **kwargs) -> None:
        pass

class Aspect:
    def __init__(self, *args, **kwargs) -> None:
        pass

class Effect(Aspect):
    pass

class TimeEffect(Effect):
    pass

class DurationAspect(Aspect):
    pass

class RangeAspect(Aspect):
    pass

class CastingTimeAspect(Aspect):
    pass

class GesturesAspect(Aspect):
    pass

class IncantationsAspect(Aspect):
    pass

class SpeedAspect(Aspect):
    @classmethod
    def based_on(cls, *args, **kwargs) -> Aspect:
        return SpeedAspect(*args, **kwargs)
