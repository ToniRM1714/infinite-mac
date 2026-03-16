# Guía de Generación de Imágenes con Draw Things en macOS

**Draw Things** es una de las mejores aplicaciones para generar imágenes en Mac porque es nativa, muy rápida y totalmente privada. Si has tenido problemas con ComfyUI, Draw Things es mucho más sencillo de usar.

---

## Paso 1: Configurar Draw Things para permitir conexiones

Para que SillyTavern pueda enviarle órdenes a Draw Things, primero debemos activar su "servidor".

1.  Abre la aplicación **Draw Things** en tu Mac.
2.  Haz clic en el icono de la **rueda dentada (Ajustes)** que verás abajo a la izquierda.
3.  Desliza hacia abajo hasta encontrar la sección **"API Server"**.
4.  Activa la opción **"Enable API Server"**.
5.  Asegúrate de que el puerto sea el `7860` (es el que viene por defecto).
6.  **Importante:** Mantén la aplicación Draw Things abierta mientras uses SillyTavern.

---

## Paso 2: Conectar SillyTavern a Draw Things

1.  Abre SillyTavern en tu navegador.
2.  Haz clic en el icono de las **Extensiones** (la pieza de puzzle arriba).
3.  Busca la sección **"Image Generation"** (Generación de imágenes).
4.  En el desplegable de **"Source"** (Fuente), elige **"Draw Things"**.
5.  En el cuadro de **"API URL"**, escribe: `http://127.0.0.1:7860`.
6.  Haz clic en el botón **"Connect"**. Si sale un mensaje verde indicando éxito, ¡ya están vinculados!

---

## Paso 3: Generar tu primera imagen

1.  En el chat, verás que ha aparecido un icono nuevo de una **montaña** o una **varita** cerca de donde escribes.
2.  Puedes escribir un mensaje normal a tu personaje y luego darle a ese botón para que genere una imagen de la situación.
3.  También puedes usar el comando manual escribiendo: `/sd un astronauta en la luna`.

---

## Consejos para Mac

-   **Modelos:** Draw Things te permite descargar muchos modelos diferentes (SDXL, SD 1.5, etc.) directamente desde la app. Te recomiendo usar **SDXL Turbo** o **SDXL Lightning** si quieres que las imágenes se generen en pocos segundos.
-   **Memoria:** Al igual que con LM Studio, estas aplicaciones consumen mucha memoria. Si notas que tu Mac va lento, intenta usar un modelo más pequeño en LM Studio (como el que ya tienes de 1b) mientras generas imágenes.
-   **Sin Errores:** A diferencia de ComfyUI, Draw Things no suele dar errores de "validación de API" si está el servidor encendido.

¡Disfruta viendo a tus personajes cobrar vida!

---

## Solución de Problemas y Conceptos Clave

### ¿Por qué la imagen no se parece a lo que dice el chat?
SillyTavern intenta resumir el último mensaje para enviárselo a Draw Things. Si quieres mejorar esto, configura lo siguiente en la pestaña de **Extensiones -> Image Generation**:

1.  **Character Visual Description**: En la ficha del personaje, asegúrate de rellenar el campo de descripción visual (pelo, ropa, rasgos). SillyTavern añadirá esto a todas las imágenes para que el personaje siempre sea el mismo.
2.  **Prompt Prefix/Suffix**: Añade palabras como `masterpiece, high quality, realistic` para mejorar el estilo artístico.
3.  **Uso de la IA para el Prompt**: Puedes configurar que sea **LM Studio** quien redacte el "prompt" de la imagen basándose en la historia, en lugar de que SillyTavern simplemente copie el último párrafo.

### El papel de LM Studio vs Draw Things
Es normal preguntarse: *¿Para qué necesito LM Studio si puedo copiar el texto en Draw Things yo mismo?*

-   **LM Studio (El Escritor):** Se encarga de la lógica, la memoria y la personalidad. Entiende la historia y decide *qué* está pasando.
-   **Draw Things (El Pintor):** Solo sabe pintar lo que le pides en el momento. No sabe quién eres tú ni qué pasó hace diez mensajes.
-   **SillyTavern (El Director):** Conecta a ambos. SillyTavern lee lo que LM Studio escribe, extrae la esencia visual y le dice a Draw Things qué pintar de forma automática.

La ventaja es la **automatización y la coherencia**: no tienes que salir del chat ni copiar/pegar nada; la imagen aparece como parte de la experiencia narrativa.

---

## Cómo hacer que LM Studio redacte las descripciones automáticamente

Si no quieres que SillyTavern se limite a copiar el último mensaje, puedes pedirle a **LM Studio** que redacte una descripción artística (un "prompt") por ti.

1.  Ve a la pestaña de **Extensiones** (pieza de puzzle 🧩) y haz clic en la opción **"Image Generation"**. Se abrirá un panel nuevo a la derecha.
2.  Dentro de ese panel, busca la sección **"Prompt Creation"**.
    -   *Nota:* Si no ves esa opción ahí, busca en el menú principal de Extensiones (la pieza de puzzle) una opción llamada **"Plantillas de aviso de SD"** (SD Prompt Templates).
3.  Asegúrate de que el **"Modo interactivo"** esté activado.
4.  En el cuadro de instrucciones (que puede llamarse **"Aviso para aviso"**), puedes poner una instrucción como esta:
    -   *"Redacta un prompt de imagen corto y descriptivo en inglés basado en el último mensaje del chat. Céntrate en la apariencia, la ropa y el entorno. Solo devuelve el prompt, sin introducciones."*
5.  **Aviso de rendimiento:** Ten en cuenta que esto hará que LM Studio trabaje el doble (primero para responderte al chat y luego para pensar la imagen), por lo que tardará unos segundos más.
