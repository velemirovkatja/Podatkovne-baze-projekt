<!DOCTYPE html>
<html lang="si">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/static/favicon.ico">

    <title>Nakup vstopnice</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron-narrow.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
        <nav>
	          
	%if uporabnisko_ime:
          <form class="navbar-form navbar-right">
	    <a class="btn btn-link" role="button">{{uporabnisko_ime}}</a>
            <a href="/odjava/" class="btn btn-xs btn-info" role="button">Odjava</a>  
	  </form>
	%end

        </nav>
        <h3 class="text-muted"><a href="/">Kinospored</a></h3>
      </div>


      <div class="page-header">
        <h1>Nakup vstopnice</h1>
      </div>

      <h3>Podatki o vstopnici:</h3>
	<ul>
	%for naslov_filma, dvorana, termin_predstave, cena, sedez in podatki_vstopnice:
    		<p>Naslov filma: {{ naslov_filma}}</p>
    		<p>Termin predstave: {{ termin_predstave }}</p>
    		<p>Cena vstopnice: {{ cena }} €</p>
	
	%end
	</ul>
	
      <div class="page-header">
         <h2>Vpišite število vstopnic, ki jih želite kupiti (kupite jih lahko največ 5):</h2>
      </div>

	  <form action="/{{id_projekcije}}/nakup_vstopnice/">
	    <p><input type="number" name="stVstopnic" placeholder="Število vstopnic..."></p>
	    <p><button type="submit" class="btn btn-success">Nakup</button></p>
	   
	  </form> 

	    
      </div>


    </div> <!-- /container -->

<br>
    <footer class="footer">
        <p>&copy; Kinospored 2015</p>
    </footer>


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/static/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
