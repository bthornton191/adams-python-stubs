# adamspy-stubs

Python type stubs (`.pyi` files) for the **MSC Adams Python API** (`import Adams`), the object-oriented Python interface embedded in Adams View 2023.1.

These stubs provide IDE autocompletion, type checking, and inline documentation for Adams Python scripts. They are maintained alongside the [adams-vscode](https://github.com/bthornton191/adams_vscode) extension and consumed as a reference by the [adams-python-model-builder](https://github.com/bthornton191/adams_skills) skill.

## Structure

```
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
# The `Adams` module (top-level) is the session entry point. Everything hangs off it:
import Adams

# Create a model
mod = Adams.Models.create(name='MY_MODEL')

# Set units
Adams.defaults.units.setUnits(length='mm', mass='kg', time='second', force='newton')

# Access the active/default model
mod = Adams.defaults.model

# Create a part in the model
part = mod.Parts.createRigidBody(name='PART_1')

# Create a marker on the part
mkr = part.Markers.create(name='MARKER_1')

dv = mod.DesignVariables.createReal(name='DV_1', value=10.0)

# String-to-object lookup
marker = Adams.stoo('.MY_MODEL.PART_1.MARKER_1')

# Evaluate an Adams expression
val = Adams.evaluate_exp('.MY_MODEL.DV_1')

# Execute CMD language command from Python
Adams.execute_cmd('simulation single_run transient end_time=5.0 number_of_steps=500 model_name=.MY_MODEL')
```


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
