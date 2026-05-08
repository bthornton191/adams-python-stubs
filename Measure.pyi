import Manager
from Marker import Marker
import Object
from typing import List, ItemsView, Iterable, ValuesView


class Measure(Object.ObjectComment):
    adams_id_id: int


class ObjectMeasure(Measure):
    """Measure of a pre-defined characteristic of a model object.

    Created via ``model.Measures.createObject(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    characteristic: str
    """Object characteristic to be measured."""
    component: str
    """Component of the characteristic in which you are interested. Available components depend on the coordinate system."""
    coordinate_rframe: Marker
    """Existing marker defining the reference frame for coordinate measurements."""
    coordinate_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for coordinate measurements."""
    motion_rframe: Marker
    """Existing marker defining the reference frame for motion measurements."""
    motion_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for motion measurements."""
    object: Object.ObjectComment
    """Object to measure."""
    object_name: str
    """Full dot-path name of the object to measure."""
    from_first: bool
    """Select point at which forces are measured or from which distances are measured."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


pt2pt_characteristics: List[str]


class Pt2ptMeasure(Measure):
    """Measure of a kinematic characteristic between two points (markers).

    Created via ``model.Measures.createPt2pt(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    characteristic: str
    """Kinematic characteristic to be measured."""
    component: str
    """Component of the characteristic in which you are interested. Available components depend on the coordinate system."""
    coordinate_rframe: Marker
    """Existing marker defining the reference frame for coordinate measurements."""
    coordinate_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for coordinate measurements."""
    motion_rframe: Marker
    """Existing marker defining the reference frame for motion measurements."""
    motion_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for motion measurements."""
    from_point: Marker
    """Marker from which to measure."""
    from_point_name: str
    """Full dot-path name of the marker from which to measure."""
    to_point: Marker
    """Marker to which to measure."""
    to_point_name: str
    """Full dot-path name of the marker to which to measure."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class AngleMeasure(Measure):
    """Measure of the angle defined by three markers.

    Created via ``model.Measures.createAngle(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    first_point: Marker
    """First marker on an entity."""
    first_point_name: str
    """Full dot-path name of the first marker on an entity."""
    middle_point: Marker
    """Middle (vertex) marker on an entity."""
    middle_point_name: str
    """Full dot-path name of the middle (vertex) marker on an entity."""
    last_point: Marker
    """Last marker on an entity."""
    last_point_name: str
    """Full dot-path name of the last marker on an entity."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class ComputedMeasure(Measure):
    """Measure evaluated using an Adams View expression (design-time).

    Created via ``model.Measures.createComputed(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    text_of_expression: str
    """Computation to be performed by the function. Must be a character string, not an expression object."""
    units: str
    """Type of units to be used for this measure."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class OrientMeasure(Measure):
    """Measure of the orientation of one frame relative to another.

    Created via ``model.Measures.createOrient(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    characteristic: str
    """Characteristic convention with which to associate the component."""
    component: str
    """Rotational component to measure."""
    to_frame: Object.ObjectComment
    """Coordinate system (Model, Part, or Marker) to which to measure."""
    to_frame_name: str
    """Full dot-path name of the coordinate system to which to measure."""
    from_frame: Object.ObjectComment
    """Coordinate system (Model, Part, or Marker) from which to measure."""
    from_frame_name: str
    """Full dot-path name of the coordinate system from which to measure."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class PointMeasure(Measure):
    """Measure of a kinematic characteristic at a single point (marker).

    Created via ``model.Measures.createPoint(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    characteristic: str
    """Kinematic characteristic to be measured."""
    component: str
    """Component of the characteristic in which you are interested. Available components depend on the coordinate system."""
    coordinate_rframe: Marker
    """Existing marker defining the reference frame for coordinate measurements."""
    coordinate_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for coordinate measurements."""
    motion_rframe: Marker
    """Existing marker defining the reference frame for motion measurements."""
    motion_rframe_name: str
    """Full dot-path name of the marker defining the reference frame for motion measurements."""
    point: Marker
    """Marker or point to measure."""
    point_name: str
    """Full dot-path name of the marker or point to measure."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class RangeMeasure(Measure):
    """Statistical range measure (max, min, average, variation) of an existing measure.

    Created via ``model.Measures.createRange(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    range_measure_type: str
    """Type of the range measure."""
    of_measure_name: str
    """Full dot-path name of the existing predefined measure to analyze."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class FunctionMeasure(Measure):
    """Measure evaluated by the Adams Solver at each timestep during simulation.

    Created via ``model.Measures.createFunction(...)``.
    """
    comment_id: int
    legend: str
    """Text that will appear at the top of the created measure. The legend text may only be set during measure creation."""
    function: str
    """Function expression to be evaluated by Adams Solver during the simulation."""
    user_function: List[float]
    """Up to 30 real constants passed to the user-written subroutine."""
    routine: str
    """Library and subroutine name for the user-written function measure."""
    units: str
    """Units to be associated with the function measure result."""
    create_measure_display: bool
    """If True, a strip chart of the measure is displayed in the GUI. Read-only after creation."""


class MeasureManager(Manager.SubclassManager):
    def createObject(self,
                     name: str = None,
                     object: Object.ObjectComment = None,
                     object_name: str = None,
                     characteristic: str = None,
                     component: str = None,
                     from_first: bool = False,
                     legend: str = None,
                     coordinate_rframe: Marker = None,
                     coordinate_rframe_name: str = None,
                     motion_rframe: Marker = None,
                     motion_rframe_name: str = None,
                     create_measure_display: bool = True,
                     **kwargs) -> ObjectMeasure:
        """Create a measure of a pre-defined characteristic of a model object.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_OBJECT_n`` if not provided.
        object : Object.ObjectComment, optional
            Object on which the measure is to be created. Required if ``object_name`` is not given.
        object_name : str, optional
            Full dot-path name of the object to measure. Required if ``object`` is not given.
        characteristic : str
            Characteristic of the object to be measured. Options include:
            ``angular_acceleration``, ``angular_deformation``, ``angular_deformation_velocity``,
            ``angular_kinetic_energy``, ``angular_momentum_about_cm``, ``angular_velocity``,
            ``ax_ay_az_projection_angles``, ``cm_acceleration``, ``cm_angular_acceleration``,
            ``cm_angular_displacement``, ``euler_angles``, ``cm_angular_velocity``,
            ``cm_position``, ``cm_position_relative_to_body``, ``cm_velocity``,
            ``contact_point_location``, ``element_force``, ``element_torque``,
            ``integrator_order``, ``integrator_stepsize``, ``integrator_time_step``,
            ``iterator_steps``, ``iteration_count``, ``kinetic_energy``,
            ``potential_energy_delta``, ``power_consumption``, ``pressure_angle``,
            ``static_imbalance``, ``strain_kinetic_energy``, ``translational_acceleration``,
            ``translational_deformation``, ``translational_deformation_velocity``,
            ``translational_displacement``, ``translational_kinetic_energy``,
            ``translational_momentum``, ``translational_velocity``.
        component : str
            Component of the characteristic to be measured. Options include:
            ``x_component``, ``y_component``, ``z_component``, ``mag_component``,
            ``r_component``, ``rho_component``, ``theta_component``, ``phi_component``.
        from_first : bool, optional
            If ``True``, measure from the i-marker; otherwise from the j-marker, by default ``False``.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        coordinate_rframe : Marker, optional
            Marker defining the reference frame for coordinate measurements.
        coordinate_rframe_name : str, optional
            Full dot-path name of the marker defining the reference frame for coordinate measurements.
        motion_rframe : Marker, optional
            Marker defining the reference frame for motion measurements.
        motion_rframe_name : str, optional
            Full dot-path name of the marker defining the reference frame for motion measurements.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        ObjectMeasure
            The newly created object measure.
        """
        ...

    def createPt2pt(self,
                    name: str = None,
                    characteristic: str = None,
                    component: str = None,
                    from_point: Marker = None,
                    from_point_name: str = None,
                    to_point: Marker = None,
                    to_point_name: str = None,
                    coordinate_rframe: Marker = None,
                    coordinate_rframe_name: str = None,
                    motion_rframe: Marker = None,
                    motion_rframe_name: str = None,
                    legend: str = None,
                    create_measure_display: bool = True,
                    **kwargs) -> Pt2ptMeasure:
        """Create a point-to-point kinematic measure between two markers.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_PT2PT_n`` if not provided.
        characteristic : str
            Kinematic characteristic to be measured. Options:
            ``translational_displacement``, ``translational_velocity``,
            ``translational_acceleration``, ``angular_velocity``, ``angular_acceleration``.
        component : str
            Component of the characteristic. Options include:
            ``x_component``, ``y_component``, ``z_component``, ``mag_component``,
            ``r_component``, ``rho_component``, ``theta_component``, ``phi_component``.
        from_point : Marker, optional
            Marker from which to measure. Required if ``from_point_name`` is not given.
        from_point_name : str, optional
            Full dot-path name of the marker from which to measure.
        to_point : Marker, optional
            Marker to which to measure. Required if ``to_point_name`` is not given.
        to_point_name : str, optional
            Full dot-path name of the marker to which to measure.
        coordinate_rframe : Marker, optional
            Marker defining the reference frame for coordinate measurements.
        coordinate_rframe_name : str, optional
            Full dot-path name of the coordinate reference frame marker.
        motion_rframe : Marker, optional
            Marker defining the reference frame for motion measurements.
        motion_rframe_name : str, optional
            Full dot-path name of the motion reference frame marker.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        Pt2ptMeasure
            The newly created point-to-point measure.
        """
        ...

    def createAngle(self,
                    name: str = None,
                    first_point: Marker = None,
                    first_point_name: str = None,
                    middle_point: Marker = None,
                    middle_point_name: str = None,
                    last_point: Marker = None,
                    last_point_name: str = None,
                    legend: str = None,
                    create_measure_display: bool = True,
                    **kwargs) -> AngleMeasure:
        """Create an angle measure defined by three markers.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_ANGLE_n`` if not provided.
        first_point : Marker, optional
            First marker on the entity. Required if ``first_point_name`` is not given.
        first_point_name : str, optional
            Full dot-path name of the first marker.
        middle_point : Marker, optional
            Middle (vertex) marker on the entity. Required if ``middle_point_name`` is not given.
        middle_point_name : str, optional
            Full dot-path name of the middle (vertex) marker.
        last_point : Marker, optional
            Last marker on the entity. Required if ``last_point_name`` is not given.
        last_point_name : str, optional
            Full dot-path name of the last marker.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        AngleMeasure
            The newly created angle measure.
        """
        ...

    def createComputed(self,
                       name: str = None,
                       text_of_expression: str = None,
                       units: str = None,
                       legend: str = None,
                       create_measure_display: bool = True,
                       **kwargs) -> ComputedMeasure:
        """Create a computed measure evaluated using an Adams View expression (design-time).

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_COMPUTED_n`` if not provided.
        text_of_expression : str
            Computation to be performed. Must be a character string (not an expression object).
            Can reference any Adams View variable or measure.
        units : str, optional
            Units to associate with the measure result (e.g. ``"length"``, ``"force"``).
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        ComputedMeasure
            The newly created computed measure.
        """
        ...

    def createOrient(self,
                     name: str = None,
                     characteristic: str = None,
                     component: str = None,
                     to_frame: Object.ObjectComment = None,
                     to_frame_name: str = None,
                     from_frame: Object.ObjectComment = None,
                     from_frame_name: str = None,
                     legend: str = None,
                     create_measure_display: bool = True,
                     **kwargs) -> OrientMeasure:
        """Create an orientation measure of one coordinate frame relative to another.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_ORIENT_n`` if not provided.
        characteristic : str
            Characteristic convention to use (e.g. Euler angles, body-fixed rotation sequence).
        component : str
            Rotational component to measure.
        to_frame : Object.ObjectComment, optional
            Coordinate system (Model, Part, or Marker) to which to measure.
            Required if ``to_frame_name`` is not given.
        to_frame_name : str, optional
            Full dot-path name of the coordinate system to which to measure.
        from_frame : Object.ObjectComment, optional
            Coordinate system (Model, Part, or Marker) from which to measure.
        from_frame_name : str, optional
            Full dot-path name of the coordinate system from which to measure.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        OrientMeasure
            The newly created orientation measure.
        """
        ...

    def createPoint(self,
                    name: str = None,
                    point: Marker = None,
                    point_name: str = None,
                    characteristic: str = None,
                    component: str = None,
                    coordinate_rframe: Marker = None,
                    coordinate_rframe_name: str = None,
                    motion_rframe: Marker = None,
                    motion_rframe_name: str = None,
                    legend: str = None,
                    create_measure_display: bool = True,
                    **kwargs) -> PointMeasure:
        """Create a kinematic measure at a single point (marker).

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_POINT_n`` if not provided.
        point : Marker, optional
            Marker or point to measure. Required if ``point_name`` is not given.
        point_name : str, optional
            Full dot-path name of the marker or point to measure.
        characteristic : str
            Kinematic characteristic to be measured. Options include:
            ``translational_displacement``, ``translational_velocity``,
            ``translational_acceleration``, ``angular_velocity``, ``angular_acceleration``,
            and others from the full characteristic list.
        component : str
            Component of the characteristic. Options include:
            ``x_component``, ``y_component``, ``z_component``, ``mag_component``,
            ``r_component``, ``rho_component``, ``theta_component``, ``phi_component``.
        coordinate_rframe : Marker, optional
            Marker defining the reference frame for coordinate measurements.
        coordinate_rframe_name : str, optional
            Full dot-path name of the coordinate reference frame marker.
        motion_rframe : Marker, optional
            Marker defining the reference frame for motion measurements.
        motion_rframe_name : str, optional
            Full dot-path name of the motion reference frame marker.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        PointMeasure
            The newly created point measure.
        """
        ...

    def createRange(self,
                    name: str = None,
                    range_measure_type: str = None,
                    of_measure_name: str = None,
                    legend: str = None,
                    create_measure_display: bool = True,
                    **kwargs) -> RangeMeasure:
        """Create a statistical range measure on an existing measure.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_RANGE_n`` if not provided.
        range_measure_type : str
            Type of range calculation to perform (e.g. ``maximum``, ``minimum``,
            ``average``, ``variation``).
        of_measure_name : str
            Full dot-path name of the existing measure to analyze.
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        RangeMeasure
            The newly created range measure.
        """
        ...

    def createFunction(self,
                       name: str = None,
                       function: str = None,
                       user_function: List[float] = None,
                       routine: str = None,
                       units: str = None,
                       legend: str = None,
                       create_measure_display: bool = True,
                       **kwargs) -> FunctionMeasure:
        """Create a function measure evaluated by Adams Solver during simulation.

        Parameters
        ----------
        name : str, optional
            Name of the measure. Auto-generated as ``MEA_FUNCTION_n`` if not provided.
        function : str, optional
            Adams Solver run-time function expression to evaluate each timestep
            (e.g. ``"MOTION(.MODEL_1.MOT_1, 0, 0, MODEL)"``).
        user_function : list of float, optional
            Up to 30 real constants passed to the user-written subroutine specified by ``routine``.
        routine : str, optional
            Library and subroutine name of the user-written function measure
            (e.g. ``"myfunlib::MYFUNC"``).
        units : str, optional
            Units to associate with the measure result (e.g. ``"length"``, ``"force"``).
        legend : str, optional
            Text to display at the top of the measure plot. Can only be set at creation time.
        create_measure_display : bool, optional
            If ``True``, creates a strip-chart display window in the GUI, by default ``True``.

        Returns
        -------
        FunctionMeasure
            The newly created function measure.
        """
        ...

    def __getitem__(self, name) -> Measure: ...
    def __iter__(self, *args) -> Iterable[str]: ...
    def items(self) -> ItemsView[str, Measure]: ...
    def values(self) -> ValuesView[Measure]: ...
