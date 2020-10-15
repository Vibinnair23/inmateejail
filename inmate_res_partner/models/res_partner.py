from odoo import fields,models,_,api


class ResPartner(models.Model):

    _inherit = 'res.partner'


    inmate_name = fields.Char(string="Inmates Name")
    inmate_identifier = fields.Selection([('male','Male'),
    										('female','Female'),
    										('gendernon','Gender Nonconforming/Gender Nonbinary'),
    										('transmale','Transgender Male'),
    										('transfemale','Transgender Female'),
    										('None','Other/None'),
    										('decline','Declined to Answer')],string="Inmate Identifies As")
    inmate_suicide_watch = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Was the inmate placed on suicide watch ?')
    inmate_prea_risk = fields.Selection([('yes', 'Yes'),
    									 ('no', 'No'),
    									 ('victim','Victim'),
    									 ('aggresor','Aggresor')], string='Was the inmate flagged as a PREA risk ?')
    inmate_health_issue = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Did the inmate indicate serious mental health issues ?')
    health_issue_note = fields.Text('Note')
    inmate_serious_health_issue = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Did the inmate indicate serious medical issues ?')
    srs_health_issue_note = fields.Text('Note')
    inmate_assault = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Did the inmate assault a staff member')
    inmate_gang = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Did the inmate gang or security threat group affiliation ?')
    completed_by = fields.Char('Completed BY')
    fingerprint_id = fields.Char('Fingerprint ID')
    class_date = fields.Date('Date')
    class_state_id = fields.Char('State Id')
    inmate_first_name = fields.Char('First Name')
    class_fbi_number = fields.Char('FBI Number')
    class_state = fields.Selection([('indiana','Indiana'),
    						('hawaii','Hawaii'),
    						('gendernon','Gender Nonconforming/Gender Nonbinary'),
    						('michigan','Michigan'),
    						('ohio','Ohio')],string="state")
    severe_current_charges = fields.Selection([('Moc','MIsd or Civil'),
    											('low','Low'),
    											('mod','Moderate'),
    											('high','High'),
    											('highest','Highest')],string="SEVERITY OF CURRENT CHARGES/CONVICTIONS")
    serious_felony = fields.Selection([('Moc','MIsd or Civil'),
    									('low','Low'),
    									('mod','Moderate'),
    									('high','High'),
    									('highest','Highest')],string="MOST SERIOUS FELONY CONVICTIONS PAST 10 YEARS")
    institutional_assault = fields.Selection([('none','None'),
    										('assault','Assault not involving use of a weapon'),
    										('sexassault','Predatory or Sexual Assault with or without injury'),
    										('weaponassault','Assault involving use of a weapon or resulting is serious injury')],
    										string="INSTITUTIONAL ASSAULT/FIGHT HISTORY PAST 10 YEAR")
    escape_history = fields.Selection([('noescape','No escape or attempts'),
    									('walkaway','Walk-away from non-secure/minimum security or failure to return'),
    									('withoutviolence','Escape from medium/maximum facility without violence'),
    									('withviolence','Escape from medium/maximum facility with violence')],
    									string="ESCAPE HISTORY")
    disciplinary_history = fields.Selection([('none','None or one (1) minor'),
    									('two','Two or more Minor'),
    									('tampering','Tampering with jail security equipment'),
    									('nonpredatory','Non-Predatory Major Incident(s)'),
    									('predatory','Predatory Major Incident(s)')],
    									string="INSTITUTIONAL DISCIPLINARY HISTORY (Past ten years)")
    prior_felony = fields.Selection([('none','None'),
    									('lom','Low or Moderate'),
    									('high','High'),
    									('highest','Highest')],string="PRIOR FELONY CONVICTIONS PAST 10 YEARS ( excluding questions 1 and 2 above)")
    
    prior_doc_timereserved = fields.Selection([('20','No prior DOC history or more than 20 years DOC me'),
    									('4','Four years or less DOC '),
    									('520','Between 5 to 20 years DOC me'),
    									],string="PRIOR DOC TIMESERVE")
    age = fields.Selection([('38o','Age 38 or over'),
    						('18l','Youthful Offender (less than 18)'),
    						('b28','Age Between 28 - 37'),
    						('b18','Age Between 18 - 27')],string="Age")

    inmate_custody = fields.Selection([('minimum','Minimum'),
    									('medium','Medium'),
    									('maximum','Maximum')],string="Custody")
    inmate_housing = fields.Selection([('gp','General Population'),
    									('pc','Productive Custody'),
    									('med','Medical'),
    									('as','Administrative Segregation'),
    									('mh','Mental Health'),
    									('other','Other')
    									],string="Housing")
    housing_note = fields.Text('Housing Note')
    reason_for_place = fields.Text('REASON(S) FOR PLACEMENT IF THIS DEPARTS FROM RECOMMENDED LEVELS:')
    supervisor_review = fields.Char('SUPERVISOR’S REVIEW / APPROVAL')
    date_housing = fields.Date('Date')
