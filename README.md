# EDCS – Emergent Drone Coordination System

**Fully Decentralized, Self-Healing Drone Swarm Architecture**  
**Vitavolt Global Enerji | Technology Portfolio**

EDCS is a completely decentralized drone swarm coordination framework that enables autonomous formation, resilient operation, and automatic recovery without any central command node.

It is designed for real-world environments where GPS can be denied, communication can be jammed, and individual drones can be lost.

---

## Core Value Proposition

Most existing drone swarm systems rely on centralized command-and-control. This creates critical weaknesses:

- Single point of failure
- High communication overhead
- Limited scalability
- Vulnerability to GPS jamming and spoofing

**EDCS solves these problems** through three core innovations:

1. **Reference Signal Propagation** – Distributed formation initialization via nearest-neighbor signal chaining
2. **Adaptive Artificial Potential Fields** – Smooth, collision-free motion control
3. **Distributed Self-Healing** – Automatic detection and recovery from drone loss

The system operates with **minimum communication** (primarily passive Bluetooth RSSI) and remains functional in GPS-denied environments.

---

## Key Technical Features

| Feature | Description |
|--------|-------------|
| Fully Decentralized | No central command, no permanent leader drone |
| Self-Healing | Automatic reformation after drone loss while preserving formation shape |
| Low Communication Load | Primarily uses passive Bluetooth RSSI |
| GPS Resilient | Can operate with intermittent or denied GPS |
| Scalable | Local decision-making allows natural scaling |
| Adaptive Motion | Potential field based smooth trajectories |

---

## Core Algorithms

### 1. Reference Signal Propagation
The first drone that obtains reliable positioning becomes a temporary Reference Drone and broadcasts a Reference Signal (position + formation pattern + scale). The signal propagates only to the nearest neighbor (highest RSSI), creating a low-overhead distributed chain that initializes the formation.

### 2. Adaptive Artificial Potential Fields

Total force on each drone:

```
F = F_rep + F_coh + F_goal
```

- **F_rep** (Repulsive): Prevents collisions
- **F_coh** (Cohesive): Maintains swarm integrity
- **F_goal** (Attractive): Guides the mission objective

This produces smooth trajectories and automatic collision avoidance.

### 3. Distributed Self-Healing
Every drone continuously monitors its neighbors via RSSI. When a missing neighbor is detected, a local query is initiated. If no response is received, the swarm automatically reforms while preserving the overall formation shape.

---

## Target Applications

- **Agricultural Spraying** – Large-area coverage with formation resilience
- **Disaster Response & Search-and-Rescue** – Operation in infrastructure-collapsed and low-signal environments
- **Area Scanning & Security** – Persistent surveillance with long endurance
- **UAV / SİHA Tactical Operations** – Resilience against jamming and single-point failures
- **High-Speed Automated Highway Systems** – Continuous corridor monitoring and incident support

---

## Simulation Status

Current implementation includes:
- Python-based 2D swarm simulation
- Reference signal chain initialization
- Adaptive potential field motion
- Self-healing under random drone loss
- Visual validation of formation stability

Simulation code is located in `src/`.

---

## Anne AI & Ethical Framework

EDCS is being developed within Vitavolt’s broader technology vision that also includes **Anne AI** — an ethical, empathetic multi-agent AI initiative focused on human-centered and responsible autonomy.

The long-term goal is to explore the integration of ethical decision layers and multi-agent coordination principles between Anne AI and physical swarm systems such as EDCS.

---

## Current Development Status

- Conceptual architecture: Completed
- Mathematical model: Defined
- Simulation prototype: Implemented
- Technical documentation: Available
- Hardware prototype: Planned
- UWB integration: Planned
- Field trials: Planned

---

## Repository Structure

```
EDCS-Drone-Swarm/
├── src/
│   └── edcs_swarm_sim.py          # Core simulation
├── EDCS_Makale.pdf                # Technical paper
├── EDCS_Technical_Presentation.pptx
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Collaboration & Funding

EDCS is positioned as a strategic technology within **Vitavolt Global Enerji**.

We are open to:

- Technical collaboration
- Research partnerships
- Pilot projects
- Investment and funding discussions

If you are interested in contributing, testing, or supporting the development of EDCS, please get in touch.

---

## Contact

**Mustafa Gökhan Yılmaz**  
Co-founder & Technology Lead  
Vitavolt Global Enerji İnşaat Taahüt Ltd. Şti.  
İzmir, Türkiye  

GitHub: [github.com/mgy421977-bit/EDCS-Drone-Swarm](https://github.com/mgy421977-bit/EDCS-Drone-Swarm)

---

*EDCS – Emergent intelligence for resilient autonomous systems.*
