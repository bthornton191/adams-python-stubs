from collections.abc import Generator
from typing import Any, ItemsView, Iterable, KeysView, ValuesView
from Object import Object


class DuplicateNameError(AttributeError):
    ...


class ObjectCreationFailure(Exception):
    ...


class InvalidNameError(AttributeError):
    ...


class AdamsManager():
    parent: Any
    managedClass: Any
    def __init__(self, managed_class, parent) -> None: ...
    def set(self, name, **properties): ...
    def iterDBKeys(self) -> Generator[Any, None, None]: ...

    def values_full(self, *args) -> ValuesView[Object]:
        """Return all managed objects keyed by their full dot-path name.

        Unlike :meth:`values`, this method uses the full dot-path name
        (e.g. ``'.MODEL_1.UDE_INSTANCE_1.PART_1'``) as the dictionary key,
        so objects from different UDE instances that share the same short name
        are all returned — none are silently dropped.

        Prefer this over :meth:`values` whenever the model contains
        User-Defined Element (UDE) instances whose child objects share
        identical short names.  See ADMS-137078.

        Example::

            # Instead of (may silently drop duplicates under UDEs):
            for part in model.Parts.values():
                ...

            # Use (returns every part regardless of name collisions):
            for part in model.Parts.values_full():
                ...
        """
        ...

    def keys_full(self, *args) -> KeysView[str]:
        """Return the full dot-path names of all managed objects.

        Unlike :meth:`keys`, this method uses the full dot-path name
        (e.g. ``'.MODEL_1.UDE_INSTANCE_1.PART_1'``) as the key, so objects
        from different UDE instances that share the same short name are all
        represented — none are silently dropped.

        Prefer this over :meth:`keys` whenever the model contains
        User-Defined Element (UDE) instances whose child objects share
        identical short names.  See ADMS-137078.
        """
        ...

    def items_full(self, *args) -> ItemsView[str, Object]:
        """Return ``(full_name, object)`` pairs for all managed objects.

        Unlike :meth:`items`, this method uses the full dot-path name
        (e.g. ``'.MODEL_1.UDE_INSTANCE_1.PART_1'``) as the key, so objects
        from different UDE instances that share the same short name are all
        returned — none are silently dropped.

        Prefer this over :meth:`items` whenever the model contains
        User-Defined Element (UDE) instances whose child objects share
        identical short names.  See ADMS-137078.
        """
        ...

    def iterkeys(self, *args) -> None: ...
    def iteritems(self, *args) -> None: ...
    def itervalues(self, *args) -> None: ...
    def __len__(self, *args): ...
    def __dir__(self, all: bool = ...): ...

    def create(self, name: str = None, **kwargs) -> Object:
        """Create a new object.

        Parameters
        ----------
        name : str, optional
            Name of the object.
        """
        ...

    def items(self) -> ItemsView[str, Object]:
        """Return ``(short_name, object)`` pairs for all managed objects.

        .. warning::
            The dictionary is keyed by **short name**.  If the model contains
            User-Defined Element (UDE) instances whose child objects share the
            same short name, only one object per name is returned — later
            entries silently overwrite earlier ones (ADMS-137078).
            Use :meth:`items_full` to retrieve all objects by full dot-path name.
        """
        ...

    def values(self) -> ValuesView[Object]:
        """Return all managed objects.

        .. warning::
            Internally keyed by **short name**.  If the model contains
            User-Defined Element (UDE) instances whose child objects share the
            same short name, only one object per name is returned — duplicates
            are silently dropped (ADMS-137078).
            Use :meth:`values_full` to retrieve all objects regardless of name
            collisions.
        """
        ...

    def keys(self) -> KeysView[str]:
        """Return the short names of all managed objects.

        .. warning::
            Returns **short names** only.  If the model contains
            User-Defined Element (UDE) instances whose child objects share the
            same short name, only one name per collision is returned
            (ADMS-137078).
            Use :meth:`keys_full` to retrieve every object's full dot-path name.
        """
        ...

    def __getitem__(self, name) -> Object: ...
    def __iter__(self, *args) -> Iterable[str]: ...
    def __contains__(self, name) -> bool: ...


class SubclassManager(AdamsManager):
    def __init__(self, managedClass, parent) -> None: ...
    def set(self, name, cls, **kwargs): ...
