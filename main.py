import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from docx import Document  
from docx.shared import Pt
import io
from flask_wtf import FlaskForm
from wtforms import MultipleFileField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.csrf import CSRFProtect


import magic 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB
app.config['UPLOAD_EXTENSIONS'] = ['.docx']
app.config['MAX_FILES'] = 5 

csrf = CSRFProtect(app)

logging.basicConfig(level=logging.INFO, filename='upload_logs.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def validate_file(form, field):
    files = field.data
    if len(files) > app.config['MAX_FILES']:
        raise ValidationError(f'Maksimal hanya diperbolehkan {app.config["MAX_FILES"]} file.')

class UploadForm(FlaskForm):
    files = MultipleFileField('Unggah Dokumen (.docx):', validators=[
        DataRequired(),
        validate_file
    ])
    submit = SubmitField('Periksa Dokumen')

def allowed_file(filename):
    return os.path.splitext(filename)[1].lower() in app.config['UPLOAD_EXTENSIONS']

def get_mime_type(file_stream):
    """Mengembalikan tipe MIME dari file."""
    mime = magic.Magic(mime=True)
    return mime.from_buffer(file_stream.read(2048))

def check_docx(doc: Document) -> dict:
    report = []
    success = True

    for para in doc.paragraphs:
        for run in para.runs:
            if run.font.name != 'Times New Roman':
                report.append(f'Font tidak sesuai di paragraf: "{para.text[:30]}..."')
                success = False
                break
            if run.font.size and run.font.size.pt != 12:
                report.append(f'Ukuran font tidak sesuai di paragraf: "{para.text[:30]}..."')
                success = False
                break

        if para.paragraph_format.line_spacing is not None:
            spacing = para.paragraph_format.line_spacing
            if spacing != 1.5:
                report.append(f'Spasi tidak sesuai di paragraf: "{para.text[:30]}..."')
                success = False

    sections = doc.sections
    if sections:
        section = sections[0]

        left_margin_cm = section.left_margin.inches * 2.54
        right_margin_cm = section.right_margin.inches * 2.54
        top_margin_cm = section.top_margin.inches * 2.54
        bottom_margin_cm = section.bottom_margin.inches * 2.54

        expected_margins_cm = {
            'left': 4.0,    # 4 cm
            'right': 3.0,   # 3 cm
            'top': 3.0,     # 3 cm
            'bottom': 3.0   # 3 cm
        }

        tolerance = 0.1  # cm

        if abs(left_margin_cm - expected_margins_cm['left']) > tolerance:
            report.append(f'Margin kiri tidak sesuai: {left_margin_cm:.2f} cm (Diharapkan: {expected_margins_cm["left"]} cm)')
            success = False
        if abs(right_margin_cm - expected_margins_cm['right']) > tolerance:
            report.append(f'Margin kanan tidak sesuai: {right_margin_cm:.2f} cm (Diharapkan: {expected_margins_cm["right"]} cm)')
            success = False
        if abs(top_margin_cm - expected_margins_cm['top']) > tolerance:
            report.append(f'Margin atas tidak sesuai: {top_margin_cm:.2f} cm (Diharapkan: {expected_margins_cm["top"]} cm)')
            success = False
        if abs(bottom_margin_cm - expected_margins_cm['bottom']) > tolerance:
            report.append(f'Margin bawah tidak sesuai: {bottom_margin_cm:.2f} cm (Diharapkan: {expected_margins_cm["bottom"]} cm)')
            success = False
    else:
        report.append('Tidak dapat memeriksa margin.')
        success = False

    return {"success": success, "messages": report}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        uploaded_files = form.files.data
        if not uploaded_files:
            flash('Tidak ada file yang diunggah.', 'danger')
            return redirect(request.url)

        reports = []
        for uploaded_file in uploaded_files:
            filename = uploaded_file.filename
            logging.info(f'Menerima file: {filename}')

            if filename == '':
                logging.warning('File kosong diunggah.')
                continue 

            if not allowed_file(filename):
                logging.warning(f'File dengan ekstensi tidak diizinkan diunggah: {filename}')
                reports.append({
                    "success": False,
                    "filename": filename,
                    "messages": ["Silakan unggah file .docx saja."]
                })
                continue

            try:
                file_stream = io.BytesIO(uploaded_file.read())
                mime_type = get_mime_type(file_stream)
                if mime_type != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                    logging.warning(f'Tipe MIME tidak sesuai untuk file {filename}: {mime_type}')
                    reports.append({
                        "success": False,
                        "filename": filename,
                        "messages": ["Tipe file tidak sesuai. Silakan unggah file .docx yang valid."]
                    })
                    continue

                file_stream.seek(0)  
                doc = Document(file_stream)
                report = check_docx(doc)

            except Exception as e:
                logging.error(f'Error memproses file {filename}: {str(e)}')
                report = {"success": False, "messages": ["Gagal membaca dokumen .docx. Pastikan file dalam format yang benar."]}

            report["filename"] = filename
            reports.append(report)

        return render_template('index.html', reports=reports, form=form)

    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error di {field}: {error}', 'danger')

    return render_template('index.html', form=form)

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('File terlalu besar. Maksimal 50MB.', 'danger')
    return redirect(url_for('index')), 413

if __name__ == '__main__':

    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=81, debug=debug_mode)

    print("Isi folder 'templates':", os.listdir('templates'))
    app.run(host='0.0.0.0', port=81)
