const $formularioCurso = document.getElementById('formularioCurso');

const $txtNombre = document.getElementById('txtNombre');

const btnsElimininacion = document.querySelectorAll('.btnEliminacion');

(function()
{

    $formularioCurso.addEventListener('submit', function(e)
    {

        let nombre = String($txtNombre.value).trim();

        if(nombre.length==0)
        {
            alert('El nombre del curso no puede ir vacío')

            e.preventDefault();
        }

    });

    btnsElimininacion.forEach(btn => {

        btn.addEventListener('click', function(e){

            let confirmation=confirm("¿Confirma la eliminación del curso?")

            if(!confirmation)
            {
                e.preventDefault();
            }

        })

    });

})();
