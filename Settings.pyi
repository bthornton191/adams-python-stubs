import Manager
import Object
from DatabaseIds import PreferenceIds as PreferenceIds
from collections.abc import Generator
from typing import Any, ItemsView, Iterable, KeysView, List, Literal, ValuesView

BUFFER_SIZE: Any
__asita__: str


class ModelSettings(Object.ObjectSubBase):
    advanced: AdvancedSettingManager
    def __init__(self, mod) -> None: ...
    integrator: IntegratorSettings
    linear_solver: LinearSolverSettings
    kinematics: KinematicsSettings
    equilibrium: EquilibriumSettings
    initial_conditions: InitialConditionsSettings
    contact: ContactSettings
    flex_body: FlexBodySettings
    debug: DebugSettings
    solver: SolverSettings
    output: OutputSettings


class AdvancedSettingManager(Manager.AdamsManager):
    def iterDBKeys(self) -> Generator[Any, None, None]: ...
    def values(self) -> ValuesView[AdvancedSetting]: ...
    def keys(self) -> KeysView[str]: ...
    def items(self) -> ItemsView[str, AdvancedSetting]: ...
    def __getitem__(self, name: str) -> AdvancedSetting: ...
    def __iter__(self) -> Iterable[AdvancedSetting]: ...
    def values_full(self) -> ValuesView[AdvancedSetting]: ...
    def keys_full(self) -> KeysView[str]: ...
    def items_full(self) -> ItemsView[str, AdvancedSetting]: ...


class SinglerunPreferences(Object.ObjectSubBase):
    icon_visibility: bool
    """Turn icon visibility on or off during animation."""
    time_delay: float
    """Specifies the number of seconds to temporarily halt command processing."""
    update_graphics: Literal["contact_output_step", "contact_step", "end", "iteration", "none", "output_step", "time_step"]
    """Specifies when to update graphics."""
    monitor: Literal["contact_output_step", "contact_step", "end", "iteration", "none", "output_step", "time_step"]
    """Turns on output for monitoring the simulation."""
    alert: bool
    """Turns on alerting the user before reading the binary file if there is data that has been modified since the last save operation."""
    save_analyses: bool
    """Specifies if analyses are to be saved."""
    analysis_prefix: str
    """Specified name of the analysis object."""


class GeneralPreferences(Object.ObjectSubBase):
    file_prefix: str
    """Prefix for saved analysis files if save_files is turned on."""
    save_files: bool
    """Turns on/off saving of analysis files."""
    load_analysis: bool
    """Load analysis after a run."""
    model_update: Literal["auto", "off", "on"]
    """Specifies when the model is updated during simulation."""
    solver_preference: Literal["external", "internal", "write_files_only"]
    """Set solver preference."""
    verify_first: bool
    """Verify model before running the simulation."""
    hold_solver_license: bool
    """Set whether or not the Adams Solver license is checked back in once the simulation is complete."""
    user_solver_executable: str
    """Set it to use the standard Adams Solver executable (leave it blank) or a user-defined or customized Adams Solver library."""
    show_all_messages: bool
    """For externally run Adams Solver, turns on display of Adams Solver messages in the information window."""
    choice_for_solver: Literal["cplusplus", "fortran"]
    """Set solver choice (write-only). One of 'cplusplus' or 'fortran'."""
    remote_compute: bool
    """(Linux only) Enter the name of the remote host where you run Adams Solver or leave blank to use local machine."""
    node_name: str
    """(Linux only) Node ID of the remote computer."""
    mdi_directory_remote: str
    """(Linux only) Name of the Adams Solver installation directory on the remote machine."""
    remote_directory: str
    """(Linux only) Directory that Adams Solver uses to write out its files and search for input files."""


class SinglerunDebuggerPreferences(Object.ObjectSubBase):
    iterations_per_step_measure: bool
    """Displays the number of iterations that Adams Solver needed to successfully progress to the next integration time step, over the course of a simulation."""
    integrator_order_measure: bool
    """Displays the order of the polynomial that Adams Solver uses during the predictor phase of integration."""
    static_imbalance_measure: bool
    """Displays the current imbalance in the equilibrium equations that Adams Solver computes during a static equilibrium simulation."""
    step_size_measure: bool
    """Displays the integrator step size (units of model time), as the simulation progresses, on a logarithmic scale."""
    enable_debugger: bool
    """Enables or disables the debugger."""
    track_maximum: Literal["acceleration", "change", "error", "force"]
    """Enables tracking of modeling element."""
    show_table: bool
    """Enables/disables showing of the debug table."""
    highlight_objects: bool
    """Turns highlighting on/off for objects experiencing the most error or the most change in states based on the element being tracked."""


