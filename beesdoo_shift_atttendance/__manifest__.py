{
    'name': "Beescoop Shift Attendance Sheet",

    'summary': """
        Volonteer Timetable Management
        Attendance Sheet""",

    'description': """

    """,

    'author': "Elouan Le Bars, Coop It Easy",
    'website': "https://github.com/beescoop/Obeesdoo",

    'category': 'Cooperative management',
    'version': '12.0.1.0.0',

    'depends': [
        'beesdoo_shift',
        'beesdoo_worker_status',
        'mail', 
        'barcodes', #Need for attendance_sheet that will be move to another module
    ],

    'data': [
        "data/system_parameter.xml",
        "data/cron.xml",
        "data/mail_template.xml",
        "security/group.xml",
        "security/ir.model.access.csv",
        "views/res_config_settings_view.xml",
        "wizard/validate_attendance_sheet.xml",
        "views/attendance_sheet.xml",
    ],
    'demo': []
}
