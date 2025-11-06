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
# dentro de notas-rapidas/
composer install
cp .env.example .env
php artisan key:generate

# Base de datos SQLite
type nul > database\database.sqlite

# Migraciones
php artisan migrate

# Levantar API
php artisan serve
```

En .env debe quedar:

```bash
DB_CONNECTION=sqlite
DB_DATABASE=./database/database.sqlite

```

3) Frontend (Vite + Vue):

- Node v20.17.0 y npm v10.8.2
  
- Tailwind v4 + PostCSS

```bash
# en otra terminal también dentro de notas-rapidas/
npm install
npm run dev
```

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
└─vite.config.ts
```

# 2. Manipulación de listas y diccionarios
- Python v3.12.6

# 3. Lectura de archivos
- Python v3.12.6
- datos.txt
