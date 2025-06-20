from flask import Flask, request, render_template
import base64
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/decrypt_link', methods=['GET', 'POST'])
def decrypt_link():
    decrypted = error = None
    encrypted = request.args.get('encrypted') or request.form.get('encrypted')
    
    if request.method == 'POST':
        key = request.form['key']
        try:
            custom_key = key.ljust(32, '0').encode()
            cipher_suite = Fernet(base64.urlsafe_b64encode(custom_key))
            decrypted = cipher_suite.decrypt(encrypted.encode()).decode()
        except Exception as e:
            error = f"Decryption error: {str(e)}"

    return render_template('decrypt_link.html', encrypted=encrypted, decrypted=decrypted, error=error)

if __name__ == "__main__":
    app.run(debug=True)
