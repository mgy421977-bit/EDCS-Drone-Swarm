# EDCS - Emergent Drone Coordination System

**Dağıtık ve Kendi Kendini Onaran Drone Sürüsü Sistemi**

EDCS, merkezi komuta gerektirmeyen, tamamen dağıtık (decentralized) çalışan ve **self-healing** yeteneğine sahip bir drone sürüsü mimarisidir. Sistem, GPS'siz ortamlarda ve drone kaybı durumunda otomatik olarak formasyonu koruyarak çalışır.

## Özellikler

- **Tamamen Dağıtık Mimari** — Merkezi komuta, lider drone veya yer istasyonu gerektirmez
- **Self-Healing** — Drone kaybı durumunda otomatik formasyon onarımı
- **Minimum İletişim** — Sadece Bluetooth RSSI (opsiyonel UWB) ile yerel koordinasyon
- **GPS Bağımsız** — Jamming/spoofing riskine dayanıklı
- **Adaptive Potential Field + Boids** hibrit algoritması
- **SİHA, Tarım, Afet ve Güvenlik** uygulamalarına uygun

## Teknik Dokümantasyon

| Dosya | Açıklama |
|-------|----------|
| `EDCS_Makale.pdf` | Detaylı teknik makale (matematiksel model + algoritmalar) |
| `EDCS_Technical_Presentation.pptx` | 8 slaytlık teknik sunum (denklemler + akış diyagramları) |

## Matematiksel Model (Özet)

### Boids Algoritması (Reynolds, 1987)
