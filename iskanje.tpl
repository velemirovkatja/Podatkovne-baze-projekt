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

    <title>Seznam vseh filmov</title>

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

      <div class="jumbotron">
        <h2>Seznam filmov, ki vsebujejo niz "{{ iskano_ime }}"</h2>
	<ul>
	%for id, ime in filmi:
    		<li>Film z naslovom <a href="/Seznam_filmov/{{id}}">{{ ime }}</a>
	%end
	</ul>
      </div>

      </div>


      <footer class="footer">
        <p>&copy; Kinospored 2015</p>
      </footer>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/static/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>