# EDCS – Emergent Drone Coordination System

**Fully Decentralized, Self-Healing Drone Swarm Architecture**  
**Vitavolt Global Enerji | Technology Portfolio**

EDCS is a research architecture for completely decentralized drone swarm coordination. The design aims to support autonomous formation, resilient operation, and automatic recovery without a permanent central command node.

It is intended for environments where GPS may be intermittent or denied, communication may be degraded, and individual drones may be lost. These conditions are treated as **design objectives** evaluated in simulation; they are not presented as field-proven operational results.

---

## Research Identity & Network

**EDCS — Emergent Drone Coordination System**

EDCS is a **research / simulation prototype** for decentralized, self-healing drone swarm coordination. It is **not** an operational or certified military/defense system. Current results come from architecture definition and a Python 2D simulation; they should not be read as field-proven operational performance, electronic-warfare immunity, or certified reliability.

| Resource | URL |
|----------|-----|
| EDCS canonical project page | https://vitavoltglobal.com/edcs.html |
| EDCS research page | https://vitavoltglobal.com/research/edcs.html |
| Vitavolt Research | https://vitavoltglobal.com/research/ |
| Research publication map | https://vitavoltglobal.com/research/publications.html |
| This repository | https://github.com/mgy421977-bit/EDCS-Drone-Swarm |

Vitavolt Global → Vitavolt Research → EDCS → this repository.

---

## Core Value Proposition

Most existing drone swarm systems rely on centralized command-and-control. This creates critical weaknesses:

- Single point of failure
- High communication overhead
- Limited scalability
- Vulnerability to GPS jamming and spoofing

**EDCS is designed to address these weaknesses** through three core architectural ideas (evaluated in the current 2D simulation):

1. **Reference Signal Propagation** – Distributed formation initialization via nearest-neighbor signal chaining
2. **Adaptive Artificial Potential Fields** – Smooth, collision-avoiding motion control in the model
3. **Distributed Self-Healing** – Detection and recovery from simulated drone loss while preserving formation shape

The architecture targets **minimum communication** (primarily passive Bluetooth RSSI in the design) and explores operation under intermittent or denied GPS as a research direction—not as a certified field capability.

---

## Key Technical Features (design / simulation)

| Feature | Description |
|--------|-------------|
| Fully Decentralized | No permanent central command or leader drone in the architecture |
| Self-Healing (sim) | Automatic reformation after simulated drone loss while preserving formation shape |
| Low Communication Load | Design preference for primarily passive Bluetooth RSSI |
| GPS resilience (design objective) | Intended to operate with intermittent or denied GPS; not field-validated |
| Scalable (local decisions) | Local decision-making is intended to support natural scaling |
| Adaptive Motion | Potential-field based trajectories in the simulation model |

---

## Core Algorithms

### 1. Reference Signal Propagation
In the model, the first drone that obtains reliable positioning becomes a temporary Reference Drone and broadcasts a Reference Signal (position + formation pattern + scale). The signal propagates only to the nearest neighbor (highest RSSI), creating a low-overhead distributed chain that initializes the formation.

### 2. Adaptive Artificial Potential Fields

Total force on each drone in the model:

```
F = F_rep + F_coh + F_goal
```

- **F_rep** (Repulsive): Collision avoidance term
- **F_coh** (Cohesive): Swarm integrity term
- **F_goal** (Attractive): Mission objective term

This produces smooth trajectories and collision avoidance behavior in simulation.

### 3. Distributed Self-Healing
Every drone continuously monitors its neighbors via RSSI in the model. When a missing neighbor is detected, a local query is initiated. If no response is received, the swarm reforms while preserving the overall formation shape (simulation behavior).

---

## Intended application domains (research targets)

Candidate domains for future evaluation—not proven operational deployments:

- **Agricultural spraying** – Large-area coverage with formation resilience as a design goal
- **Disaster response & search-and-rescue** – Operation in infrastructure-degraded and low-signal environments (research target)
- **Area scanning & security** – Persistent coverage concepts under study
- **UAV coordination research** – Resilience to single-point failures and degraded navigation as architectural goals (not a certified tactical or defense product)
- **Corridor / infrastructure monitoring concepts** – Continuous monitoring scenarios as possible future pilots

---

## Simulation Status

Current implementation includes:
- Python-based 2D swarm simulation
- Reference signal chain initialization
- Adaptive potential field motion
- Self-healing under random drone loss
- Visual validation of formation stability

Simulation code is located in `src/`.

Hardware prototype, UWB integration, and field trials remain **planned**, not completed.

---

## Anne AI & Ethical Framework

EDCS is being developed within Vitavolt’s broader technology vision that also includes **ANNE** (ANNE — AGI-Oriented Open Cognitive Architecture) as a related research thread focused on cognitive orchestration and responsible autonomy.

The long-term research goal is to explore whether ethical decision layers and multi-agent coordination principles from ANNE-style architectures can inform physical swarm systems such as EDCS. This remains a research direction, not an integrated product claim.

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

EDCS is positioned as a strategic research technology within **Vitavolt Global Enerji**.

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

*EDCS — research architecture for resilient decentralized swarm coordination (simulation prototype).*
