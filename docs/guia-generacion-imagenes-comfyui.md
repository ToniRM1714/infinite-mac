# Guía de Generación de Imágenes con ComfyUI en SillyTavern

Esta guía te ayudará a configurar la extensión de generación de imágenes para que tus personajes puedan "enviarte" fotos o puedas crear arte directamente desde el chat.

## Requisitos previos
1.  Tener **ComfyUI** instalado y funcionando en tu Mac.
2.  Tener al menos un modelo de generación (como SDXL o SD 1.5) descargado dentro de ComfyUI.

---

## Paso 1: Activar la extensión en SillyTavern

1.  Abre SillyTavern en tu navegador.
2.  Haz clic en el icono de las **Extensiones** (parece una pieza de rompecabezas o tres cubos apilados) en la barra superior.
3.  Busca la opción **"Image Generation"** (Generación de imágenes) y asegúrate de que esté marcada/activada.

## Paso 2: Configurar la Fuente (ComfyUI)

1.  Dentro del menú de Extensiones, expande la sección **"Image Generation"**.
2.  En el desplegable **"Source"** (Fuente), selecciona **"ComfyUI"**.
3.  En **"ComfyUI Address"**, asegúrate de que ponga: `http://127.0.0.1:8188` (es la dirección estándar).
4.  Haz clic en el botón **"Check Stats"** o **"Connect"**. Si sale un mensaje verde, ¡ya están conectados!

## Paso 3: Elegir el modelo y el flujo (Workflow)

ComfyUI es muy potente pero un poco complejo porque usa "flujos de trabajo" (workflows).

1.  **Workflow:** SillyTavern intentará usar uno por defecto. Si tienes uno propio que te gusta en ComfyUI, puedes exportarlo como JSON y cargarlo aquí, pero para empezar, deja el que viene por defecto.
2.  **Sampler / Steps:** Estos son ajustes técnicos. Si no sabes qué poner, los valores estándar son:
    *   **Steps:** 20 o 30.
    *   **Cfg Scale:** 7.
    *   **Sampler:** dpmpp_2m_sde_gpu o euler_ancestral.

## Cómo generar imágenes en el chat

Una vez configurado, tienes varias formas de usarlo:

1.  **Comando manual:** Escribe en el chat `/draw un gato con sombrero` y pulsa Enter.
2.  **Botón rápido:** Busca el icono de una **montaña** o un **cuadro** cerca de donde escribes. Al pulsarlo, generará una imagen basada en lo último que ha pasado en el chat.
3.  **Auto-generación:** En los ajustes de la extensión, puedes marcar "Sent by Character", y la IA decidirá por sí misma cuándo enviarte una imagen según la conversación.

---

## Solución de problemas comunes

-   **"Error: Connection Refused":** Asegúrate de que ComfyUI esté abierto y funcionando en otra ventana.
-   **Imágenes negras o error de memoria:** ComfyUI consume mucha potencia. Si tienes LM Studio abierto a la vez con un modelo muy grande, es posible que tu Mac se quede sin memoria (VRAM). Prueba a usar un modelo más pequeño en LM Studio si esto ocurre.
