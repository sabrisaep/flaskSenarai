import os  # untuk urusan baca senarai fail dan padam fail

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    path = 'istilah'
    obj = os.scandir(path)
    senarai = []
    for entry in obj:
        if entry.is_file():
            senarai.append(entry.name[0:-4])
    return render_template('index.html', senarai=senarai)


@app.route('/daftar')
def register():
    return render_template('daftar.html')


@app.route('/daftar_simpan', methods=['POST'])
def daftar_simpan():
    istilah = request.form['istilah']
    namafail = 'istilah/' + istilah + '.txt'
    open(namafail, "x")
    return redirect('/')


@app.route('/papar', methods=['GET'])
def papar():
    args = request.args
    istilah = args.get('istilah')
    namafail = 'istilah/' + istilah + '.txt'
    f = open(namafail, 'r')
    detail = f.readlines()
    f.close()
    return render_template('papar.html', istilah=istilah, detail=detail)


@app.route('/tulis', methods=['GET'])
def tulis():
    args = request.args
    istilah = args.get('istilah')
    namafail = 'istilah/' + istilah + '.txt'
    f = open(namafail, 'r')
    detail = f.read()
    f.close()
    return render_template('tulis.html', istilah=istilah, detail=detail)


@app.route('/tulis_simpan', methods=['POST'])
def tulis_simpan():
    istilah = request.form['istilah']
    keterangan = request.form['keterangan']
    namafail = 'istilah/' + istilah + '.txt'
    f = open(namafail, "w")
    f.write(keterangan)
    f.close()
    return redirect('/')


@app.route('/tambah', methods=['GET'])
def tambah():
    args = request.args
    istilah = args.get('istilah')
    namafail = 'istilah/' + istilah + '.txt'
    f = open(namafail, 'r')
    detail = f.readlines()
    f.close()
    return render_template('tambah.html', istilah=istilah, detail=detail)


@app.route('/tambah_simpan', methods=['POST'])
def tambah_simpan():
    istilah = request.form['istilah']
    keterangan = request.form['keterangan']
    namafail = 'istilah/' + istilah + '.txt'
    f = open(namafail, "a")
    f.write("\n")
    f.write(keterangan)
    f.close()
    return redirect('/')


@app.route('/padam', methods=['GET'])
def padam():
    args = request.args
    namafail = 'istilah/' + args.get('istilah') + '.txt'
    os.remove(namafail)
    return redirect('/')


if __name__ == '__main__':
    app.run()
