from pathlib import Path

lines = [
    "Sticky Notes Django Fix Report",
    "",
    "Problem 1:",
    "The Django app would not start because the shell was using the wrong Python interpreter.",
    "Running python manage.py runserver returned ModuleNotFoundError: No module named django.",
    "",
    "Problem 2:",
    "After the server started, the homepage still failed because the root URL '/' was not mapped to the notes app.",
    "Django returned a Page not found error at the homepage.",
    "",
    "Problem 3:",
    "The notes database tables were missing, so the notes page could not render properly.",
    "The app raised an OperationalError for the notes_note table.",
    "",
    "Fixes applied:",
    "1. Started the project with the workspace virtual environment at .venv/Scripts/python.exe.",
    "2. Added a PowerShell launcher script, start_server.ps1, to make future launches consistent.",
    "3. Updated sticky_notes/urls.py to route the root path '' to the notes URLs.",
    "4. Added ALLOWED_HOSTS entries for 127.0.0.1, localhost, and testserver.",
    "5. Created and applied the missing migration for the Note model.",
    "6. Added a regression test to confirm the homepage loads successfully.",
    "",
    "Result:",
    "The application now runs successfully at http://127.0.0.1:8000/ and the homepage responds correctly.",
]

# Build a very small PDF manually.


def escape_pdf_text(text: str) -> str:
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


objects = []
content_lines = []
for i, line in enumerate(lines):
    y = 760 - (i * 14)
    content_lines.append(
        f"BT /F1 12 Tf 50 {y} Td ({escape_pdf_text(line)}) Tj ET")

content_stream = "\n".join(content_lines)

pdf = []
pdf.append('%PDF-1.4')
pdf.append('1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj')
pdf.append('2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj')
pdf.append(
    '3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj')
pdf.append('4 0 obj << /Length 0 >> stream')
pdf.append(content_stream)
pdf.append('endstream endobj')
pdf.append('5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj')
pdf.append('xref')
pdf.append('0 6')
pdf.append('0000000000 65535 f ')
# Simple offsets are not required for a basic PDF; this is enough for viewers to open it.
pdf.append('trailer << /Size 6 /Root 1 0 R >>')
pdf.append('startxref')
pdf.append('0')
pdf.append('%%EOF')

output_path = Path(__file__).with_suffix('.pdf')
output_path.write_bytes("\n".join(pdf).encode('latin-1'))
print(output_path)
