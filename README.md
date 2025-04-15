# upgrade-tool-box

Script can be executed with main.py.
Given as argument the Odoo module folder path
or directly from this folder without any argument.

Main Objects:

- Parsers: They manage a type of parsing (ast, etree, ...).
They will loop trough the explicited file types,
build from them using the corresponding library (ast, etree, ...)
and look for any node having the corresponding structure of a Check.

- BaseChecks: They manage the processing of a Check, comparing a node
of a Parser type and returning information about the corresponding elements.

- Checks: Those are the objects that developers should add.
Under checks/<any file.py>. They specify a partner of a BaseChecks
to be found in any node from the Parser. They are designed to be easy to
add (@register_check) and implement using the BaseCheck logic.
