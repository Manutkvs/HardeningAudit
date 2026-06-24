# HardeningAudit
HardeningAudit es una herramienta ligera de automatización escrita en Python diseñada para auditar configuraciones de seguridad en sistemas Linux. Ayuda a administradores y entusiastas de la ciberseguridad a identificar rápidamente configuraciones débiles (misconfigurations) que podrían comprometer la integridad del sistema.

## 🚀 Características
- Verificación de políticas de SSH (Root login, autenticación por clave).
- Escaneo de puertos abiertos en escucha.
- Detección de permisos inseguros en archivos críticos (ej. /etc/shadow).
- Reportes rápidos en consola.

## 📋 Prerrequisitos
- Python 3.x instalado.
- Privilegios de superusuario (sudo) para acceder a configuraciones del sistema.

## 🛠 Instalación
```bash
git clone [https://github.com/tu-usuario/SecSentinel-Linux.git](https://github.com/tu-usuario/SecSentinel-Linux.git)
cd SecSentinel-Linux
pip install -r requirements.txt
