import Manager
import Object
from DBAccess import CustomProperty as CustomProperty
from EntityTypes import ent_femdata as ent_femdata
from typing import Any, ItemsView, Iterable, KeysView, ValuesView


class FemdataManager(Manager.AdamsManager):
    def values(self) -> ValuesView[Femdata]: ...
    def keys(self) -> KeysView[str]: ...
    def items(self) -> ItemsView[str, Femdata]: ...
    def __getitem__(self, name: str) -> Femdata: ...
    def __iter__(self) -> Iterable[Femdata]: ...
    def values_full(self) -> ValuesView[Femdata]: ...
    def keys_full(self) -> KeysView[str]: ...
    def items_full(self) -> ItemsView[str, Femdata]: ...


class Femdata(Object.ObjectComment, Object.ObjectAdamsId):
    def __init__(self, _DBKey) -> None: ...
    fe_part: Any
    fe_part_name: Any
    output_type: Any
    markers: Any
    marker_names: Any
    hotspots: Any
    radius: Any
    criterion: Any
    file_name: Any
    start: Any
    end: Any
    skip: Any
