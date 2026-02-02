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
6. In the **API Key** field, enter any text (e.g., `123`). Although marked as optional, SillyTavern sometimes requires it to establish the connection.
7. Click **Connect**.
8. Once connected, **select your model** in the **Model** dropdown. If you don't select a model, the chat will not work.

## Chatting in Spanish (Castellano)

You can definitely chat in Spanish! Here are some tips:
- **Choose the right model**: Most modern models like Llama 3, Mistral, and Gemma are excellent at understanding and responding in Spanish.
- **Character Configuration**: You can edit your character's "Description" or "Scenario" to specify that the conversation should be in Spanish.
- **User Persona**: In SillyTavern, you can create a "User Persona" (User icon on the left) and specify that you prefer to communicate in Spanish.
- **Translation Extension**: SillyTavern includes a built-in translation extension (accessible via the Extensions menu) that can automatically translate incoming and outgoing messages if needed.

---

## How to Restart SillyTavern

SillyTavern stops when you close the Terminal window or restart your Mac. To start it again:

1. Open **Terminal**.
2. Type `cd SillyTavern` and press Enter.
3. Type `./start.sh` and press Enter.

### Create a Shortcut (Quick Start Button)

To avoid typing commands every time, you can create a ".command" file:

1. Open **TextEdit** and go to **Format > Make Plain Text**.
2. Paste the following:
   ```bash
   #!/bin/bash
   cd -- "$(dirname "$0")"
   ./start.sh
   ```
3. Save it as `StartST.command` inside your SillyTavern folder.
4. In the **Terminal**, run this once to give it permission: `chmod +x ~/SillyTavern/StartST.command`

Now you can start SillyTavern by **double-clicking** this file.
