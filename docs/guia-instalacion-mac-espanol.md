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

---

## Cómo crear un Personaje en SillyTavern

Crear un personaje es la parte más divertida. Sigue estos pasos:

1.  En la barra superior de SillyTavern, haz clic en el icono del **busto de una persona** (Personajes).
2.  Haz clic en el botón con el símbolo **"+"** y elige **"Create New Character"**.
3.  **Configura los campos principales:**
    -   **Name**: El nombre del personaje.
    -   **Description**: Aquí describes quién es, su historia y cómo se comporta. Sé detallado para que la IA lo entienda bien.
    -   **Personality**: Define rasgos cortos (ej: "Sarcástico, valiente, protector").
    -   **First Message**: El primer mensaje que el personaje te enviará al empezar el chat. ¡Es vital para marcar el tono!
4.  **Añadir una imagen**: Haz clic en el recuadro gris vacío para subir una foto desde tu ordenador.
5.  Pulsa el botón **"Save"** (el icono del disquete) abajo a la derecha.

### Truco: Importar personajes ya creados
No tienes por qué crearlo todo de cero. Puedes descargar "tarjetas de personaje" (archivos .png que contienen la configuración) de sitios como **Chub.ai** o **SillyTavern Cards**.
Solo tienes que arrastrar ese archivo .png dentro de la ventana de SillyTavern y el personaje se configurará solo con su descripción, imagen y personalidad.

---

## De Mazmo a SillyTavern: Guía de Equivalencias

Si vienes de Mazmo, aquí tienes dónde encontrar cada opción en SillyTavern:

| En Mazmo | En SillyTavern | Ubicación en SillyTavern |
| :--- | :--- | :--- |
| **Nombre** | **Name** | Pestaña Personaje (icono busto) |
| **Descripción** | **Description** | Pestaña Personaje -> Campo "Description" |
| **Personalidad** | **Personality** | Pestaña Personaje -> Campo "Personality Summary" |
| **Categorías/Etiquetas** | **Tags** | Pestaña Personaje -> Botón "Tags" (arriba, icono etiqueta) |
| **Primer Mensaje** | **First Message** | Pestaña Personaje -> Campo "First Message" |
| **Valores Técnicos** | **Generation Settings** | Icono de Barras Deslizantes (arriba) |

### ¿Dónde están los valores técnicos (Temperatura, etc.)?

En Mazmo los valores suelen estar ocultos o simplificados. En SillyTavern, haz clic en el icono de las **Barras Deslizantes** (Configuración de IA) en la parte superior:

1.  **Temperatura**: Controla la "creatividad". (0.7 es equilibrado, 1.2 es muy creativo/caótico).
2.  **Context Size**: Cuánta memoria tiene el bot. Si usas LM Studio, suele ser lo que hayas configurado en el servidor (ej: 4096 o 8192).
3.  **Response Length**: Longitud máxima de la respuesta del bot.

Para que el bot se comporte como los de Mazmo (por ejemplo, el tag **Sádique (19)** que mencionas), simplemente añade esa palabra en el campo **Personality** y refuerza su comportamiento en la **Description**. SillyTavern es mucho más sensible a lo que escribes ahí.

---

## Cómo configurar tu propio Perfil (Tu Personaje)

En SillyTavern, tú también tienes una "ficha" para que el bot sepa quién eres y cómo debe tratarte.

1.  Busca el icono de **Usuario / Persona** (es la silueta de una persona sola, **no el engranaje de ajustes**).
2.  Una vez dentro, verás una sección llamada **"User Persona"** (o simplemente "Persona"). Allí es donde verás tu perfil (por defecto se llama "User").
3.  **Configura tus datos:**
    -   **Name**: Tu nombre en la historia.
    -   **Description**: Describe quién eres tú. Ejemplo: "Soy un joven aventurero que busca tesoros", o "Soy el jefe de Sam". Esto ayuda a la IA a entender la relación entre vosotros.
    -   **Avatar**: Puedes subir tu propia foto haciendo clic en el recuadro de la imagen.
4.  Puedes crear varios perfiles diferentes (Personas) si quieres jugar distintas historias con distintos nombres.

---

## Cómo hacer Chats de Grupo (Varios personajes a la vez)

Si quieres hablar con dos o más personajes al mismo tiempo en el mismo chat, debes usar la función de **Grupo**:

1.  Busca el icono de **Chat de Grupo** (parece la silueta de tres personas juntas). Suele estar arriba a la derecha.
2.  Pulsa en **"Create New Group"**.
3.  **Añade a los personajes:** Selecciona en la lista a los personajes que quieres que participen.
4.  **Configura el orden:** Puedes elegir si los personajes responden por turnos o de forma aleatoria.

**Nota importante:** En SillyTavern solo puede haber **un Usuario** (tú) y varios **Personajes**. Si has creado a tu segunda "persona" en el menú de Usuario, el sistema no la verá como un personaje con el que hablar. Para que estén juntos, uno debe estar creado en el menú de **Personajes** y el otro ser tú (Usuario).

---

## Cómo controlar el Ritmo (Pacing) del personaje

Si el bot avanza demasiado rápido en la historia o pasa de un paso a otro sin disfrutar el momento, debes darle instrucciones de **ritmo** en su **Description** o en el campo **Scenario**:

### Instrucciones para "frenar" a la IA:
Añade frases como estas al final de su descripción:
- *"El personaje es pausado y disfruta de cada acción. No pasa al siguiente paso hasta que el usuario se lo pida explícitamente."*
- *"Escribe respuestas largas y detalladas centrándote en el momento presente."*
- *"Si hay una lista de pasos, el personaje debe repetir y recrearse en el paso actual varias veces antes de sugerir el siguiente."*

### Uso de la Nota del Autor (Author's Note):
Si durante el chat ves que corre mucho, puedes usar la **Nota del Autor** (en el icono de Extensiones -> Author's Note):
- Escribe allí: *"[Ritmo: lento. Céntrate en repetir la acción actual y no avances en la lista]"*.
Esto actúa como un recordatorio constante para la IA mientras habláis.
