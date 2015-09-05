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

    <title>Podatki o filmu</title>

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
          <ul class="nav nav-pills pull-right">

          %if uporabnisko_ime:
          <form class="navbar-form navbar-right">
	    <a class="btn btn-link" role="button">{{uporabnisko_ime}}</a>
            <a href="/odjava/" class="btn btn-xs btn-info" role="button">Odjava</a>  
	  </form>

	  %else:
          <form class="navbar-form navbar-right">
	  
	    <a href="/prijava/" class="btn btn-info" role="button">Prijava</a>
	       
            <a href="/registracija/" class="btn btn-info" role="button">Registracija</a>
          </form>
	  %end

          </ul>
        </nav>
        <h3 class="text-muted"><a href="/">Kinospored</a></h3>
      </div>


      <div class="page-header">
        <h1>Podatki o filmu</h1>
      </div>
       
      <ul>
      %for id, ime, opis, napovednik in podatki:

        <h3>Naslov filma</h3>
        <p>{{ ime }}</p>

        <h3>Opis filma</h3>
        <p>{{ opis }}</p>

        <h3>Napovednik filma</h3>
        <p><a href="{{ napovednik }}">{{ napovednik }}</a></p>
	
	%if uporabnisko_ime:
	  %if opis is None:
	    <form action="/{{id}}/dodaj_opis/" method="POST">
	      <div class="form-group">
	        <input type="text" name="opis" placeholder="Dodaj vsebino filma...">
	        <button type="submit" class="btn btn-success">Dodaj</button>
              </div>
	    </form>
          %end
   	
          <br>

          %if napovednik is None:
	    <form action="/{{id}}/dodaj_napovednik/" method="POST">
  	    <div class="form-group">
	        <input type="text" name="napovednik" placeholder="Povezava do napovednika...">
	        <button type="submit" class="btn btn-success">Dodaj</button>
              </div>
	    </form>
          %end
	%end
      %end
	
      <div class="page-header">
        <h2>Termini predstav</h2>
      </div>
      
        %for id, dvorana, termin_predstave, cena in podatki_projekcije:
          <p>Dvorana filma: {{ dvorana }}</p>
    	  <p>Termin predstave: {{ termin_predstave }}</p>
    	  <p>Cena: {{ cena }} €</p>
	%end

        %if podatki_projekcije:
	  %if uporabnisko_ime:
	    <form action="/{{id}}/nakup_vstopnice/"> 
               <p><a href="{{id}}/nakup_vstopnice/">Kupi vstopnico</a></p>
	     </form>
	  %else:
	    <div class="alert alert-danger" role="alert">
              <strong>Če želite kupiti vstopnico morate biti prijavljeni.</strong>
            </div>
	  %end
        %else:
	  <p>Za izbrani film ni še nobenih razpisanih terminov predstav. Dodali jih bomo kmalu.</p>
        %end

	

      <div class="page-header">
        <h2>Komentarji o filmu</h2>
      </div>
      <div class="panel-body">
	%for kdo, komentar in komentarji:
	  <div class="alert alert-info" role="alert">
          <strong>{{kdo}}:</strong> {{komentar}}
          </div>
	%end
	
	%if uporabnisko_ime:
	<form action="/{{id}}/dodaj_komentar/">
	<div class="form-group">
	  <input type="text" name="komentar" placeholder="Komentar...">
  	  
   	  <button type="submit" class="btn btn-success">Komentiraj</button>
	</form>
	%else:
	<div class="alert alert-danger" role="alert">
           <strong>Če želite komentirati morate biti prijavljeni.</strong>
        </div>
        %end
       
	</ul>

      </div>


    </div> <!-- /container -->

    <footer class="footer">
      <p>&copy; Kinospored 2015</p>
    </footer>


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/static/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
