# python-server_side_rendering

Server-side rendering (SSR) in Python: generating text files from a
template, and building Flask applications that render dynamic HTML pages
with Jinja from in-memory data, JSON, CSV, and a SQLite database.

## Learning Objectives

- Understand server-side rendering and how it differs from client-side
  rendering.
- Implement SSR in Python using the Flask framework.
- Use the Jinja templating engine to dynamically generate HTML pages,
  including loops, conditionals, and reusable `{% include %}` components.
- Read and display data from JSON, CSV, and SQLite sources.
- Handle dynamic content, query parameters, and error cases gracefully.

## Requirements

- Python 3
- Flask (`pip install Flask`)

## Files

| File | Description |
| --- | --- |
| `task_00_intro.py` | `generate_invitations(template, attendees)`: generates `output_X.txt` invitation files from `template.txt`, with validation for empty/invalid inputs and `"N/A"` fallback for missing data |
| `template.txt` | Invitation template with `{name}`, `{event_title}`, `{event_date}`, `{event_location}` placeholders |
| `task_01_jinja.py` | Flask app serving `/`, `/about`, `/contact` with shared `header.html` / `footer.html` includes |
| `task_02_logic.py` | Adds `/items`, rendering a list read from `items.json` with a loop and an empty-list conditional |
| `items.json` | Sample list of items for `/items` |
| `task_03_files.py` | Adds `/products?source=json\|csv&id=<id>`, reading and optionally filtering `products.json` / `products.csv` |
| `products.json` / `products.csv` | Sample product data |
| `task_04_db.py` | Extends `/products` with `source=sql`, reading from a SQLite `products.db` (auto-created and seeded on startup) |
| `templates/` | Jinja templates: `header.html`, `footer.html`, `index.html`, `about.html`, `contact.html`, `items.html`, `product_display.html` |

## Usage

```
python3 task_00_intro.py   # library only, see example below
python3 task_01_jinja.py   # http://localhost:5000/
python3 task_02_logic.py   # http://localhost:5000/items
python3 task_03_files.py   # http://localhost:5000/products?source=json
python3 task_04_db.py      # http://localhost:5000/products?source=sql
```

Example for `task_00_intro.py`:

```python
from task_00_intro import generate_invitations

with open('template.txt') as f:
    template_content = f.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference",
     "event_date": "2023-07-15", "event_location": "New York"},
]

generate_invitations(template_content, attendees)
```

## Error handling

- `generate_invitations`: logs an error and does nothing when `template`
  is not a string, `attendees` is not a list of dictionaries, the template
  is empty, or the attendee list is empty. Missing per-attendee fields are
  rendered as `"N/A"`.
- `/products`: renders `"Wrong source"` when `source` is not `json`, `csv`
  or `sql`, and `"Product not found"` when `id` does not match any product.
