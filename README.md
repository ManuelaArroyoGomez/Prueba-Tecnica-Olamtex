# Prueba Tecnica


# 1. Notas Rápidas

## Guía de instalación y ejecución

1) Comunes:

- Git

- Editor recomendado: VS Code

2) Backend (Laravel):

- PHP v8.3.26 y Composer v2.8.12

- Extensiones PHP: pdo_sqlite, sqlite3 habilitadas

- Node v20.17.0 (para Vite/HMR)

```bash
php artisan key:generate
php artisan migrate
php artisan serve
```

3) Frontend (Vite + Vue):

- Node v20.17.0 y npm v10.8.2

```bash
npm run dev  
```

## Backend (Laravel)

## Estructura

```plaintext
notas-rapidas/
├─ app/
│  └─ Http/Controllers/NoteController.php
├─ database/
│  ├─ database.sqlite
│  └─ migrations/2025_xx_xx_create_notes_table.php
├─ resources/
│  ├─ css/app.css
│  ├─ js/
│  │  ├─ app.ts
│  │  └─ components/NotesApp.vue
│  └─ views/welcome.blade.php
├─ routes/
│  ├─ api.php
│  └─ web.php
├─ postcss.config.js
├─ vite.config.ts
└─ README.md
```

# 2. Manipulación de listas y diccionarios
- Python v3.12.6

# 3. Lectura de archivos
- Python v3.12.6
- datos.txt
