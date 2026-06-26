#!/usr/bin/env python3
"""
EDCS - Emergent Drone Coordination System
Basit Swarm Simülasyonu (Boids + Adaptive Potential Field + Self-Healing)

Gereksinimler:
    pip install numpy matplotlib

Kullanım:
    python src/edcs_swarm_sim.py --drones 15 --formation grid --steps 300
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Drone:
    position: np.ndarray
    velocity: np.ndarray
    id: int
    active: bool = True


class EDCSSwarm:
    def __init__(self, n_drones: int = 15, formation: str = "grid", 
                 world_size: float = 100.0, neighbor_radius: float = 15.0):
        self.n_drones = n_drones
        self.world_size = world_size
        self.neighbor_radius = neighbor_radius
        self.formation = formation
        self.drones: List[Drone] = []
        self.history: List[List[np.ndarray]] = []
        
        self._init_swarm()
    
    def _init_swarm(self):
        """ İlk formasyonu oluştur """
        if self.formation == "grid":
            side = int(np.ceil(np.sqrt(self.n_drones)))
            positions = []
            for i in range(self.n_drones):
                x = (i % side) * 8 - (side * 4) / 2
                y = (i // side) * 8 - (side * 4) / 2
                positions.append(np.array([x, y]))
        elif self.formation == "circle":
            angles = np.linspace(0, 2 * np.pi, self.n_drones, endpoint=False)
            radius = 20
            positions = [np.array([radius * np.cos(a), radius * np.sin(a)]) 
                        for a in angles]
        else:  # random
            positions = [np.random.uniform(-30, 30, 2) for _ in range(self.n_drones)]
        
        for i, pos in enumerate(positions):
            vel = np.random.uniform(-1, 1, 2)
            self.drones.append(Drone(position=pos, velocity=vel, id=i))
    
    def get_neighbors(self, drone: Drone) -> List[Drone]:
        """Komşuları bul (RSSI simülasyonu)"""
        neighbors = []
        for other in self.drones:
            if other.id != drone.id and other.active:
                dist = np.linalg.norm(drone.position - other.position)
                if dist < self.neighbor_radius:
                    neighbors.append(other)
        return neighbors
    
    def separation(self, drone: Drone, neighbors: List[Drone]) -> np.ndarray:
        """Ayrılma kuvveti"""
        if not neighbors:
            return np.zeros(2)
        force = np.zeros(2)
        for n in neighbors:
            diff = drone.position - n.position
            dist = np.linalg.norm(diff)
            if dist > 0:
                force += diff / (dist ** 2)
        return force
    
    def alignment(self, drone: Drone, neighbors: List[Drone]) -> np.ndarray:
        """Hizalama kuvveti"""
        if not neighbors:
            return np.zeros(2)
        avg_vel = np.mean([n.velocity for n in neighbors], axis=0)
        return avg_vel - drone.velocity
    
    def cohesion(self, drone: Drone, neighbors: List[Drone]) -> np.ndarray:
        """Birleşme kuvveti"""
        if not neighbors:
            return np.zeros(2)
        center = np.mean([n.position for n in neighbors], axis=0)
        return center - drone.position
    
    def adaptive_potential_field(self, drone: Drone, neighbors: List[Drone], 
                                  goal: np.ndarray = None) -> np.ndarray:
        """Adaptive Potential Field kuvveti"""
        force = np.zeros(2)
        
        # Çekim (hedefe doğru)
        if goal is not None:
            to_goal = goal - drone.position
            dist = np.linalg.norm(to_goal)
            if dist > 0:
                force += 0.8 * to_goal / dist
        
        # İtme (komşulardan)
        for n in neighbors:
            diff = drone.position - n.position
            dist = np.linalg.norm(diff)
            if 0 < dist < self.neighbor_radius:
                force += 1.5 * diff / (dist ** 2)
        
        return force
    
    def self_healing(self, drone: Drone):
        """Self-Healing: En yakın komşuya yönelme"""
        if not drone.active:
            return np.zeros(2)
        
        # Aktif komşuları bul
        active_neighbors = [d for d in self.drones 
                           if d.id != drone.id and d.active]
        
        if not active_neighbors:
            return np.zeros(2)
        
        # En yakın komşuyu bul
        distances = [np.linalg.norm(drone.position - n.position) 
                    for n in active_neighbors]
        closest_idx = np.argmin(distances)
        closest = active_neighbors[closest_idx]
        
        # Boşluğa doğru hafifçe çekil
        return 0.3 * (closest.position - drone.position)
    
    def update(self, dt: float = 0.5, goal: np.ndarray = None):
        """Bir adım simülasyon"""
        new_velocities = []
        
        for drone in self.drones:
            if not drone.active:
                new_velocities.append(np.zeros(2))
                continue
            
            neighbors = self.get_neighbors(drone)
            
            # Boids kuvvetleri
            sep = self.separation(drone, neighbors)
            ali = self.alignment(drone, neighbors)
            coh = self.cohesion(drone, neighbors)
            
            # Potential Field
            pot = self.adaptive_potential_field(drone, neighbors, goal)
            
            # Self-Healing
            heal = self.self_healing(drone)
            
            # Toplam kuvvet
            total_force = (1.0 * sep + 
                          0.8 * ali + 
                          0.6 * coh + 
                          1.2 * pot + 
                          0.4 * heal)
            
            # Hız güncelle
            new_vel = drone.velocity + total_force * dt
            new_vel = np.clip(new_vel, -3, 3)  # Maksimum hız sınırı
            new_velocities.append(new_vel)
        
        # Pozisyon ve hız güncelle
        for i, drone in enumerate(self.drones):
            if drone.active:
                drone.velocity = new_velocities[i]
                drone.position += drone.velocity * dt
                
                # Dünya sınırları
                drone.position = np.clip(drone.position, 
                                        -self.world_size/2, 
                                        self.world_size/2)
        
        # Simülasyon geçmişini kaydet
        self.history.append([d.position.copy() for d in self.drones])
    
    def simulate_drone_loss(self, drone_id: int):
        """Drone kaybı simülasyonu (Self-Healing testi)"""
        for drone in self.drones:
            if drone.id == drone_id:
                drone.active = False
                print(f"⚠️  Drone {drone_id} devre dışı bırakıldı (Self-Healing testi)")
                break
    
    def plot(self, step: int, goal: np.ndarray = None):
        """Görselleştirme"""
        plt.figure(figsize=(10, 10))
        
        # Drone pozisyonları
        for drone in self.drones:
            if drone.active:
                plt.scatter(drone.position[0], drone.position[1], 
                           c='blue', s=200, marker='o', edgecolors='black')
                plt.text(drone.position[0], drone.position[1] + 3, 
                        str(drone.id), ha='center', fontsize=9)
            else:
                plt.scatter(drone.position[0], drone.position[1], 
                           c='red', s=200, marker='x', linewidths=3)
        
        # Komşu bağlantıları çiz
        for drone in self.drones:
            if not drone.active:
                continue
            neighbors = self.get_neighbors(drone)
            for n in neighbors:
                plt.plot([drone.position[0], n.position[0]],
                        [drone.position[1], n.position[1]],
                        'g--', alpha=0.3, linewidth=1)
        
        # Hedef
        if goal is not None:
            plt.scatter(goal[0], goal[1], c='green', s=300, 
                       marker='*', edgecolors='black', linewidths=2, 
                       label='Hedef')
        
        plt.xlim(-self.world_size/2, self.world_size/2)
        plt.ylim(-self.world_size/2, self.world_size/2)
        plt.grid(True, alpha=0.3)
        plt.title(f"EDCS Swarm Simülasyonu - Adım {step}\n"
                 f"Aktif Drone: {sum(d.active for d in swarm.drones)}/{self.n_drones}")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"edcs_step_{step:04d}.png", dpi=150, bbox_inches='tight')
        plt.close()


def main():
    parser = argparse.ArgumentParser(description="EDCS Swarm Simülasyonu")
    parser.add_argument("--drones", type=int, default=15, help="Drone sayısı")
    parser.add_argument("--formation", type=str, default="grid", 
                       choices=["grid", "circle", "random"])
    parser.add_argument("--steps", type=int, default=200, help="Simülasyon adımı")
    parser.add_argument("--loss", type=int, default=None, 
                       help="Hangi drone devre dışı bırakılsın (Self-Healing testi)")
    parser.add_argument("--loss_step", type=int, default=50, 
                       help="Drone kaybı hangi adımda olsun")
    parser.add_argument("--plot_every", type=int, default=20, 
                       help="Kaç adımda bir görsel kaydet")
    args = parser.parse_args()
    
    print("=" * 60)
    print("EDCS - Emergent Drone Coordination System")
    print("Basit Swarm Simülasyonu")
    print("=" * 60)
    
    swarm = EDCSSwarm(n_drones=args.drones, formation=args.formation)
    
    # Hedef (formasyonun biraz üstü)
    goal = np.array([0, 40])
    
    print(f"\nDrone sayısı: {args.drones}")
    print(f"Formasyon: {args.formation}")
    print(f"Toplam adım: {args.steps}")
    if args.loss is not None:
        print(f"Drone {args.loss} adım {args.loss_step}'te devre dışı bırakılacak")
    print("\nSimülasyon başlıyor...\n")
    
    for step in range(args.steps):
        # Self-Healing testi
        if args.loss is not None and step == args.loss_step:
            swarm.simulate_drone_loss(args.loss)
        
        swarm.update(goal=goal)
        
        if step % args.plot_every == 0:
            swarm.plot(step, goal=goal)
            print(f"Adım {step:4d} | Aktif Drone: {sum(d.active for d in swarm.drones)}/{args.drones}")
    
    print("\n" + "=" * 60)
    print("Simülasyon tamamlandı!")
    print(f"Sonuç görselleri: edcs_step_*.png")
    print("=" * 60)


if __name__ == "__main__":
    main()