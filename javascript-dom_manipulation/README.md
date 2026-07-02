# javascript-dom_manipulation

Manipulating the DOM with vanilla JavaScript: selecting elements, listening
to events, updating styles/classes/content, creating elements, and fetching
data from an API with the Fetch API.

## Learning Objectives

At the end of this project, you should be able to explain, without the help
of Google:

- How to select HTML elements in JavaScript
- How to add an event listener to an HTML element in JavaScript
- How to manipulate the class list of an HTML element
- How to modify the style of an HTML element in JavaScript
- How to modify the content of an HTML element in JavaScript
- How to make a `GET` API call with the Fetch API in JavaScript
- Async programming basics with Promises

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts are executed in a browser (Google Chrome, latest version)
- All files should end with a new line
- Code must be semistandard compliant (version 16.x.x): rules of Standard +
  semicolons on top
- No import/export of code is allowed
- Every `N-script.js` is tested against the matching `N-main.html`

## Tasks

| File | Description |
| --- | --- |
| `0-script.js` | Colors the `header` element text red |
| `1-script.js` | Colors the `header` red when `#red_header` is clicked |
| `2-script.js` | Adds the `red` class to `header` when `#red_header` is clicked |
| `3-script.js` | Toggles `header` between the `red` and `green` classes when `#toggle_header` is clicked |
| `4-script.js` | Adds a `<li>Item</li>` to `ul.my_list` when `#add_item` is clicked |
| `5-script.js` | Updates `header` text to `New Header!!!` when `#update_header` is clicked |
| `6-script.js` | Fetches a Star Wars character name and displays it in `#character` |
| `7-script.js` | Fetches Star Wars movie titles and lists them in `#list_movies` |
| `8-script.js` | Fetches a translated "hello" and displays it in `#hello`, loaded from `<head>` |

## Usage

Open the matching `N-main.html` file in a browser (or serve the folder with
a local HTTP server) to test each script, e.g.:

```
python3 -m http.server 8000
```

Then visit `http://localhost:8000/0-main.html`, etc.
