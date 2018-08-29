import json
import sqlite3
from flaskr.db import get_db,init_db_command
class DBBackfill:
    json_filename = 'conversion_table_manual_fill.json'
    def fill_db_manual(self):
        with open(self.json_filename, 'r') as read_file:
            data = json.load(read_file)
	    init_db_command #erases database
	    db = get_db()


    	row_data = []
		for row in data:
		    row_data.append(tuple(row.values()))
		db.executemany(
    		'INSERT INTO carbon_conversion_factor (display_name, api_name, input_units, output_units,input_to_output,required_flags,required_flags_value)'
    		' VALUES (?,?,?,?,?,?,?)',cmmd
		)
		db.commit()
