<html>
<head>
	<link rel="stylesheet" type="text/css" href="/snapy/style"/>
  <link rel="stylesheet" type="text/css" href="/snapy/theme"/>
	<style type="text/css">
      body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
      }

      .form-signin {
        max-width: 480px;
        padding: 19px 29px 29px;
        margin: 0 auto 20px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
        -webkit-border-radius: 5px;
           -moz-border-radius: 5px;
                border-radius: 5px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.05);
           -moz-box-shadow: 0 1px 2px rgba(0,0,0,.05);
                box-shadow: 0 1px 2px rgba(0,0,0,.05);
      }
      .form-signin .form-signin-heading,
      .form-signin .checkbox {
        margin-bottom: 10px;
      }
      .form-signin input[type="text"],
      .form-signin input[type="password"] {
        font-size: 16px;
        height: auto;
        margin-bottom: 15px;
        padding: 7px 9px;
      }

    </style>
</head>
<body>
	<div class='container' id='auth'>
		<form class='form-signin' action='/snapy/web_login' method='POST'>
			<h2 class='form-signin-heading'>Please sign in</h2>
			Username:<br /><input class='input-block-level form-control' type='text' name='username' required='required'/><br />
			Password:<br /><input class='input-block-level form-control' type='password' name='password' required='required'/><br />
			<button type='submit' class='btn btn-lg btn-primary'>Login</button><br />
      <br /><a href='/snapy/web_signup'>Don't have an account?</a>		</form>
</body>
</html>