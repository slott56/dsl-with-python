"""Example spell book."""
push = Spell(
    name="Push",
    skill="Apportation",
    notes="Even the most subtle of things,,,",
    effect=TimeEffect("sends a small object into the future", "10 min"),
    duration=DurationAspect(measure="10 minutes"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="1 round"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "gestures": GesturesAspect("Wave one hand ...", "simple"),
        "incantations": IncantationsAspect(
            "Where did it go?", "sentence"
        ),
    },
)
spells = [push]
