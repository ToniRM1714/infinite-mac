# SillyTavern macOS Installation & LM Studio Setup Guide

This guide provides step-by-step instructions to install SillyTavern on macOS and connect it to LM Studio for a fully offline AI chat experience.

## Prerequisites

- **Node.js**: SillyTavern requires Node.js version 18 or higher. You can download it from [nodejs.org](https://nodejs.org/).
- **Git**: Required to clone the repository. Usually pre-installed on macOS, or available via Homebrew.
- **LM Studio**: Download and install it from [lmstudio.ai](https://lmstudio.ai/).

## Step 1: Install SillyTavern

1. Open your **Terminal** application.
2. Clone the SillyTavern repository to your desired location:
   ```bash
   git clone https://github.com/SillyTavern/SillyTavern.git
   ```
3. Navigate into the directory:
   ```bash
   cd SillyTavern
   ```
4. Start SillyTavern:
   ```bash
   ./start.sh
   ```
   *The first time you run this, it will install the necessary dependencies.*

Once started, SillyTavern will be available in your browser at `http://localhost:8000`.

## Step 2: Setup LM Studio

1. Open **LM Studio**.
2. Search for and download a model (e.g., "Llama 3" or "Mistral").
   - *Tip: For Spanish (Castellano) chats, look for models labeled as "multilingual" or check the model description for Spanish support.*
3. Go to the **Local Server** tab (double arrow icon on the left sidebar).
4. Select your downloaded model from the top dropdown.
5. Click **Start Server**. Note the "Base URL", which is usually `http://localhost:1234`.

## Step 3: Connect SillyTavern to LM Studio

1. Open SillyTavern in your browser (`http://localhost:8000`).
2. Click on the **Plug** icon at the top to open the **API Connections** menu.
3. Set **API Type** to `Chat Completion`.
4. Set **Chat Completion Source** to `Custom (OpenAI-compatible)`.
5. In the **URL** field, enter the LM Studio server address: `http://localhost:1234/v1`.
6. Click **Connect**.
7. Once connected, select your model in the **Model** dropdown.

## Chatting in Spanish (Castellano)

You can definitely chat in Spanish! Here are some tips:
- **Choose the right model**: Most modern models like Llama 3, Mistral, and Gemma are excellent at understanding and responding in Spanish.
- **Character Configuration**: You can edit your character's "Description" or "Scenario" to specify that the conversation should be in Spanish.
- **User Persona**: In SillyTavern, you can create a "User Persona" (User icon on the left) and specify that you prefer to communicate in Spanish.
- **Translation Extension**: SillyTavern includes a built-in translation extension (accessible via the Extensions menu) that can automatically translate incoming and outgoing messages if needed.
