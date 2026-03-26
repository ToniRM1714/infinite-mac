# Solución: El disco "Macintosh HD Final" no aparece en SheepShaver (Mac OS 9)

Si después de iniciar el Sistema 9 en SheepShaver no ves el disco duro **"Macintosh HD Final"** en el escritorio, sigue estos pasos para solucionarlo.

---

## 1. Comprobar la configuración de SheepShaver

El problema más común es que el archivo del disco duro no esté correctamente añadido a la lista de volúmenes de SheepShaver.

1.  **Cierra SheepShaver** completamente.
2.  Abre el configurador de SheepShaver (**SheepShaver Prefs** o la interfaz gráfica que uses).
3.  Ve a la pestaña **Volumes**.
4.  Revisa si "Macintosh HD Final" aparece en la lista.
    -   **Si no aparece**: Haz clic en **Add...** y busca el archivo del disco duro en tu Mac actual para añadirlo.
    -   **Si aparece pero está abajo**: Asegúrate de que el disco que contiene el sistema de arranque esté el primero en la lista (arriba del todo).
5.  Haz clic en **Save** o **Start**.

---

## 2. Verificar el archivo en macOS

A veces, el archivo del disco duro puede haber cambiado de sitio o tener un problema de permisos.

1.  Busca el archivo `Macintosh HD Final` (normalmente tiene extensión `.dsk`, `.img` o ninguna) en tu carpeta de SheepShaver en macOS.
2.  Asegúrate de que el archivo no esté "Bloqueado" (puedes verlo haciendo clic derecho sobre el archivo > **Obtener información**).
3.  Si has movido la carpeta de SheepShaver recientemente, es muy probable que la "ruta" (el camino hacia el archivo) haya cambiado y debas volver a añadirlo en las preferencias como explicamos en el punto 1.

---

## 3. Comprobar si el disco necesita reparación (dentro de Mac OS 9)

Si el sistema arranca pero el segundo disco no aparece, puede que el Sistema 9 lo reconozca pero no pueda "montarlo".

1.  Dentro de Mac OS 9, ve al menú de la manzana (arriba a la izquierda).
2.  Abre **Utilidades** (o busca una aplicación llamada **Disk First Aid**).
3.  Mira si el disco aparece en la lista de la izquierda de Disk First Aid. Si aparece, selecciónalo y dale a **Verify** o **Repair**.

---

## 4. Recuperar la barra de menús (Modo Pantalla Completa)

Si SheepShaver se abre en pantalla completa y no ves el menú de arriba para entrar en Preferencias:

1.  **Sal del modo pantalla completa**: Pulsa **Control + Enter** (o **Command + Enter**) mientras el emulador está en primer plano. Esto pasará a modo ventana y verás el menú arriba.
2.  **Si no funciona**: Debes editar el archivo de configuración oculto.
    -   Abre el **Terminal** en macOS.
    -   Escribe `nano ~/.sheepshaver_prefs` y pulsa Enter.
    -   Busca la línea `fullscreen true` y cámbiala a `fullscreen false`.
    -   Guarda con **Control+O**, pulsa Enter y sal con **Control+X**.

---

## 5. Problema con el "Unix Root"

Si estás usando la carpeta compartida "Unix" para mover archivos, a veces esto causa conflictos visuales.

-   Asegúrate de que no haya un conflicto de nombres entre la carpeta compartida y el nombre de tu disco duro.
-   Intenta arrancar SheepShaver sin ningún CD virtual (archivo .iso o .toast) cargado, para descartar que el sistema esté intentando leer el CD en lugar del disco duro.

---

### ¿Sigues con problemas?
Si después de estos pasos sigues sin verlo, fíjate si al arrancar el Sistema 9 te sale un mensaje preguntando si quieres **"Inicializar el disco"**.
-   **¡CUIDADO!**: No le des a inicializar si tienes datos importantes dentro, ya que eso borraría el contenido del disco para darle un formato nuevo.
