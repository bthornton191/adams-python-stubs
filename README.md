# adamspy-stubs

Python type stubs (`.pyi` files) for the **MSC Adams Python API** (`import Adams`), the object-oriented Python interface embedded in Adams View 2023.1.

These stubs provide IDE autocompletion, type checking, and inline documentation for Adams Python scripts. They are maintained alongside the [adams-vscode](https://github.com/bthornton191/adams_vscode) extension and consumed as a reference by the [adams-python-model-builder](https://github.com/bthornton191/adams_skills) skill.

## Structure

```
adamspy/          # Package stubs — matches the Adams Python module layout
  Adams.pyi         # Top-level session: Models, defaults, execute_cmd(), stoo(), file I/O
  Model.pyi         # Model class + ModelManager
  Part.pyi          # RigidBody, PointMass, FlexBody, FEPart, ExternalSystem + PartManager
  Marker.pyi        # Marker, FloatingMarker + MarkerManager
  Constraint.pyi    # All joint types, motions, primitives, couplers, gears + ConstraintManager
  Force.pyi         # All force types (spring, bushing, beam, SFORCE, GFORCE, etc.) + ForceManager
  Geometry.pyi      # All geometry types + GeometryManager
  DataElement.pyi   # Spline, Array, Matrix, StateVariable, PInput/POutput/PState + DataElementManager
  Simulation.pyi    # Simulation, SimulationManager
  Analysis.pyi      # Analysis, ResultComponent, AnalysisManager
  Measure.pyi       # ObjectMeasure, Pt2ptMeasure, FunctionMeasure, etc. + MeasureManager
  Defaults.pyi      # AdamsDefaults, DefaultUnits (unit string enums)
  DesignVariable.pyi# IntegerDV, RealDV, StringDV, ObjectDV + DesignVariableManager
  Contact.pyi       # Contact (solid-to-solid, curve-to-curve, etc.) + ContactManager
  SystemElement.pyi # DifferentialEquation, TransferFunction, LinearStateEquation + manager
  Expression.pyi    # expression(), eval(), AdamsExpr
  Object.pyi        # Base classes: ObjectBase, ObjectComment, ObjectAdamsId
  Manager.pyi       # AdamsManager, SubclassManager base classes
  Material.pyi      # Material + MaterialManager
  Sensor.pyi        # Sensor + SensorManager
  RuntimeFunction.pyi
  Section.pyi
  ...               # Other supporting modules
```

## Adams Python API — Quick Overview

The Adams Python API is embedded in Adams View. Scripts always begin with:

```python
import Adams
```

The `Adams` module (top-level) is the session entry point. Everything hangs off it:

```python
# Create a model
m = Adams.Models.create(name='MY_MODEL')

# Set units
Adams.defaults.units.length = 'mm'
Adams.defaults.units.mass = 'kg'
Adams.defaults.units.time = 'second'
Adams.defaults.units.force = 'newton'

# Access the active/default model
m = Adams.defaults.model

# String-to-object lookup
marker = Adams.stoo('.MY_MODEL.PART_1.MARKER_1')

# Evaluate an Adams expression
val = Adams.evaluate_exp('.MY_MODEL.DV_1')

# Execute CMD language command from Python
Adams.execute_cmd('simulation single_run transient end_time=5.0 number_of_steps=500 model_name=.MY_MODEL')
```

## Key API Patterns

### Manager-based creation

All entities are created through manager objects on the parent:

```python
part   = m.Parts.createRigidBody(name='LINK_1', location=[0, 0, 0])
marker = part.Markers.create(name='PIN', location=[100, 0, 0])
joint  = m.Constraints.createRevolute(name='J1', i_marker=marker, j_marker=m.ground_part.Markers['GROUND_MKR'])
spring = m.Forces.createTranslationalSpringDamper(name='SPR_1', i_marker_name='.MY_MODEL.LINK_1.PIN', j_marker_name='.MY_MODEL.ground.REF', stiffness=5000.0, damping=50.0)
sim    = m.Simulations.create(name='SIM_1', end_time=2.0, number_of_steps=200)
sim.simulate()
```

### Object references vs string names

Most `create` methods accept **either** an object reference or a name string for related objects:

```python
# Equivalent:
joint = m.Constraints.createRevolute(i_marker=marker_obj, j_marker=ground_marker_obj)
joint = m.Constraints.createRevolute(i_marker_name='.MY_MODEL.LINK_1.PIN', j_marker_name='.MY_MODEL.ground.REF')
```

### Parameterization with expressions

```python
from Adams import expression

dv = m.DesignVariables.createReal(name='LENGTH', value=250.0)
marker.location = expression(f'{dv.full_name}')  # deferred — re-evaluates when DV changes
```

### Array property gotcha

Array properties (location, orientation, stiffness, etc.) must be reassigned in full — in-place mutation doesn't propagate:

```python
loc = marker.location      # get a copy
loc[0] += 50.0             # mutate the copy
marker.location = loc      # reassign — THIS is what Adams sees
# marker.location[0] += 50 # ← does NOT work
```

## Version

These stubs target **MSC Adams 2023.1**. Some API surface may differ in earlier or later releases.

## Usage

### In a VS Code project with the Adams extension

The [adams-vscode](https://github.com/bthornton191/adams_vscode) extension already bundles these stubs. No extra setup needed.

### Standalone (Pylance / Pyright)

Add the repo root to `python.analysis.extraPaths` in your VS Code settings:

```json
{
  "python.analysis.extraPaths": ["C:/path/to/adams-python-stubs"]
}
```

Or point Pyright at it in `pyrightconfig.json`:

```json
{
  "extraPaths": ["C:/path/to/adams-python-stubs"]
}
```