class MultirunPreferences(Object.ObjectSubBase):
    save_analyses: bool
    """Turn on to automatically copy parametric analysis results to a permanent location when the analysis is complete."""
    load_analyses: bool
    """Turn on to load analyses."""
    analysis_prefix: str
    """Base name for analysis objects."""
    save_curves: bool
    """Clears all displayed measures at the beginning of the parametric analysis and automatically saves the curve from each trial or iteration."""
    chart_design_objectives: bool
    """Enables charting of design objectives."""
    chart_design_objective_variables: bool
    """Displays strip charts for each design variable, plotting its value versus the trial or iteration number."""
    stop_on_error: bool
    """Turn on/off stopping a parametric analysis on the first simulation error encountered."""
    show_summary: bool
    """Turn on/off summary display."""
    write_single_parasolid_file: bool
    """Write a single parasolid file."""


class OptimizationPreferences(Object.ObjectSubBase):
    algorithm: Literal["dot1", "dot2", "dot3", "optdes_grg", "optdes_sqp", "user1", "user2", "user3"]
    """Specifies optimization algorithm to use."""
    maximum_iterations: int
    """Maximum number of design iterations allowed."""
    convergence_tolerance: float
    """An optimization run is considered to be successful if the differences in the objective in two successive iterations falls below this value."""
    differencing_technique: Literal["centered_difference", "forward_difference"]
    """Differencing technique for the optimizer to compute gradients for the design functions."""
    scaled_perturbation: float
    """Size of perturbations."""
    user_parameters: List[float]
    """Adams View passes the user parameters to a user-written optimization algorithm."""
    rescale_iterations: int
    """Number of iterations after which the design variable values are rescaled. A value of -1 turns off scaling."""
    slp_convergence_iter: int
    """Number of consecutive iterations for which the absolute or relative convergence criteria must be met to indicate convergence in the DOT Sequential Linear Programming method."""
    debug: bool
    """Turns on debugging output."""


class SolverSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    threads: int
    """Number of threads to use."""
    library_path: str
    """Path to user libraries."""
    status_message: bool
    """Set to True to turn on solver messages."""


class LinearSolverSettings(Object.ObjectSubBase):
    solver: Literal["auto", "calahan", "harwell", "umfpack"]
    """Linear system solver to be used."""
    stability: float
    """Factor used in the modified Markowitz criterion during pivot selection of a LU matrix factorization."""


class IntegratorSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    type: Literal["gstiff", "hastiff", "hht", "newmark", "wstiff"]
    """Type of integrator for simulation."""
    pattern: List[bool]
    """Jacobian pattern of dynamics (max allowed: 10)."""
    formulation: Literal["i3", "si1", "si2"]
    """Equation formulation."""
    corrector: Literal["modified", "orig_constant", "original"]
    """Type of corrector."""
    error: float
    """Error tolerance."""
    hinit: float
    """Initial time step."""
    hmax: float
    """Maximum time step."""
    hmin: float
    """Minimum time step."""
    interpolate: bool
    """Interpolate output step."""
    maxit: int
    """Maximum number of corrector iterations allowed."""
    kmax: int
    """Maximum integrator order."""
    alpha: float
    """Alpha coefficient for HHT integrator."""
    beta: float
    """Beta coefficient for Newmark integrator."""
    gamma: float
    """Gamma coefficient for Newmark integrator."""
    fixit: int
    """Fixed number of corrector iterations per time step."""
    hratio: int
    """Hratio for fix step integrator."""
    maxerror: float
    """Max error for fixed step integrator."""


class KinematicsSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    apattern: List[bool]
    """Pattern for kinematics acceleration solution (max allowed: 10)."""
    pattern: List[bool]
    """Pattern for kinematic displacement solution (max allowed: 10)."""
    aerror: float
    """Maximum acceleration error Adams Solver is to allow for each time step."""
    error: float
    """Maximum displacement error Adams Solver is to allow for each time step."""
    alimit: float
    """Maximum angular increment Adams Solver is to allow per iteration."""
    tlimit: float
    """Maximum translational increment Adams Solver is to allow per iteration."""
    hmax: float
    """Maximum time step that the kinematics solver is allowed to take."""
    amaxit: int
    """Maximum number of iterations Adams Solver is to allow for finding accelerations at a point in time."""
    maxit: int
    """Maximum number of iterations Adams Solver is to allow for finding the displacements at a point in time."""


class InitialConditionsSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    aerror: float
    """Maximum acceleration error Adams Solver is to allow during an initial conditions solution."""
    error: float
    """Maximum displacement error Adams Solver is to allow for the assembly process."""
    alimit: float
    """Maximum angular increment Adams Solver is to allow while testing trial solutions for a set of consistent initial conditions."""
    tlimit: float
    """Maximum translational increment Adams Solver is to allow while testing trial solutions during a solution step."""
    verror: float
    """Maximum velocity error that Adams Solver is to allow during an initial conditions solution."""
    amaxit: int
    """Maximum number of iterations Adams Solver is to allow for finding accelerations."""
    maxit: int
    """Maximum number of iterations Adams Solver is to allow for finding displacements during initial conditions."""
    apattern: List[bool]
    """Pattern for evaluating the Jacobian matrix during the modified Newton-Raphson solution for the accelerations (max allowed: 10)."""
    pattern: List[bool]
    """Pattern for evaluating the Jacobian matrix during the modified Newton-Raphson solution for the displacements (max allowed: 10)."""


class EquilibriumSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    alimit: float
    """Maximum angular increment allowed per iteration during a static or quasi-static equilibrium analysis."""
    error: float
    """Relative correction convergence threshold."""
    imbalance: float
    """Equation imbalance convergence threshold."""
    tlimit: float
    """Maximum translational increment allowed per iteration."""
    stability: float
    """Fraction of the mass and damping matrices Adams Solver adds to the stiffness matrix during static simulations."""
    maxit: int
    """Maximum number of iterations allowed for finding static equilibrium."""
    solver_method: Literal["advanced", "aggressive", "all", "original"]
    """Static solver method to be used for equilibrium solution."""
    atol: float
    """Absolute tolerance value."""
    rtol: float
    """Relative tolerance value."""
    maxitl: int
    """Maximum number of allowed inner loops in all the solvers."""
    etamax: float
    """Maximum threshold for the error tolerance of the linear Krylov solver for Newton+Krylov and Tensor-Krylov methods."""
    eta: float
    """Initial residual tolerance for the linear Krylov Solver for Tensor_Krylov method."""
    pattern: List[bool]
    """Equilibrium pattern (max allowed: 10)."""


class ContactSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    faceting_tolerance: float
    """Faceting tolerance."""
    geometry_library: Literal["default_library", "parasolids"]
    """Library to be used for contact computation."""


class FlexBodySettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    limit_check: Literal["none", "selnod", "skin"]
    """Linear limit checking on all the flexible bodies in the model."""
    limit_action: Literal["halt", "message_only", "return"]
    """Action to be taken by Adams Solver if a flexible body exceeds its linear limit."""
    formulation: Literal["max_optimized", "optimized", "original"]
    """Formulation to be used for flexible bodies."""


class DebugSettings(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    debug: bool
    """Turns on debugging output."""
    dump: bool
    """Write current representation of a model to the message file."""
    eprint: bool
    """Write solution diagnostic information to the message file."""
    verbose: bool
    """When turned on writes extensive model diagnostic information to the screen."""
    reqdump: bool
    """Enables dumping of requests at each iteration."""
    jmdump: bool
    """Enables export of the model jacobian to a *.jac file at each iteration."""
    rhsdump: bool
    """Enables export the model equation residuals to a *.rhs file at each iteration."""
    dof: bool
    """Fortran solver only: prints degrees-of-freedom in the tabular output file."""
    topology: bool
    """Enables printing topological data in the message file."""


class AdvancedSetting(Object.ObjectSubBase):
    setting: str
    """Solver advanced setting name."""
    value: str
    """Solver advanced setting value."""
    deactivate: bool
    """Solver advanced setting deactivate status (whether setting is set or unset)."""
    def destroy(self): ...


class OutputSettings(Object.ObjectSubBase):
    Femdatas: Any
    def __init__(self, _DBKey) -> None: ...
    stress: Literal["", "dac", "generic", "rpc"]
    """Specifies the stress type."""
    strain: Literal["", "dac", "generic", "rpc"]
    """Specifies the strain type."""


class SessionPreferences(Object.ObjectSubBase):
    def __init__(self, _DBKey) -> None: ...
    general: GeneralPreferences
    single_run: SinglerunPreferences
    single_run_debugger: SinglerunDebuggerPreferences
    multi_run: MultirunPreferences
    optimization: OptimizationPreferences
