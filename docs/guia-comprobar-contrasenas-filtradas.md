# Guía para saber si tus cuentas o contraseñas han sido filtradas o hackeadas

Si te preocupa que alguna de tus contraseñas o cuentas de correo electrónico haya sido comprometida en una filtración de datos (hackeo masivo o *data breach*), existen métodos gratuitos, seguros y sencillos para comprobarlo sin poner en riesgo tu seguridad.

---

## 1. Comprobación de tu correo en "Have I Been Pwned?" (HIBP)

**Have I Been Pwned?** (`haveibeenpwned.com`) es el servicio web más reconocido y fiable a nivel mundial para verificar filtraciones. Fue creado por el experto en ciberseguridad Troy Hunt.

### Pasos para usarlo:
1. Abre tu navegador web e ingresa a: **[https://haveibeenpwned.com/](https://haveibeenpwned.com/)**.
2. En la barra de búsqueda, escribe tu **dirección de correo electrónico** (o tu número de teléfono en formato internacional).
3. Haz clic en el botón **"pwned?"**.

### ¿Cómo interpretar el resultado?
* **Fondo Verde (*"Good news — no pwnage found!"*)**: Tu correo no aparece en ninguna base de datos pública de filtraciones masivas conocidas por el sitio.
* **Fondo Rojo (*"Oh no — pwned!"*)**: Tu correo forma parte de una o varias filtraciones. Al desplazar la página hacia abajo, verás la lista de servicios/páginas web que sufrieron el ataque (por ejemplo, Wattpad, LinkedIn, Canva, etc.) y qué datos se filtraron (contraseñas, correos, nombres de usuario, etc.).

> **Nota de seguridad:** Nunca introduzcas tus contraseñas reales en sitios web de comprobación abierta. HaveIBeenPwned solo solicita tu correo o usuario.

---

## 2. Gestores de contraseñas integrados (Navegadores y Sistemas)

Hoy en día, la mayoría de los navegadores y sistemas operativos incluyen alertas automáticas de contraseñas vulneradas o filtradas.

### A) Google Chrome (PC, Mac, Android e iOS)
1. Abre Chrome y haz clic en los **tres puntos** (arriba a la derecha) > **Configuración**.
2. Ve a la sección **Autocompletar y contraseñas** > **Administrador de contraseñas de Google**.
3. Haz clic en **Comprobación de contraseñas** (*Password Checkup*).
4. Chrome analizará tus claves guardadas e indicará si alguna de ellas ha sido expuesta en una filtración pública.

### B) Apple (iPhone, iPad, Mac - Llavero de iCloud / Contraseñas)
1. En Mac: Abre **Ajustes del Sistema** > **Contraseñas** (o la app **Contraseñas** en macOS Sequoia).
2. En iPhone/iPad: Abre **Ajustes** > **Contraseñas**.
3. Revisa la sección **Recomendaciones de seguridad**.
4. El sistema te mostrará con un aviso de advertencia si alguna contraseña guardada aparece en filtraciones conocidas.

### C) Mozilla Firefox (Firefox Monitor)
1. Entra en **[https://monitor.firefox.com/](https://monitor.firefox.com/)**.
2. Inicia sesión con tu cuenta de Firefox o ingresa tu correo para realizar el escaneo de filtraciones.

---

## 3. ¿Qué hacer si descubres que una contraseña ha sido hackeada?

Si confirmas que tus datos o contraseñas han sido filtrados, sigue estos pasos inmediatos:

1. **Cambia la contraseña inmediatamente**:
   * Entra al sitio web o servicio afectado y actualiza tu clave.
   * **Muy importante:** Si usabas esa misma contraseña en otros sitios (Gmail, redes sociales, bancos, etc.), cámbiala también en todos esos sitios de inmediato.

2. **Crea contraseñas seguras e independientes**:
   * Utiliza una contraseña única para cada cuenta.
   * Combina letras mayúsculas, minúsculas, números y símbolos.

3. **Activa la Verificación en Dos Pasos (2FA / Autenticación de doble factor)**:
   * Activa el envío de códigos por app autenticadora (Google Authenticator, Microsoft Authenticator, 1Password, etc.) o SMS.
   * Esto evita que alguien acceda a tu cuenta aunque conozca tu contraseña.

4. **Considera usar un gestor de contraseñas dedicado**:
   * Herramientas como Bitwarden, 1Password o el propio gestor integrado de tu dispositivo te permiten generar y almacenar contraseñas complejas sin tener que memorizarlas todas.
