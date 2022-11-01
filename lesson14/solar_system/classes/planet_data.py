"""DTO pattern"""
from typing import NamedTuple


class PlanetData(NamedTuple):
    """Planet DTO"""
    planet_size: tuple[float, float]
    planet_color: str | tuple[float, float, float]
    radius: int
    increase_angle: float
    name: str = 'star'
