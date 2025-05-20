# run doc tasks
[group('doc')]
doc: doc-build

# build documentation
[group('doc')]
doc-build output="docs/html": clean-docs
    uv run pdoc --output-directory={{output}} {{SOURCES}}/{{PACKAGE}}

# serve documentation
[group('doc')]
doc-serve port="8088":
    uv run pdoc --port={{port}} {{SOURCES}}/{{PACKAGE}}
