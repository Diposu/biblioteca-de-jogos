$('form input[type="file"]').change(event => {
    let arquivo = event.target.files;
    if (arquivos.length === 0 ){
        console.log('sem imagem para mostrar')
    }
    else {
        if (arquivo[0].type == 'image/jpeg') {
            $('img').remove();
            let imagem = $('<img class="img-responsive">');
            imagem.attr('src', window.URL.createObjectURL(arquivo[0]));
            $('figure').prepend(imagem);
        }
        else {
            alert('formato nao suportado')
        }
    }
});