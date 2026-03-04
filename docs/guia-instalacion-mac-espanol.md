# Guía de Instalación de SillyTavern en macOS y Configuración con LM Studio

Esta guía está diseñada para ayudarte a instalar SillyTavern en tu Mac paso a paso, de la manera más sencilla posible, incluso si no tienes conocimientos técnicos previos.

## ¿Qué es SillyTavern?
Es una interfaz (como una aplicación de chat) que te permite hablar con personajes de Inteligencia Artificial que funcionan en tu propio ordenador (usando LM Studio), sin necesidad de internet y de forma privada.

---

## Paso 1: Preparar las herramientas necesarias

Para que SillyTavern funcione, necesitamos instalar un "motor" llamado **Node.js**.

1. Ve a la página oficial: [nodejs.org](https://nodejs.org/).
2. Haz clic en el botón que dice **"LTS"** (es la versión más estable).
3. Descarga el instalador para Mac, ábrelo y sigue los pasos como con cualquier otra aplicación.

---

## Paso 2: Descargar e instalar SillyTavern

No te asustes, usaremos la "Terminal", pero solo copia y pega lo que verás aquí.

1. Abre el **Terminal** en tu Mac (puedes buscarlo con la lupa arriba a la derecha escribiendo "Terminal").
2. Escribe (o copia y pega) este comando y pulsa la tecla Enter:
   ```bash
   git clone https://github.com/SillyTavern/SillyTavern.git
   ```
   *Esto descargará el programa en una carpeta llamada SillyTavern.*
3. Ahora entra en esa carpeta con este comando y pulsa Enter:
   ```bash
   cd SillyTavern
   ```
4. Finalmente, inicia el programa con este comando y pulsa Enter:
   ```bash
   ./start.sh
   ```
   *La primera vez tardará un poco porque descargará lo que necesita para funcionar.*

Cuando termine, se abrirá automáticamente una ventana en tu navegador. Si no se abre, escribe `http://localhost:8000` en la barra de direcciones de tu navegador (Safari o Chrome).

---

## Paso 3: Configurar LM Studio (Tu motor de IA)

Como ya tienes LM Studio instalado, solo tenemos que "encenderlo":

1. Abre **LM Studio**.
2. En la barra de la izquierda, haz clic en el icono que parece una **doble flecha (<->)**. Es el "Local Server".
3. Arriba del todo, elige el modelo que quieras usar (si no tienes ninguno, ve a la lupa y busca "Llama 3" o "Mistral" y descárgalo).
4. Haz clic en el botón verde **"Start Server"**.
5. Verás que pone algo como `Server is listening on port 1234`. ¡Perfecto!

---

## Paso 4: Conectar SillyTavern con LM Studio

Ahora vamos a decirle a SillyTavern que use el cerebro de LM Studio:

1. En la ventana de SillyTavern (en tu navegador), haz clic en el icono de un **Enchufe** arriba a la derecha.
2. Donde pone **"API Type"**, selecciona **"Chat Completion"**.
3. Donde pone **"Chat Completion Source"**, selecciona **"Custom (OpenAI-compatible)"**.
4. En el recuadro de **"URL"**, escribe esto: `http://localhost:1234/v1`
5. En el cuadro de **"API Key"**, escribe cualquier cosa (por ejemplo: `123`). Aunque ponga opcional, a veces SillyTavern lo necesita para conectar.
6. Haz clic en el botón **"Connect"**.
7. Justo debajo, en **"Model"**, **selecciona tu modelo** en el desplegable. Si no lo seleccionas, el chat no funcionará.

---

## Cómo hablar en Español

Para que la IA te responda siempre en español:

- **Selecciona un modelo multilingüe**: En LM Studio, busca modelos que digan "multilingual".
- **Configura tu personaje**: Haz clic en el icono del personaje (el busto de una persona), y en la sección "Description" o "Scenario", escribe al final: "Responder siempre en español".
- **Tu perfil**: Haz clic en el icono de "User" (a la izquierda) y en tu descripción pon que prefieres hablar en castellano.

¡Ya está! Ahora puedes elegir un personaje o crear uno nuevo y empezar a chatear.

---

## Cómo volver a abrir SillyTavern (Reiniciar)

SillyTavern se detiene cuando cierras el Terminal o apagas el Mac. Para volver a abrirlo:

1. Abre el **Terminal**.
2. Escribe `cd SillyTavern` y pulsa Enter.
3. Escribe `./start.sh` y pulsa Enter.

### Crear un acceso directo (Botón de inicio rápido)

Para no tener que escribir comandos cada vez, puedes crear un archivo ".command":

1. Abre **TextEdit** y ve a **Formato > Convertir a texto sencillo**.
2. Pega este contenido:
   ```bash
   #!/bin/bash
   cd -- "$(dirname "$0")"
   ./start.sh
   ```
3. Guárdalo como `IniciarST.command` dentro de la carpeta SillyTavern.
4. En el **Terminal**, escribe esto una vez para darle permiso: `chmod +x ~/SillyTavern/IniciarST.command`

Ahora podrás iniciar el programa haciendo **doble clic** en ese archivo.

---

## Solución de Problemas Comunes

### Error 504: Gateway Timeout
Si intentas conectarte a un servicio externo y recibes un error **"504: Gateway Timeout"**, esto suele significar que el servidor remoto está tardando demasiado en procesar la respuesta. Esto es frecuente en servicios de IA gratuitos o muy demandados.

**La solución recomendada** es usar SillyTavern **localmente** con su propio motor de IA (como se explica en esta guía). Al ejecutar todo en tu propio ordenador:
- Evitas los tiempos de espera (timeouts) de servidores externos.
- No dependes de si una web está caída o lenta.
- Tus conversaciones son 100% privadas y no salen de tu máquina.
