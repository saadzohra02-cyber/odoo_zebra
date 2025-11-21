{
    'name': 'Zebra Professional Label System',
    'version': '2.0.0',
    'summary': 'Enterprise-Grade Label Printing Solution for Zebra ZD220',
    'description': """
        🏆 Enterprise Label Printing System
        ==================================
        
        ✨ **المميزات المتقدمة:**
        • تصميم احترافي متجاوب
        • دعم متعدد اللغات
        • إدارة الألوان والعلامات التجارية
        • معالجة ذكية للبيانات
        • تحسينات أداء متقدمة
        • تقارير تحليلية مدمجة
        
        🛠 **التقنيات المدعومة:**
        - PDF عالي الجودة (300 DPI)
        - رموز شريطية متعددة التنسيقات
        - رموز QR ديناميكية
        - تخطيطات قابلة للتخصيص
    """,
    'author': 'Massari Solutions',
    'website': 'https://www.massari-solutions.com',
    'depends': ['base', 'stock', 'product', 'web'],
    'category': 'Inventory/Operations',
    'data': [
        'security/ir.model.access.csv',
        'data/paperformat.xml',
        'data/label_config_data.xml',
        'views/label_config_views.xml',
        'report/label_template.xml',
        'report/label_report.xml',
        'wizards/label_print_wizard.xml',
    ],
    'demo': ['data/label_demo.xml'],
    'assets': {
        'web.assets_backend': [
            'odoo_zebra_label/static/src/css/label_styles.css',
            'odoo_zebra_label/static/src/js/label_actions.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'EUR',
}