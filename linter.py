from SublimeLinter.lint import Linter


class JSONSchemaLint(Linter):
    cmd = 'jsonschema-lint ${file_on_disk}'
    name = 'jsonschema-lint'
    regex = r'(?P<filename>.*):(?P<line>[1-9][0-9]*):(?P<col>[1-9][0-9]*):(?P<end_line>[1-9][0-9]*):(?P<end_col>[1-9][0-9]*): (?P<message>.*)'
    tempfile_suffix = "-"
    multiline = False
    defaults = {
        'selector': 'source.json, source.yaml'
    }
