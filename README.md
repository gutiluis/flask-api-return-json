>[!WARNING]
>CURRENTLY UNDER DEVELOPMENT

# API Return JSON Forms App

Flask application that serves an HTML form and returns a JSON response when the form is submitted through a **POST** request, showing form data, headers, files, raw request body, JSON body, client IP, and URL in the jsonify response.

---

## How it works

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python flask_api.py
```

---

## Features

- Serves an HTML form for user input.
- Accepts POST requests and returns all submitted data as JSON.
- Supports:
  - Form fields (request.form)
  - File uploads (request.files)
  - Query parameters (request.args)
  - HTTP headers (request.headers)
  - Raw body (request.data)
  - JSON body (request.get_json)
- Shows client IP (request.remote_addr) and request URL (request.url).

---

## Requirements

- Python 3.7+
- Flask

---

## Tech-Stack

- Python
- Flask
- JSON
- HTML

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see [CONTRIBUTING.md](https://github.com/gutiluis/.github/blob/main/CONTRIBUTING.md) for more information on what we're looking for and how to get started.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/gutiluis/.github/blob/main/CODE_OF_CONDUCT.md).

---

## Security Policy

If you discover a security vulnerability, please review our [Security Policy](https://github.com/gutiluis/.github/blob/main/SECURITY.md) for reporting guidelines.

---

## Support

If you run into any issues or have questions, please check our [SUPPORT.md](https://github.com/gutiluis/.github/blob/main/SUPPORT.md) file for guidance, or reach out through one of our community channels below.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on our **Community** channels:
* **Discord:** [Community channel](https://discord.gg/5xdAFuadP)
* **Slack Workspace:** [technobool.slack.com](https://technobool.slack.com)
* **GitHub Discussions:** [Open a discussion](https://github.com/gutiluis/flask-api-return-json/discussions)

---

## License

[MIT LICENSE](LICENSE)
