# Guía: Ejecutar WarBirds en Mac con Apple Silicon (M1, M2, M3, M4)

Si tienes un Mac moderno con procesador Apple Silicon (como el nuevo Mac mini M4) y el juego **WarBirds** no abre, esta guía te explicará por qué sucede y cómo solucionarlo.

## El Problema: Arquitectura de 32 bits
El juego **WarBirds** para macOS fue desarrollado originalmente como una aplicación de **32 bits**. Apple eliminó el soporte para este tipo de aplicaciones con el lanzamiento de macOS Catalina (10.15).

Además, aunque los Macs modernos incluyen **Rosetta 2** (un traductor que permite ejecutar aplicaciones diseñadas para procesadores Intel), Rosetta 2 **solo es compatible con aplicaciones de 64 bits**. Debido a esto, la versión nativa de Mac de WarBirds no puede ejecutarse en sistemas modernos.

---

## Soluciones Sencillas (Hardware Existente)

Si dispones de equipos antiguos o un PC, estas son las opciones más directas:

### 1. Usar un Portátil PC (Recomendado)
Instalar la versión de Windows directamente en un PC portátil.
* **Ventaja:** Es la versión más estable y compatible con todos los periféricos y Joysticks sin necesidad de configuraciones complejas en macOS.

### 2. Usar Macs antiguos mediante "Compartir Pantalla"
Si ya tienes WarBirds funcionando en un Mac mini antiguo, puedes controlarlo desde tu Mac M4:
1. **En el Mac antiguo:** Activa *Compartir Pantalla* en los ajustes de Compartir.
2. **En el Mac M4:** Abre la aplicación *Compartir Pantalla* y conéctate al Mac antiguo.
3. Podrás jugar en una ventana de tu nuevo Mac utilizando la potencia del antiguo.

---

## Soluciones Técnicas en el Mac M4

### 1. Ejecutar la versión de Windows en el M4
#### Opción A: Virtualización con VMWare Fusion (Gratis) o Parallels
Permite instalar Windows 11 dentro de tu Mac. Windows 11 ARM puede ejecutar el juego de 32 bits mediante su propio traductor.
#### Opción B: Capas de compatibilidad (Whisky o CrossOver)
Ejecutan el programa de Windows sin instalar el sistema operativo completo.

### 2. Versión de iPad en el Mac
Busca "WarBirds Fighter Pilot Academy" en la Mac App Store bajo la pestaña "Apps para iPhone e iPad".

---

## Periféricos y Joysticks
La mayoría de los Joysticks estándar son reconocidos por macOS. Si tu mando usa USB-A, necesitarás un adaptador USB-C para el Mac mini M4.
