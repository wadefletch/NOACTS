from flask import render_template, session, redirect, url_for
from . import main
from .forms import *
import csv
import os
import json

@main.route('/')
def index():
    return redirect(url_for('main.start'))


@main.route('/scriptreader', methods=['GET', 'POST'])
def script():
    if not session['authenticated']:
        return redirect(url_for('main.start'))
    form = LineEntryForm()
    if form.validate_on_submit():
        form.line.data = ''
    return render_template('scriptreader.html', form=form, session=session)


@main.route('/start', methods=['GET', 'POST'])
def start():
    form = StartForm()

    if form.validate_on_submit():
        session['role'] = form.role.data
        session['script'] = form.script.data
        session['authenticated'] = True
        return redirect(url_for('main.script'))
    return render_template('start.html', form=form)

@main.route('/line/<index>')
def line(index):
    if not session['authenticated']:
        return redirect(url_for('main.start'))
    lines = []
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'static/preordeal.tsv')) as f:
        reader = csv.reader(f, delimiter='\t', )
        lines = []
        for row in reader:
            lines.append(row)
    return json.dumps(lines[int(index)])


