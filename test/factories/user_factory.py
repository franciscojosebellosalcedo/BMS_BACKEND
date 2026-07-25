def data_create_user ():
    return {
        "user": {
            "usua_Nombre": "Francisco",
            "usua_NombreUsuario": "fran_test",
            "usua_Contrasenia": "123456",
            "usua_RolId": 1,
            "usua_CreacionId": 1,
            "usua_ModificacionId": 1,
            "usua_Activo": True
        },
        "permissions": [
            {
                "peusua_UsuarioId": 1,
                "peusua_OpcionId": 1,
                "peusua_Crear": True,
                "peusua_Editar": True,
                "peusua_CambiarEstado": True,
                "peusua_CreacionId": 1,
                "peusua_ModificacionId": 1
            }
        ]
    }