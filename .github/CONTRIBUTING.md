# Contributing to Shel

Thanks for wanting to make Shel better! Every contribution counts — code, docs, ideas, or bug reports.

## Getting Started

1. Fork the repo and clone it:
   ```bash
   git clone https://github.com/shri7-lab/Shel.git
   cd Shel
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the smoke test to verify your setup:
   ```bash
   python test_db.py
   ```

## Development Workflow

1. Create a branch: `git checkout -b feat/my-feature`
2. Make your changes. Follow the existing code style:
   - Type hints on all function signatures
   - Docstrings on public methods
   - Keep modules self-contained under `modules/`
3. Verify nothing broke:
   ```bash
   python test_db.py
   python benchmark/runner.py
   ```
4. Commit with a clear message:
   ```
   feat: add XYZ module
   fix: correct ABC parsing
   docs: clarify quick-start
   ```
5. Push and open a Pull Request against `main`.

## Where to Start

- Look for issues labeled `good first issue` — they're small, well-scoped, and perfect for getting familiar with the codebase.
- The architecture map lives in the README; read it before diving into `agent/`.

## Pull Request Checklist

- [ ] Change is scoped to one feature/bugfix
- [ ] Code has type hints and docstrings
- [ ] `python test_db.py` passes
- [ ] No secrets, API keys, or personal paths in the diff
- [ ] Update README if user-facing behavior changed

## Code of Conduct

All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful, assume good intent, and never use this tool to attack systems you don't own or have explicit permission to test.

## Security

Shel is a security tool — handle it responsibly. Report vulnerabilities privately per our [Security Policy](SECURITY.md). Never open a public issue for a live exploit.
