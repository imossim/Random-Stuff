# Aerodynamics

## Fundamental Forces

There are four fundamental aerodynamic forces for Aircraft

- Weight $(W)$
- Thrust $(T)$
- Lift $(L)$
- Drag $(D)$

For the case of heavier than air flight,
$$
\frac{L}{D} = \frac{W}{T}
$$

### Weight

Weight of the aircraft, contributed by aircraft frame and subsystems.

### Thrust

Force provided by propulsion system in the forward direction of the aircraft. Direction of force produced by propulsion system may vary, but thrust is the force in the forward direction.

### Lift

There are multiple theories to explain the generation of lift

- Velocity changes caused by circulation on the upper and lower surfaces of the airfoil lead to pressure changes. This results in air above the wing traveling at a higher velocity than the air below the wing, resulting in a pressure difference, with a greater pressure below the wing.
  $$
  \Delta V \rightarrow \Delta P \rightarrow \text{Lift}
  $$
  

  - NOTE: Difference in velocity is *NOT* due to equal transit time, in which the air above the wing has to cover a larger distance to meet up with the air below the wing. If this were true, airfoils would not be able to function upside down.

- Angle of attack of airfoil/wing results in downwash, and provides a force upwards due to conservation of momentum. This can also be a result of negative camber
  $$
  \Delta M_{\text{in vertical plane}} \rightarrow \text{Lift}
  $$
  

  - Camber is the asymmetry between the top and bottom acting surfaces of the airfoil, which represents the "curve" of the airfoil.

    - Positive camber is if the airfoil is generally convex upwards

    - Negative camber is in the situation in which the airfoil is concave downward

    - No camber generally means that the airfoil is symmetrical

    - Camber can be characterized by the camber line, the curve $Z(x)$ that is a function of the midpoint between the upper and lower surfaces of the airfoil and the thickness function of the airfoil $T(x)$ by the following equations. 
      $$
      Z_{upper}(x) = Z(x) + T(x)\\
      Z_{lower}(x) = Z(x) - T(x)
      $$

### Drag

Force produced by aircraft body which opposes thrust produced by the engine. Aircraft bodies are made to be streamlined to reduced the effects of the various forms of drag as listed below.

- Friction Drag (Skin Friction)
- Pressure Drag
- Induced Drag
- Wave Drag

##### Friction Drag

Friction drag or skin friction is the drag produced due to interactions between the boundary layer of the skin of the aircraft and the freestream flow. This form of drag can be reduced by polishing the surface, or producing conditions such that the flow across the surface would remain attached.

##### Pressure Drag

Pressure drag increases with Angle of Attack ($\alpha$) of the aircraft, due to increased separation of flow occurring. This can be reduced by streamlining the aicraft.

##### Induced Drag

As the generation of lift would not only result in a force along the perpendicular axis, induced drag is a result of the generation of lift, which results in the direction of the net force vector pointing towards the rear of the aircraft.

##### Wave Drag

A result of high speed flight

### Performance

Power required to sustain flight can be estimated from knowing the aerodynamic forces on the aircraft. This can then be used to estimate the range, endurance, takeoff/landing distance, and the glide slope of the aircraft.

### Stability

Stability is the aircraft's tendency to return towards a specific state during flight.

- Positive stability
  - When an aircraft in stable flight has a natural tendency to correct itself towards the aforementioned stable position when a small deflection is introduced
  - Commonly seen in most aircraft. It also negates the need for a flight computer to constantly correct the aircraft.
- Negative stability
  - When an aircraft in stable flight has a tendency to continue to rotate in the direction of rotation when a small deflection is introduced
  - Commonly seen in fighter jets, to improve roll and pitch performance