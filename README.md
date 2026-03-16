# Recipol UI

Recipol UI is a desktop application for inspecting MTP (`.aml`) files and recipe (`.xml`) files, visualizing the parsed hierarchy, and monitoring recipe execution as a Sequential Function Chart (SFC). It provides a Home page for file management, an MTP Viewer for browsing services/procedures/parameters, a Recipe Monitor with an SFC diagram, and a Logs page for execution output.

**Features**
1. Home page file manager for importing `.aml` (MTP) and `.xml` (recipe) files and grouping them by type.
2. Multi-select table with quick actions to **Import**, **Delete Selected**, and **Reset Selection**.
3. One-click **Inspect** that parses selected files and drives the rest of the UI.
4. MTP Viewer that shows the parsed hierarchy (Service ? Procedure ? Parameter) with IDs, types, default values, and limits.
5. Recipe Monitor that renders Sequential Function Chart (SFC) flows with steps and transitions, including zoom controls.
6. Optional recipe execution via OPC UA, with live highlighting of active steps/transitions.
7. Execution log view to track parsing, generation, and run-time status messages.

**Requirements**
- Python 3.10+ (the code uses `X | None` union type hints).
- Dependencies (install via `pip`):
  - `PyQt6`
  - `qfluentwidgets`
  - `asyncua`
  - `defusedxml`
  - `xmlschema`

Example:
```bash
pip install PyQt6 qfluentwidgets asyncua defusedxml xmlschema
```

**Usage**
1. Start the app:
   ```bash
   python gui_main.py
   ```
2. Home page workflow:
   - Click **Import File** to add `.aml` (MTP) and/or `.xml` (recipe) files.
   - Imported files are copied to `Code/Recipol/Artifact`.
   - Select one or more rows in the table to enable **Inspect**.
   - Use **Delete Selected** to remove files from the artifact folder.
   - Use **Reset Selection** to clear the table selection and reset progress.
3. Inspect files:
   - Click **Inspect** to parse MTP files and/or generate SFC data from recipe files.
   - Progress is shown in the progress bar, and details appear in **Logs**.
4. MTP Viewer:
   - Switch to **MTP Viewer** to browse parsed modules.
   - Use the dropdown to select an MTP module.
   - Expand the tree to view Services, Procedures, and Parameters with IDs and values.
5. Recipe Monitor (SFC):
   - Switch to **Recipe Monitor** to view SFC diagrams generated from recipes.
   - Choose a recipe from the dropdown to render its flow.
   - Use the on-canvas controls to zoom in/out or reset the view.
6. Execute recipe (OPC UA):
   - After **Inspect**, click **Execute Recipe** (enabled when MTP data is available).
   - The monitor highlights running steps and transitions.
   - If the backend requests input, a prompt dialog appears.
7. Logs:
   - Open **Logs** to see parsing status, warnings, and execution output.

**Contributors**
- Yuanchen Zhao
- Alicia Eve

**Third-Party Notices**
This project uses the following third-party packages. Copyright remains with their respective authors and contributors. See each package's license for details.
- `PyQt6`
- `qfluentwidgets`
- `asyncua`
- `defusedxml`
- `xmlschema`
