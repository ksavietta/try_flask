import json
import sqlite3
from flaskr.db import get_db,init_db_command
from .api.curve_updater import CurveUpdater

	
def fill_db_manual():
	json_filename = 'flaskr/conversion_table_manual_fill.json'
	
	with open(json_filename, 'r') as read_file:
		data = json.load(read_file)
	
	
	db = get_db()
	db.execute('DELETE FROM carbon_conversion_factor') #erases database
	db.commit()
	row_data = []
	for row in data:
		row_data.append(tuple(row.values()))
	db.executemany(
		'INSERT INTO carbon_conversion_factor (display_name, api_name, input_units, output_units,input_to_output,required_flags,required_flags_value)'
		' VALUES (?,?,?,?,?,?,?)',row_data
	)
	db.commit()
def fill_db_api():
	db = get_db()
	db.row_factory = sqlite3.Row
	data = db.execute('SELECT * FROM carbon_conversion_factor').fetchall()
	cu = CurveUpdater()
	for row in data:
		param = row['api_name']
		req_flag_dict = {row['required_flags']:row['required_flags_value']}
		in_rate = cu.vary_param(param,req_flag_dict)
		out_rate = in_rate * row['input_to_output']
		db.execute('UPDATE carbon_conversion_factor SET input_to_co2 = ? WHERE id = ?',
			(out_rate,row['id']))
	db.commit()
