# Календарь звонков

[![hexlet-check](https://github.com/gbespamiatnykh/python-project-386/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gbespamiatnykh/python-project-386/actions)

Разработайте совместно с ИИ сервис для бронирования календаря

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://files.hexlet.app/a/2ipc5m

## Стек

- Backend: Django 6.1.3, Python 3.13
- Frontend: React 19, TypeScript 7, Vite 8
- API-контракт: TypeSpec → OpenAPI 3.1 → Orval → TypeScript SDK
- Тесты: pytest + pytest-django (backend), Vitest (frontend)
- Lint/format: Ruff (Python), Oxlint + oxfmt (TypeScript)
- Toolchain: mise, зависимости — uv и pnpm
- Git-хуки: hk + commitlint (Conventional Commits)
- CI: GitHub Actions (запускает ту же `mise run check`)

## Установка

<!-- Опишите установку: клонирование, зависимости, переменные окружения -->

Требуется [mise](https://mise.jdx.dev): `curl -fsSL https://mise.run | sh`

```bash
git clone https://github.com/gbespamiatnykh/python-project-386.git
cd python-project-386

# 1. Инструменты точно из mise.toml + mise.lock (node, python, pnpm, uv, hk, pitchfork)
mise install

# 2. Зависимости из lock-файлов (pnpm-lock.yaml, uv.lock)
mise run install

# 3. Все проверки: контракт/SDK, Ruff, pytest, Oxlint, oxfmt, tsc, Vitest, build
mise run check

# 4. Dev-серверы через mise daemons (backend :8000, frontend :5173)
mise run dev
```

## Использование

<!-- Добавьте примеры запуска и запись asciinema — именно это смотрит работодатель -->

Каркас приложения: бронирование и другие бизнес-функции пока не реализованы.

| Команда                 | Что делает                                                                |
| ----------------------- | ------------------------------------------------------------------------- |
| `mise run check`        | Все проверки проекта (локально и в CI)                                    |
| `mise run fix`          | Автофиксы lint/format                                                     |
| `mise run api:generate` | Регенерация OpenAPI из TypeSpec и TypeScript SDK из OpenAPI               |
| `mise run dev`          | Django (http://127.0.0.1:8000/api/health/) и Vite (http://127.0.0.1:5173) |
| `mise daemons stop`     | Остановить dev-серверы                                                    |

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.

## Script

Cal.com Booking Flow

1. Create an event type: In Event types, select New and enter the meeting name, duration, and description.
2. Set availability: Choose an availability schedule and save it.
3. Share the link: Copy the event’s public booking link.
4. Book a slot: As a guest, open the link, select an available date and time, enter the required details, and confirm the booking.
5. Verify the booking: The owner opens Bookings and finds the new entry under Upcoming. If confirmation is required, it first appears under Unconfirmed and moves to Upcoming after approval.
   Out of scope: account registration, external calendar connections, and notifications.
