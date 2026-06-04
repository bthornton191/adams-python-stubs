# Adams Python API Reference

This is the API reference for the **Adams Python API** — the `import Adams` interface
embedded in Adams View 2023.1.

## Quick start

```python
import Adams

# Create a model
model = Adams.Models.create(name='MODEL_1')
model.units.length = 'mm'
model.units.mass = 'kg'
model.units.time = 'sec'

# Create a rigid body
part = model.Parts.createRigidBody(name='PART_1')
part.mass = 1.0
part.Markers.create(name='MKR_1', location=[0, 0, 0])

# Run a command
Adams.execute_cmd("simulation single_step dur=1.0 steps=100")
```

## How to navigate

Use the left sidebar to browse by category, or the search bar to find a specific
class, method, or property.

## Session entry point

The `Adams` module is the top-level session object. All models are accessed through
`Adams.Models`, defaults through `Adams.defaults`, etc.
See [Adams](adams.md) and [Model](model.md) for details.

## Manager pattern

Every collection of child objects is exposed as a typed **manager**:

```python
model.Parts           # PartManager
model.Parts['PART_1'] # RigidBody
part.Markers          # MarkerManager
part.Markers.create(name='MKR_1', location=[0, 0, 0])  # Marker
```

See [Manager](manager.md) for the base class interface.
