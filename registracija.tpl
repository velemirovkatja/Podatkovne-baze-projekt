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

    <title>Kinospored</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/jumbotron.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/signin.css" rel="stylesheet">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Kinospored</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">

        </div><!--/.navbar-collapse -->
      </div>
    </nav>


    <div class="container">
      <form class="form-signin" role="form" method="post" action=".">
        <h2 class="form-signin-heading">Registracija</h2>

	%if napaka:
        <div class="alert alert-warning">{{napaka}}</div>
        %end
 	
	<input type="text" name="uporabnisko_ime" placeholder="Uporabniško ime..." class="form-control"
		%if uporabnisko_ime:
                value="{{uporabnisko_ime}}"
                %end
                required autofocus>
	
	<input type="text" name="ime" placeholder="Polno ime..." class="form-control"
		%if ime:
                value="{{ime}}"
                %end
                required autofocus>

	<input type="password" name="geslo1" placeholder="Vnesi geslo..." class="form-control" required>
	<input type="password" name="geslo2" placeholder="Potrdi geslo..." class="form-control" required>
        
        <button class="btn btn-lg btn-primary btn-block" type="submit">Registriraj me</button>

      </form>
    </div> <!-- /container -->





   
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>