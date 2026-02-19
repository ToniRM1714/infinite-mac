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
