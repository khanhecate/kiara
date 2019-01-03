
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="<?=base_url('assets/css/bootstrap-material-design.min.css') ?>">
	<script type="text/javascript" src="<?=base_url('assets/js/bootstrap-material-design.min.js') ?>"></script>
</head>
<body>
	<style type="text/css">
		@font-face{
			font-family: sans;
			src:url('<?=base_url('assets/font/SourceSansPro-Regular.ttf') ?>');

		}
		body{
			font-family: sans;
		}
	</style>
		<div class="row">
			<div class="container mt-5">
			<div class="alert alert-danger" role="alert">
				<?php 
				error_reporting(0);
				if($_GET['login']){
					echo "Login Error ! Username or Password does'nt match!";
				}else{
					echo "Connect Your Server By Login In This Site";
				}

				 ?>
			  
			</div>
			<hr>
			<form action="<?=base_url('home/do_auth') ?>" method="post">
				<div class="container">
				<div class="row">
					
					<div class="col-md-6">
					<div class="form-group">
					    <label for="exampleInputEmail1">Hostname / IP Adress</label>
					    <input autocomplete="off" type="text" name="hostname" class="form-control">
					    <small id="emailHelp" class="form-text text-muted">example.com / 127.0.0.1</small>
					  </div>
					  </div>
					  <div class="col-md-6">
					<div class="form-group">
					    <label for="port">Target Port (SSH)</label>
					    <input type="number" value="22" name="port" class="form-control">
					    <small id="emailHelp" class="form-text text-muted">Numeric Number , By Default is : 22</small>
					  </div>
					  </div>
					  <div class="col-md-6">
					  	<div class="form-group">
					    <label for="username">Target Username</label>
					    <input autocomplete="off" type="text" name="username" class="form-control">
					    <small id="emailHelp" class="form-text text-muted">Username For Your Target Server</small>
					  </div>
					  </div>
					  <div class="col-md-6">
					  	<div class="form-group">
					    <label for="password">Target Password</label>
					    <input type="password" name="password" class="form-control">
					    <small id="emailHelp" class="form-text text-muted">Password For Your Target Server</small>
					  </div>
					  </div>
					  <input type="submit" class="btn btn-outline-primary btn-block" name="login" value="Login">
				  </div>
				  </div>
			</form>
			</div>
		</div>
</body>
</html>