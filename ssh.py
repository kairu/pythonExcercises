from flask import Flask
import paramiko

app = Flask(__name__)

@app.route('/')
def ssh_connection():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('hostname', username='user', password='1234')

        # Execute a command after connection has been established
        stdin, stdout, stderr = client.exec_command('ls')
        output = stdout.read()

        client.close()
        return f'Successfully connected to the server. Command output: {output}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22)
