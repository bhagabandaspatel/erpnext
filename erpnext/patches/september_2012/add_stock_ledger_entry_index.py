import webnotes

def execute():
	webnotes.conn.commit()
	try:
		webnotes.conn.sql("""alter table `tabStock Ledger Entry` add index posting_sort_index(posting_date, posting_time, name)""")webnotes.conn.commit()
	except Exception, e:
		if e.args[0]!=1061: raise e
	webnotes.conn.begin()
	