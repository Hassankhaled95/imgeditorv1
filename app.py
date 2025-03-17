import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from rembg import remove
import io

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'تطبيق إزالة الخلفية يعمل بنجاح!'

@app.route('/remove-background', methods=['POST'])
def remove_background_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    input_data = image_file.read()

    # إزالة الخلفية باستخدام rembg
    output_data = remove(input_data)

    # تجهيز الصورة الناتجة لإرسالها كرد باستخدام BytesIO
    output_buffer = io.BytesIO(output_data)
    output_buffer.seek(0)

    return send_file(
        output_buffer,
        mimetype='image/png',
        as_attachment=False,
        download_name='output.png'
    )

if __name__ == '__main__':
    # استخدام متغير البيئة PORT أو المنفذ 5000 افتراضياً
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
