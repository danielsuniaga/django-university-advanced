const notificacionSwal = (titleText, text, icon, confirmbuttonText) => {
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon, //warning, error, success, info
        confirmButtonText:confirmbuttonText
    })
}