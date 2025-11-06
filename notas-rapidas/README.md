# Notas Rápidas

## Requisitos
- PHP 8.1+
- Composer
- Node 18+
- SQLite habilitado (pdo_sqlite, sqlite3)

## Backend (Laravel)
```bash
cp .env.example .env
php artisan key:generate
php artisan migrate
php artisan serve
