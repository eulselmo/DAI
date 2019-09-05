        $(document).ready(function(){
            $("#flip").click(function(){
                $("#panel").slideToggle("slow");
            });
            $("#cambiar").click(function() {
                $("p").css({'color':'blue','font-size':'1.5em'});
                $("h1").css({'color':'white','font-style':'italic'});
            });
            $('ul li:has(ul)').hover(
              function(e)
              {
                $(this).find('ul').css({display: "block"});
              },
              function(e)
              {
                $(this).find('ul').css({display: "none"});
              }
             );
          });

                function click_pag(pagina) {
                $.get ('/get_datos',
                {pag : pagina, valor : valores },
                function (data) {
			d=JSON.parse(data);
			$('#cuerpo_tabla').empty();
			for (fila in d){
				$('#cuerpo_tabla').append('<tr><td>'+d[fila]['nombre']+'</td><td>'+d[fila]['tipo']+'</td><td>'+d[fila]['direccion']+'</td></tr>');
                	}
		}
                );
		};

