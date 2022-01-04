{
    "name": "marketing_base",
    "summary": """
        This module is the base of the marketing module""",
    "author": "Xavier Bouquiaux",
    "category": "Marketing",
    "version": "14.0.0.0.1",
    "website": "https://github.com/OCA/web",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "installable": True,
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [],
    "application": True,
    "pre_init_hook": "pre_init_constraints",
}
