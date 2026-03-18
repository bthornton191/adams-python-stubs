import Manager
import Object
from typing import Any, List


class MaterialManager(Manager.AdamsManager):
    ...


class Material(Object.Object):
    youngs_modulus: float
    poissons_ratio: float
    density: float
    orthotropic_constants: List[float]
    anisotropic_constants: List[float]
