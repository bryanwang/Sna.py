<html>
<head>
	<link rel="stylesheet" type="text/css" href="/snapy/style"/>
  <link rel="stylesheet" type="text/css" href="/snapy/theme"/>
  <meta name="viewport" content="width=320" />
  <meta name="viewport" content="user-scalable=no" />
	<style type="text/css">
      body {
              padding-top: 40px;
              padding-bottom: 40px;
              background-color: #eee;
            }

            .form-signup {
              max-width: 330px;
              padding: 15px;
              margin: 0 auto;
            }
            .form-signup .form-signup-heading,
            .form-signup .checkbox {
              margin-bottom: 10px;
            }
            .form-signup .checkbox {
              font-weight: normal;
            }
            .form-signup .form-control {
              position: relative;
              font-size: 16px;
              height: auto;
              padding: 10px;
              -webkit-box-sizing: border-box;
                 -moz-box-sizing: border-box;
                      box-sizing: border-box;
            }
            .form-signup .form-control:focus {
              z-index: 2;
            }
            .top-cap {
              margin-bottom: -1px;
              border-bottom-left-radius: 0;
              border-bottom-right-radius: 0;
            }
            .middle-plug {
              margin-bottom: -1px;
              border-top-left-radius: 0;
              border-top-right-radius: 0;
              border-bottom-left-radius: 0;
              border-bottom-right-radius: 0;
            }
            .bottom-cap {
              margin-bottom: 10px;
              border-top-left-radius: 0;
              border-top-right-radius: 0;
            }
    </style>
</head>
<body>
	<div class='container' id='auth'>
		<form class='form-signup' action='/snapy/signup' method='POST'>
			<h2 class='form-signup-heading'>Please signup</h2>
			<input class='form-control top-cap' type='text' name='username' placeholder='username' required autofocus/>
			<input class='form-control middle-plug' type='password' name='password' placeholder='password' required/>
      <input class='form-control middle-plug' type='text' name='email' placeholder='email@address.com' required/>
      <input class='form-control bottom-cap' type='text' name='birthday' placeholder='yyyy-mm-dd' required/><br />
			<button type='submit' class='btn btn-lg btn-primary'>Signup</button>
		</form>
</body>
</html>