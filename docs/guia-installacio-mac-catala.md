# Guia d'instal·lació de SillyTavern a macOS i configuració d'LM Studio

Aquesta guia proporciona instruccions pas a pas per instal·lar SillyTavern a macOS i connectar-lo a LM Studio per tenir una experiència de xat amb IA totalment fora de línia.

## Requisits previs

- **Node.js**: SillyTavern requereix la versió 18 de Node.js o superior. Pots descarregar-lo a [nodejs.org](https://nodejs.org/).
- **Git**: Necessari per clonar el repositori. Normalment ja ve instal·lat a macOS, o es pot instal·lar mitjançant Homebrew.
- **LM Studio**: Descarrega i instal·la'l des de [lmstudio.ai](https://lmstudio.ai/).

## Pas 1: Instal·lar SillyTavern

1. Obre l'aplicació **Terminal**.
2. Clona el repositori de SillyTavern a la ubicació que vulguis:
   ```bash
   git clone https://github.com/SillyTavern/SillyTavern.git
   ```
3. Entra al directori:
   ```bash
   cd SillyTavern
   ```
4. Inicia SillyTavern:
   ```bash
   ./start.sh
   ```
   *La primera vegada que l'executis, s'instal·laran les dependències necessàries.*

Un cop iniciat, SillyTavern estarà disponible al teu navegador a `http://localhost:8000`.

## Pas 2: Configurar LM Studio

1. Obre **LM Studio**.
2. Busca i descarrega un model (per exemple, "Llama 3" o "Mistral").
   - *Consell: Per als xats en castellà, busca models etiquetats com a "multilingual" o consulta la descripció del model per veure si admet l'espanyol.*
3. Ves a la pestanya **Local Server** (icona de la doble fletxa a la barra lateral esquerra).
4. Selecciona el model que has descarregat al desplegable de la part superior.
5. Fes clic a **Start Server**. Fixa't en la "Base URL", que sol ser `http://localhost:1234`.

## Pas 3: Connectar SillyTavern a LM Studio

1. Obre SillyTavern al navegador (`http://localhost:8000`).
2. Fes clic a la icona de l'**Endoll** a la part superior per obrir el menú **API Connections**.
3. Estableix l'**API Type** a `Chat Completion`.
4. Estableix el **Chat Completion Source** a `Custom (OpenAI-compatible)`.
5. Al camp **URL**, introdueix l'adreça del servidor d'LM Studio: `http://localhost:1234/v1`.
6. Fes clic a **Connect**.
7. Un cop connectat, selecciona el teu model al desplegable **Model**.

## Xatejar en Castellà (Espanyol)

Sí, pots xatejar en castellà sense cap problema! Aquí tens alguns consells:
- **Tria el model adequat**: La majoria de models moderns com Llama 3, Mistral i Gemma entenen i responen perfectament en castellà.
- **Configuració del Personatge**: Pots editar la "Descripció" o el "Escenari" del teu personatge per especificar que la conversa ha de ser en espanyol.
- **Persona de l'usuari**: A SillyTavern, pots crear una "User Persona" (icona d'usuari a l'esquerra) i especificar que prefereixes comunicar-te en castellà.
- **Extensió de traducció**: SillyTavern inclou una extensió de traducció integrada (accessible des del menú Extensions) que pot traduir automàticament els missatges si cal.
