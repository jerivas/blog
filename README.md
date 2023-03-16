# Ed Rivas: Blog

[![Netlify Status](https://api.netlify.com/api/v1/badges/db73abe4-679b-427a-8a02-5f019471dfbe/deploy-status)](https://app.netlify.com/sites/jerivas-blog/deploys)

This blog is brought to you by
[Pelican](https://docs.getpelican.com/en/4.8.0/index.html): a static site
generator for Python.

## Contributing

Contributions are welcome! You will need the following:

- A fork of this repository
- Python (see `runtime.txt` for the specific version)
- A virtual environment (or your preferred Python environment abstraction)

After cloning the forked repository, install the requirements:

```bash
pip install requirements.txt
```

Now start Pelican in reload and listen mode:

```bash
pelican --autoreload --listen
```

Visit http://localhost:8000. The site will be re-built when you save changes to
files inside `content/`. Changing the settings might require a manual server
restart.

Finally, open a pull request from your fork. Netlify will generate a preview
link in the "Checks" section to preview your changes.