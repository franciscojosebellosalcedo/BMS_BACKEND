
menu = [
    {
        "module": {
            "modulo_Nombre": "Inicio",
            "modulo_Activo": True,
            "modulo_Indice": 1,
            "modulo_Codigo": "INICIO"
        }
    },
    {
        "module": {
            "modulo_Nombre": "Ventas",
            "modulo_Activo": True,
            "modulo_Indice": 2,
            "modulo_Codigo": "VENTAS"
        },
        "submodules": [
            {
                "submodule": {
                    "submo_Nombre": "Catálogo",
                    "submo_Activo": True,
                    "submo_Indice": 1,
                    "submo_Codigo": "VENTAS_CATALOGO"
                },
                "options": [
                    { "opci_Nombre" : "Productos", "opci_Activo": True, "opci_Slug": "SALES_PRODUCTS", "opci_Codigo": "SALES_PRODUCTS" },
                    { "opci_Nombre" : "Marcas", "opci_Activo": True, "opci_Slug": "SALES_BRANDS", "opci_Codigo": "SALES_BRANDS" },
                    { "opci_Nombre" : "Clientes", "opci_Activo": True, "opci_Slug": "SALES_CLIENTS", "opci_Codigo": "SALES_CLIENTS" },
                ]
            }
        ]
    },
    {
        "module": {
            "modulo_Nombre": "Configuración",
            "modulo_Activo": True,
            "modulo_Indice": 5,
            "modulo_Codigo": "CONFIGURACION"
        },
        "submodules": [
            {
                "submodule": {
                    "submo_Nombre": "Seguridad",
                    "submo_Activo": True,
                    "submo_Indice": 1,
                    "submo_Codigo": "CONFIGURACION_SEGURIDAD"
                },
                "options": [
                    { "opci_Nombre" : "Usuarios", "opci_Activo": True, "opci_Slug": "SETTING_USERS", "opci_Codigo": "SETTING_USERS" },
                    { "opci_Nombre" : "Roles", "opci_Activo": True, "opci_Slug": "SETTING_ROLS", "opci_Codigo": "SETTING_ROLS" },
                ]
            }
        ]
    },
]