<!DOCTYPE html>
<html lang="en">
<head>
  <title>Parking</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
	<link href="https://api.mapbox.com/mapbox-gl-js/v2.7.0/mapbox-gl.css" rel="stylesheet">
	<script src="https://api.mapbox.com/mapbox-gl-js/v2.7.0/mapbox-gl.js"></script>
	<link href="http://fonts.cdnfonts.com/css/sofia-pro" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="/style.css">
</head>

<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Website Name</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="/index.html">Home</a></li>
      <li><a href="/parking.html">Park</a></li>
      <li><a href="/studying.html">Study</a></li>
      <li><a href="/eating.html">Eat</a></li>
    </ul>
  </div>
</nav>

<body>
<div class="col-sm-4">
	Welcome <?php echo $_REQUEST["ubit"];.?><br>
	Your parking spot is: <?php echo $_REQUEST["parkingnumber"]; ?>
</div>

</body>