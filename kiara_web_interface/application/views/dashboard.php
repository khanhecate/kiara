
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
				<form action="<?=base_url('home/index') ?>" method="post">
					<input type="hidden" name="query" value="uname -a">
					<input type="submit" name="submit" class="btn btn-primary">
				</form>
			</div>
		</div>
</body>
</html>