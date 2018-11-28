$(document).ready(function(){
    
    $("#formularioMisperris").validate({
        rules:{
            txtCorreo:{
                required:true,
                minlength:3,
                maxlength:20,
                email:true
            },
            txtRun:{
                required:true,
                maxlength:9,
                minlength:9
            },

            txtDireccion:{
                required:true
            },
            txtNombreCompleto:{
                required:true,
                number:false
            },

            txtTelefono:{
                required:true,
                maxlength:9,
                minlength:9
            },

            txtFecha:{
                required:true,
                date:true
            },
            
            cboRegion:{
                required:true
            },

            cboCuidad:{
                required:true
            },

            cboVivienda:{
                required:true
            }
        },
        messages:{
            txtCorreo:{
                required:"Este campo es Obligatorio",
                minlength:"minimo 3 letras",
                maxlength:"maximo 25 letras",
                email:"Debe ingresar un correo valido"
            },
            txtRun:{
                required:"Este campo es Obligatorio",
                maxlength:"Debe contener 9 digitos",
                minlength:"Debe contener 9 digitos",
            },

            txtDireccion:{
                required:"Este campo es obligatorio"
            },
            txtNombreCompleto:{
                required:"Este campo es Obligatorio",
                text:"No debe ingresar numeros, solo letras",
                number:"Solo ingresar letras"
            },

            cboRegion:{
                required:"Este campo es Obligatorio"
            },

            txtTelefono:{
                required:"Porfavor ingrese su numero",
                maxlength:"Debe contener 9 digitos",
                minlength:"Debe contener 9 digitos"
            },

            txtFecha:{
                required:"Fecha obligatoria",
                min:"Debe ingresar una fecha entre 1950 y 2001",
                max:"Debe ingresar una fecha entre 1950 y 2001"
            },

            cboRegion:{
                required:"Campo Obligatorio"
            },

            cboCuidad:{
                required:"Campo Obligatorio"
            },

            cboVivienda:{
                required:"Campo Obligatorio"
            }
        }
    });

});