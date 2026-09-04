# Recovery Factory (stream 1)

Clean implementation of **DQ-RCV-URS-001** and **DQ-RCV-DS-001**.

Three artifacts are inputs. None of them is a prompt.

```
sealed XML zip
requirements (URS)
solution design
        ↓
   frozen specs/     ← humans own these
        ↓
   factory code      ← Cursor implements against the specs
        ↓
   named unittest    ← the only acceptance
        ↓
   evidence pack     ← rules, matrix, coverage, questions, run-manifest
        ↓
   human ratification ← name a type, settle a reading
```

Cursor is the mechanic. The URS and the design are the drawing.
The zip is the part on the bench. The unit test is the torque spec.
A person still stamps the type name.

## One-time setup

```bash
git clone git@github.com:apoondla612/dq-recovery-factory.git
cd dq-recovery-factory
python3 -m venv .venv && source .venv/bin/activate
pip install lxml
cp /path/to/Test-Mappings-Export.zip packages/Test-Mappings-Export.zip
```

Point Cursor at this repo. `.cursor/rules/recovery.mdc` is always-on.

## Commands

```bash
export PYTHONPATH=src
python -m unittest discover -s tests -q
python -m dq_recovery.cli recover --export packages/Test-Mappings-Export.zip --out artifacts/proof --repo .
```

See `IMPLEMENTATION.md` for REQ → module → test.
See `AGENTS.md` for the must-not list.
